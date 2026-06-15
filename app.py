import streamlit as st

# Page Config
st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align: center;
    color: #4F46E5;
    font-size: 40px;
    font-weight: bold;
}
.result-box {
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(135deg,#667eea,#764ba2);
    color: white;
    text-align: center;
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🎓 Grade Calculator</p>', unsafe_allow_html=True)

st.write("### Enter Marks (Out of 100)")

col1, col2 = st.columns(2)

with col1:
    sub1 = st.number_input("Subject 1", 0, 100)
    sub2 = st.number_input("Subject 2", 0, 100)
    sub3 = st.number_input("Subject 3", 0, 100)

with col2:
    sub4 = st.number_input("Subject 4", 0, 100)
    sub5 = st.number_input("Subject 5", 0, 100)

if st.button("Calculate Grade 🚀"):

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
        remark = "Excellent 🌟"
    elif percentage >= 80:
        grade = "A"
        remark = "Very Good 👍"
    elif percentage >= 70:
        grade = "B"
        remark = "Good 😊"
    elif percentage >= 60:
        grade = "C"
        remark = "Average 🙂"
    elif percentage >= 40:
        grade = "D"
        remark = "Pass ✔️"
    else:
        grade = "F"
        remark = "Fail ❌"

    st.markdown(f"""
    <div class="result-box">
        <h2>Total Marks: {total}/500</h2>
        <h2>Percentage: {percentage:.2f}%</h2>
        <h1>Grade: {grade}</h1>
        <h3>{remark}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.progress(int(percentage))