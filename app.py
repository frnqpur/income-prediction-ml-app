"""
Recruiter-ready Streamlit demo for the Income Prediction project.

Run locally:
    streamlit run app.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import joblib
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
ARTIFACT_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACT_DIR / "income_prediction_pipeline.joblib"
METRICS_PATH = ARTIFACT_DIR / "metrics.json"
METADATA_PATH = ARTIFACT_DIR / "metadata.json"
SAMPLE_INPUT_PATH = BASE_DIR / "sample_input.csv"

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

EDUCATION_NUM_MAP = {
    "Preschool": 1,
    "1st-4th": 2,
    "5th-6th": 3,
    "7th-8th": 4,
    "9th": 5,
    "10th": 6,
    "11th": 7,
    "12th": 8,
    "HS-grad": 9,
    "Some-college": 10,
    "Assoc-voc": 11,
    "Assoc-acdm": 12,
    "Bachelors": 13,
    "Masters": 14,
    "Prof-school": 15,
    "Doctorate": 16,
}

WORKCLASS_OPTIONS = [
    "Private",
    "Self-emp-not-inc",
    "Self-emp-inc",
    "Federal-gov",
    "Local-gov",
    "State-gov",
    "Without-pay",
    "Never-worked",
]

MARITAL_STATUS_OPTIONS = [
    "Never-married",
    "Married-civ-spouse",
    "Divorced",
    "Separated",
    "Widowed",
    "Married-spouse-absent",
    "Married-AF-spouse",
]

OCCUPATION_OPTIONS = [
    "Adm-clerical",
    "Exec-managerial",
    "Handlers-cleaners",
    "Prof-specialty",
    "Other-service",
    "Sales",
    "Craft-repair",
    "Transport-moving",
    "Farming-fishing",
    "Machine-op-inspct",
    "Tech-support",
    "Protective-serv",
    "Armed-Forces",
    "Priv-house-serv",
]

RELATIONSHIP_OPTIONS = [
    "Not-in-family",
    "Husband",
    "Wife",
    "Own-child",
    "Unmarried",
    "Other-relative",
]

st.set_page_config(
    page_title="Income Prediction Demo",
    page_icon="📊",
    layout="centered",
)


def add_page_style() -> None:
    """Small CSS polish without making the app heavy."""
    st.markdown(
        """
        <style>
            .main .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
                max-width: 980px;
            }
            .hero-card {
                padding: 1.15rem 1.25rem;
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 18px;
                background: linear-gradient(135deg, #111827, #1f2937);
                margin-bottom: 1.1rem;
                color: #ffffff;
            }
            .hero-card h1 {
                color: #ffffff;
            }
            .hero-card p {
                color: #e5e7eb;
            }
            .hero-card strong {
                color: #93c5fd;
            }
            .small-muted {
                color: #667085;
                font-size: 0.92rem;
            }
            div[data-testid="stMetric"] {
                border: 1px solid rgba(49, 51, 63, 0.10);
                border-radius: 14px;
                padding: 0.75rem 0.85rem;
                background: rgba(255, 255, 255, 0.7);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_resource(show_spinner=False)
def load_pipeline() -> Any:
    """Load the saved scikit-learn pipeline."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file tidak ditemukan: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


@st.cache_data(show_spinner=False)
def load_json(path: Path) -> Optional[Dict[str, Any]]:
    """Read JSON safely. Return None when the file is unavailable or invalid."""
    if not path.exists():
        return None
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return None


def format_percent(value: Any) -> str:
    """Format numeric values as percentages."""
    try:
        return f"{float(value) * 100:.2f}%"
    except (TypeError, ValueError):
        return "N/A"


def confidence_label(probability: float) -> str:
    """Human-readable confidence summary for recruiter-friendly output."""
    if probability >= 0.80:
        return "High confidence"
    if probability >= 0.60:
        return "Moderate confidence"
    return "Low confidence"


def build_input_dataframe(
    age: int,
    workclass: str,
    education: str,
    marital_status: str,
    occupation: str,
    relationship: str,
    capital_gain: int,
    capital_loss: int,
    hours_per_week: int,
) -> pd.DataFrame:
    """Create the single-row input expected by the saved pipeline."""
    education_num = EDUCATION_NUM_MAP[education]
    return pd.DataFrame(
        [
            {
                "age": age,
                "workclass": workclass,
                "education": education,
                "education.num": education_num,
                "marital.status": marital_status,
                "occupation": occupation,
                "relationship": relationship,
                "capital.gain": capital_gain,
                "capital.loss": capital_loss,
                "hours.per.week": hours_per_week,
            }
        ],
        columns=FEATURE_COLUMNS,
    )


def get_prediction_summary(pipeline: Any, input_data: pd.DataFrame) -> Tuple[str, Optional[float], Dict[str, float]]:
    """Predict one row and return label, confidence, and class probabilities."""
    prediction = str(pipeline.predict(input_data)[0])
    probability_by_class: Dict[str, float] = {}

    if hasattr(pipeline, "predict_proba"):
        probabilities = pipeline.predict_proba(input_data)[0]
        classes = [str(label) for label in pipeline.classes_]
        probability_by_class = {
            class_label: float(probability)
            for class_label, probability in zip(classes, probabilities)
        }
        confidence = probability_by_class.get(prediction)
    else:
        confidence = None

    return prediction, confidence, probability_by_class


def render_header() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <h1 style="margin-bottom: 0.25rem;">Income Prediction ML App</h1>
            <p class="small-muted" style="margin-bottom: 0;">
                An end-to-end machine learning demo that predicts income category using a trained
                preprocessing and classification pipeline.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(
        "Portfolio note: this demo does not use the target column, target-derived cluster, race, or sex as model inputs."
    )


def render_sidebar(metadata: Optional[Dict[str, Any]], metrics: Optional[Dict[str, Any]]) -> None:
    with st.sidebar:
        st.header("Model info")
        if metadata:
            st.write(f"**Project:** {metadata.get('project', 'Income Prediction Demo')}")
            st.write(f"**Target:** `{metadata.get('target_column', 'income')}`")
            st.write("**Classes:** `<=50K`, `>50K`")
            st.write("**Saved model:** `.joblib` pipeline")
        else:
            st.info("metadata.json tidak tersedia. App tetap dapat berjalan jika model tersedia.")

        if metrics:
            st.divider()
            st.write("**Latest training metrics**")
            st.write(f"Accuracy: **{format_percent(metrics.get('accuracy'))}**")
            st.write(f"F1 >50K: **{format_percent(metrics.get('f1_score_positive_class_gt_50k'))}**")
            st.write(f"ROC-AUC >50K: **{format_percent(metrics.get('roc_auc_positive_class_gt_50k'))}**")

        if SAMPLE_INPUT_PATH.exists():
            st.divider()
            st.download_button(
                label="Download sample_input.csv",
                data=SAMPLE_INPUT_PATH.read_bytes(),
                file_name="sample_input.csv",
                mime="text/csv",
                use_container_width=True,
            )


def render_input_form() -> Optional[pd.DataFrame]:
    st.subheader("1. Enter one profile")

    with st.form("prediction_form", clear_on_submit=False):
        col1, col2 = st.columns(2)

        with col1:
            age = st.slider("Age", min_value=17, max_value=90, value=35)
            workclass = st.selectbox("Workclass", WORKCLASS_OPTIONS, index=0)
            education = st.selectbox(
                "Education",
                list(EDUCATION_NUM_MAP.keys()),
                index=list(EDUCATION_NUM_MAP.keys()).index("Bachelors"),
            )
            occupation = st.selectbox("Occupation", OCCUPATION_OPTIONS, index=3)
            hours_per_week = st.slider("Hours per week", min_value=1, max_value=99, value=40)

        with col2:
            marital_status = st.selectbox("Marital status", MARITAL_STATUS_OPTIONS, index=0)
            relationship = st.selectbox("Relationship", RELATIONSHIP_OPTIONS, index=0)
            capital_gain = st.number_input("Capital gain", min_value=0, max_value=100000, value=0, step=100)
            capital_loss = st.number_input("Capital loss", min_value=0, max_value=5000, value=0, step=50)
            st.text_input("Education number", value=str(EDUCATION_NUM_MAP[education]), disabled=True)

        submitted = st.form_submit_button("Predict income", use_container_width=True)

    if not submitted:
        return None

    return build_input_dataframe(
        age=age,
        workclass=workclass,
        education=education,
        marital_status=marital_status,
        occupation=occupation,
        relationship=relationship,
        capital_gain=int(capital_gain),
        capital_loss=int(capital_loss),
        hours_per_week=hours_per_week,
    )


def render_prediction(pipeline: Any, input_data: pd.DataFrame) -> None:
    st.subheader("2. Prediction result")

    try:
        prediction, confidence, probability_by_class = get_prediction_summary(pipeline, input_data)
    except Exception as exc:  # noqa: BLE001 - Streamlit needs user-friendly failures
        st.error("Prediction failed. Please check that the saved model matches the expected input features.")
        with st.expander("Technical details"):
            st.code(str(exc))
        return

    result_col1, result_col2, result_col3 = st.columns(3)
    result_col1.metric("Predicted class", prediction)

    if confidence is not None:
        result_col2.metric("Confidence", format_percent(confidence))
        result_col3.metric("Summary", confidence_label(confidence))
    else:
        result_col2.metric("Confidence", "N/A")
        result_col3.metric("Summary", "Model has no probability output")

    if probability_by_class:
        proba_df = pd.DataFrame(
            {
                "Class": list(probability_by_class.keys()),
                "Probability": [format_percent(value) for value in probability_by_class.values()],
            }
        )
        st.dataframe(proba_df, hide_index=True, use_container_width=True)

    with st.expander("Input sent to model"):
        st.dataframe(input_data, hide_index=True, use_container_width=True)

    st.warning(
        "This result is for portfolio demonstration only. It should not be used for employment, credit, financial, or eligibility decisions."
    )


def render_metrics(metrics: Optional[Dict[str, Any]]) -> None:
    st.subheader("3. Model metrics")

    if not metrics:
        st.info("metrics.json belum tersedia atau tidak dapat dibaca. Jalankan `python train_model.py` untuk membuat ulang metrics.")
        return

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    metric_col1.metric("Baseline", format_percent(metrics.get("baseline_majority_class_accuracy")))
    metric_col2.metric("Accuracy", format_percent(metrics.get("accuracy")))
    metric_col3.metric("F1 >50K", format_percent(metrics.get("f1_score_positive_class_gt_50k")))
    metric_col4.metric("ROC-AUC >50K", format_percent(metrics.get("roc_auc_positive_class_gt_50k")))

    st.caption(
        "Baseline means always predicting the majority class. The demo model should be compared against this baseline, not against the leaked score from the old notebook."
    )

    report = metrics.get("classification_report")
    if isinstance(report, dict):
        with st.expander("Classification report"):
            rows = []
            for label in ["<=50K", ">50K", "macro avg", "weighted avg"]:
                if label in report:
                    values = report[label]
                    rows.append(
                        {
                            "label": label,
                            "precision": round(float(values.get("precision", 0)), 4),
                            "recall": round(float(values.get("recall", 0)), 4),
                            "f1-score": round(float(values.get("f1-score", 0)), 4),
                            "support": int(values.get("support", 0)),
                        }
                    )
            st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)


def render_model_notes(metadata: Optional[Dict[str, Any]]) -> None:
    st.subheader("4. Model notes")
    st.write(
        "The deployed artifact is a saved scikit-learn `.joblib` pipeline. It contains preprocessing and the trained classifier, so the same transformations are used during training and prediction."
    )

    if metadata:
        with st.expander("Features used in this public demo"):
            st.write(metadata.get("feature_columns", FEATURE_COLUMNS))
        with st.expander("Excluded columns and reason"):
            st.write(metadata.get("excluded_columns", ["Class", "cluster", "race", "sex"]))
            st.caption(metadata.get("leakage_note", "Target-derived features are excluded to avoid leakage."))
            st.caption(metadata.get("fairness_note", "Sensitive fields are excluded from the public demo form."))


def main() -> None:
    add_page_style()
    render_header()

    metrics = load_json(METRICS_PATH)
    metadata = load_json(METADATA_PATH)
    render_sidebar(metadata, metrics)

    try:
        pipeline = load_pipeline()
    except Exception as exc:  # noqa: BLE001 - show graceful Streamlit error
        st.error("Model artifact could not be loaded.")
        st.write("Please make sure `artifacts/income_prediction_pipeline.joblib` exists, or run:")
        st.code("python train_model.py")
        with st.expander("Technical details"):
            st.code(str(exc))
        st.stop()

    input_data = render_input_form()
    if input_data is not None:
        render_prediction(pipeline, input_data)

    render_metrics(metrics)
    render_model_notes(metadata)


if __name__ == "__main__":
    main()
