import streamlit as st
import random

st.set_page_config(page_title="GenAI Interview Prep", layout="centered")

st.title("🎯 GenAI-Based Personalized Interview Prep System")

# -----------------------------
# INPUTS
# -----------------------------
name = st.text_input("Enter your name")

company = st.selectbox(
    "Select Company",
    ["Google", "Amazon", "Meta", "Apple", "Netflix"]
)

domain = st.selectbox(
    "Select Domain",
    ["YouTube", "E-commerce", "Social Media", "Streaming"]
)

role = st.selectbox(
    "Select Role",
    ["SDE", "ML Engineer"]
)

level = st.selectbox(
    "Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# -----------------------------
# SMART GENERATOR (LIGHTWEIGHT)
# -----------------------------
def generate_content(company, domain, role, level):

    if role == "SDE":
        if level == "Beginner":
            return f"""
**Question:** Find the largest element in an array.

**Solution:** Traverse the array and track max value.

**Explanation:** Tests basic looping and comparisons.

**Feedback:** Focus on fundamentals of arrays.
"""
        elif level == "Intermediate":
            return f"""
**Question:** Solve Two Sum problem using hashmap.

**Solution:** Store elements in dictionary for O(n) lookup.

**Explanation:** Optimized approach using hashing.

**Feedback:** Improve time complexity thinking.
"""
        else:
            return f"""
**Question:** Design a scalable {domain} system at {company}.

**Solution:** Use load balancing, CDN, distributed storage.

**Explanation:** Tests system design & scalability.

**Feedback:** Focus on architecture and scaling.
"""

    else:  # ML Engineer
        if level == "Beginner":
            return f"""
**Question:** What is supervised learning?

**Solution:** Learning from labeled data.

**Explanation:** Basic ML concept.

**Feedback:** Revise ML basics.
"""
        elif level == "Intermediate":
            return f"""
**Question:** How does {domain} recommendation system work?

**Solution:** Uses collaborative + content-based filtering.

**Explanation:** Combines user behavior and features.

**Feedback:** Improve ML model understanding.
"""
        else:
            return f"""
**Question:** Design a {domain} recommendation system.

**Solution:** Use embeddings, deep learning, ranking models.

**Explanation:** Large-scale ML system design.

**Feedback:** Focus on production ML systems.
"""

# -----------------------------
# BUTTON
# -----------------------------
if st.button("🚀 Generate Questions"):

    if name == "":
        st.warning("Please enter your name")
    else:
        st.success(f"Hello {name}! Here is your personalized prep 👇")

        output = generate_content(company, domain, role, level)
        st.markdown(output)

# -----------------------------
# ADAPTIVE LEARNING
# -----------------------------
st.header("📈 Self Evaluation")

score = st.slider("Rate your understanding", 1, 5)

if score <= 2:
    st.error("Focus on basics.")
elif score <= 4:
    st.warning("Work on optimization.")
else:
    st.success("Try advanced problems.")

# -----------------------------
# FEEDBACK
# -----------------------------
st.header("💬 Feedback")

feedback = st.text_area("What did you find difficult?")

if st.button("Submit Feedback"):
    st.success("Feedback recorded!")