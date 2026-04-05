import streamlit as st
import requests

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="AI Interview Prep", layout="centered")

st.title("🎯 AI Interview Preparation System (LLM Powered)")

# -----------------------------
# HUGGING FACE API
# -----------------------------
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
HEADERS = {
    "Authorization": f"Bearer {st.secrets['HF_API_KEY']}"
}

def query_llm(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    return response.json()[0]["generated_text"]

# -----------------------------
# INPUTS
# -----------------------------
name = st.text_input("Enter your name")

company = st.selectbox("Company", ["Google", "Amazon", "Meta"])
domain = st.selectbox("Domain", ["YouTube", "E-commerce", "Social Media"])
role = st.selectbox("Role", ["SDE", "ML Engineer"])
level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])

# -----------------------------
# GENERATE QUESTION
# -----------------------------
if st.button("🎯 Generate Question"):

    prompt = f"""
    Generate an interview question for {role} at {company} working on {domain}.
    Level: {level}.
    Also provide answer and explanation.
    """

    output = query_llm(prompt)

    st.session_state["generated"] = output

# -----------------------------
# DISPLAY QUESTION
# -----------------------------
if "generated" in st.session_state:

    st.subheader("📌 Question & Answer")
    st.write(st.session_state["generated"])

    user_answer = st.text_area("✍️ Your Answer")

    if st.button("✅ Evaluate Answer"):

        eval_prompt = f"""
        Compare the correct answer with this user answer:

        User Answer: {user_answer}

        Give feedback in 2 lines.
        """

        feedback = query_llm(eval_prompt)

        st.subheader("📊 Feedback")
        st.write(feedback)

# -----------------------------
# ADAPTIVE LEARNING
# -----------------------------
st.header("📈 Self Evaluation")

score = st.slider("Rate yourself", 1, 5)

if score <= 2:
    st.error("Focus on basics")
elif score <= 4:
    st.warning("Improve concepts")
else:
    st.success("Try advanced problems")