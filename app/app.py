import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Intelligent Student Performance Prediction System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Intelligent Student Performance Prediction System")

st.write(
    "AI-based system for predicting student academic performance "
    "and providing personalized learning recommendations."
)

st.header("📋 Student Information")

name = st.text_input("Student Name")

col1, col2 = st.columns(2)

with col1:
    studytime = st.number_input(
        "Study Time",
        min_value=1,
        max_value=4,
        value=2
    )

    absences = st.number_input(
        "Absences",
        min_value=0,
        max_value=100,
        value=5
    )

with col2:
    failures = st.number_input(
        "Previous Failures",
        min_value=0,
        max_value=4,
        value=0
    )

    internet = st.selectbox(
        "Internet Access",
        ["Yes", "No"]
    )

if st.button("Predict Performance"):
    score = 50

    score += studytime * 8
    score -= absences * 0.5
    score -= failures * 8

    score = max(0, min(100, score))

    st.subheader("📊 Prediction Result")

    st.metric("Predicted Performance", f"{score:.1f}%")

    if score >= 75:
        st.success("🌟 Good performance! Keep up the excellent work.")
    elif score >= 50:
        st.warning("👍 Average performance. More practice is recommended.")
    else:
        st.error("⚠️ Performance needs improvement.")

    st.subheader("💡 Recommendation")

    if studytime < 3:
        st.write("📚 Increase your daily study time.")

    if absences > 10:
        st.write("🏫 Try to reduce class absences.")

    if failures > 0:
        st.write("📝 Focus on subjects where you previously had difficulties.")

    if internet == "Yes":
        st.write("💻 Use online learning resources for additional practice.")