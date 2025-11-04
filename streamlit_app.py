import streamlit as st
import joblib
import os
from pathlib import Path

ARTIFACT = Path("artifacts") / "svm_baseline.joblib"


@st.cache_resource
def load_artifact(path: str):
    if not os.path.exists(path):
        return None
    return joblib.load(path)


def predict(model_bundle, text: str):
    if model_bundle is None:
        return None
    model = model_bundle.get("model")
    vec = model_bundle.get("vectorizer")
    X = vec.transform([text])
    try:
        pred = model.predict(X)[0]
    except Exception:
        # fallback
        pred = model.predict(X)[0]
    # obtain decision score if available
    score = None
    if hasattr(model, "decision_function"):
        try:
            score = float(model.decision_function(X)[0])
        except Exception:
            score = None
    return int(pred), score


def main():
    st.set_page_config(page_title="Spam Email Classification", layout="centered")
    st.title("Spam / Ham Classifier — Phase 1 (SVM baseline)")

    st.markdown(
        "This demo uses a pre-trained SVM baseline (sample). Enter a message and click Predict."
    )

    model_bundle = load_artifact(str(ARTIFACT))
    if model_bundle is None:
        st.warning(
            "Model artifact not found at `artifacts/svm_baseline.joblib`. Run training locally or upload the artifact to the repository."
        )

    sample_messages = [
        "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)",
        "Hey, are we still meeting for lunch today?",
        "Congratulations! You've won a $1000 gift card. Click here to claim." ,
    ]

    text = st.text_area("Enter message to classify", value=sample_messages[1], height=150)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Predict"):
            if model_bundle is None:
                st.error("No model available. Please train and place artifact at artifacts/svm_baseline.joblib")
            else:
                pred, score = predict(model_bundle, text)
                label = "SPAM" if pred == 1 else "HAM"
                st.markdown(f"### Prediction: **{label}**")
                if score is not None:
                    st.write(f"Decision function score: {score:.4f}")
    with col2:
        if st.button("Use sample message"):
            st.experimental_set_query_params()
            st.session_state["_tmp"] = sample_messages[0]
            st.experimental_rerun()

    st.write("---")
    st.markdown("#### Notes")
    st.markdown(
        "- Model: LinearSVC (SVM) baseline saved as `artifacts/svm_baseline.joblib`\n- This demo shows prediction label and decision score (no calibrated probability)."
    )


if __name__ == "__main__":
    main()
