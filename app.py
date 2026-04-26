import streamlit as st
from pipeline import run_pipeline

st.set_page_config(page_title="Hallucination Detector", layout="centered")

st.title("🧠 LLM Hallucination Detector")
st.markdown("---")

st.markdown("""
This system detects hallucinations by:
- Retrieving relevant knowledge
- Generating context-aware answers
- Comparing semantic similarity
""")

question = st.text_input("Enter your question:")

if st.button("Analyze"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        result = run_pipeline(question)

        st.subheader("🧠 Answer")
        st.write(result["answer"])

        st.subheader("📚 Retrieved Context")
        for ref in result["references"]:
            st.write(f"- {ref}")

        st.subheader("📊 Similarity Score")
        st.write(f"{result['score']:.4f}")

        st.subheader("📈 Confidence")
        st.metric("Reliability", result["confidence"])

        st.progress(min(max(result['score'], 0), 1))

        if result["is_hallucination"]:
            st.error("⚠️ Hallucination Detected")
        else:
            st.success("✅ Likely Factual")