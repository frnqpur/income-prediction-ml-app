"""
Train a valid Income Prediction model for the Streamlit demo.

This script intentionally avoids the leakage pattern found in the old notebook:
- it does not use Class as a feature;
- it does not create or use cluster from the target;
- it excludes race, sex, native.country, and fnlwgt from the public demo model.

Run:
    python train_model.py
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

RANDOM_STATE = 99
TEST_SIZE = 0.30

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "adult_dataset.csv"
ARTIFACT_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACT_DIR / "income_prediction_pipeline.joblib"
METRICS_PATH = ARTIFACT_DIR / "metrics.json"
METADATA_PATH = ARTIFACT_DIR / "metadata.json"

TARGET_COLUMN = "income"
ORIGINAL_TARGET_COLUMN = "Unnamed: 14"

FEATURE_COLUMNS = [
    "age",
    "workclass",
    "education",
    "education.num",
    "marital.status",
    "occupation",
    "relationship",
    "capital.gain",
    "capital.loss",
    "hours.per.week",
]

NUMERIC_FEATURES = [
    "age",
    "education.num",
    "capital.gain",
    "capital.loss",
    "hours.per.week",
]

CATEGORICAL_FEATURES = [
    "workclass",
    "education",
    "marital.status",
    "occupation",
    "relationship",
]

EXCLUDED_COLUMNS = [
    "Class",
    "cluster",
    "fnlwgt",
    "race",
    "sex",
    "native.country",
]


def load_dataset(csv_path: Path) -> pd.DataFrame:
    """Load and normalize the Adult income dataset."""
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset tidak ditemukan: {csv_path}\n"
            "Copy adult_dataset.csv ke folder demo-app/data/ terlebih dahulu."
        )

    df = pd.read_csv(csv_path)

    if ORIGINAL_TARGET_COLUMN in df.columns:
        df = df.rename(columns={ORIGINAL_TARGET_COLUMN: TARGET_COLUMN})
    elif "Class" in df.columns:
        df = df.rename(columns={"Class": TARGET_COLUMN})

    if TARGET_COLUMN not in df.columns:
        raise ValueError(
            f"Kolom target tidak ditemukan. Harus ada '{ORIGINAL_TARGET_COLUMN}', 'Class', atau '{TARGET_COLUMN}'."
        )

    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].astype(str).str.strip()

    df = df.replace("?", np.nan)

    missing_features = [column for column in FEATURE_COLUMNS if column not in df.columns]
    if missing_features:
        raise ValueError(f"Kolom fitur tidak ditemukan: {missing_features}")

    return df


def build_pipeline() -> Pipeline:
    """Create preprocessing + classifier pipeline."""
    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
        ]
    )

    classifier = GradientBoostingClassifier(random_state=RANDOM_STATE)

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", classifier),
        ]
    )

    return pipeline


def evaluate_model(
    pipeline: Pipeline,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    y_train: pd.Series,
) -> Dict[str, object]:
    """Evaluate the trained model and return serializable metrics."""
    y_pred = pipeline.predict(X_test)
    y_proba = pipeline.predict_proba(X_test)[:, list(pipeline.classes_).index(">50K")]

    baseline_accuracy = float(y_train.value_counts(normalize=True).max())

    metrics = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "model_name": "GradientBoostingClassifier",
        "random_state": RANDOM_STATE,
        "test_size": TEST_SIZE,
        "baseline_majority_class_accuracy": baseline_accuracy,
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "f1_score_positive_class_gt_50k": float(f1_score(y_test, y_pred, pos_label=">50K")),
        "roc_auc_positive_class_gt_50k": float(roc_auc_score((y_test == ">50K").astype(int), y_proba)),
        "confusion_matrix_labels": ["<=50K", ">50K"],
        "confusion_matrix": confusion_matrix(y_test, y_pred, labels=["<=50K", ">50K"]).tolist(),
        "classification_report": classification_report(y_test, y_pred, output_dict=True),
    }
    return metrics


def train_model(
    csv_path: Path = DATA_PATH,
    artifact_dir: Path = ARTIFACT_DIR,
) -> Tuple[Pipeline, Dict[str, object]]:
    """Train, evaluate, and save the model pipeline."""
    df = load_dataset(csv_path)

    X = df[FEATURE_COLUMNS].copy()
    y = df[TARGET_COLUMN].copy()

    if TARGET_COLUMN in X.columns or "Class" in X.columns or "cluster" in X.columns:
        raise ValueError("Data leakage terdeteksi: target atau cluster masuk ke fitur.")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    metrics = evaluate_model(pipeline, X_test, y_test, y_train)

    metadata = {
        "project": "Income Prediction Demo",
        "target_column": TARGET_COLUMN,
        "target_classes": ["<=50K", ">50K"],
        "feature_columns": FEATURE_COLUMNS,
        "numeric_features": NUMERIC_FEATURES,
        "categorical_features": CATEGORICAL_FEATURES,
        "excluded_columns": EXCLUDED_COLUMNS,
        "leakage_note": "This demo model does not use Class, cluster, or any feature derived from the target.",
        "fairness_note": "The public demo form excludes race and sex. Predictions are for portfolio demonstration only.",
    }

    artifact_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, artifact_dir / MODEL_PATH.name)

    with open(artifact_dir / METRICS_PATH.name, "w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=2)

    with open(artifact_dir / METADATA_PATH.name, "w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=2)

    return pipeline, metrics


if __name__ == "__main__":
    _, training_metrics = train_model()

    print("Training selesai.")
    print(f"Model disimpan ke: {MODEL_PATH}")
    print(f"Metrics disimpan ke: {METRICS_PATH}")
    print()
    print("Ringkasan metrics:")
    print(f"Baseline accuracy: {training_metrics['baseline_majority_class_accuracy']:.4f}")
    print(f"Accuracy: {training_metrics['accuracy']:.4f}")
    print(f"F1-score >50K: {training_metrics['f1_score_positive_class_gt_50k']:.4f}")
    print(f"ROC-AUC >50K: {training_metrics['roc_auc_positive_class_gt_50k']:.4f}")
