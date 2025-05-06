
import streamlit as st
import random
import string

st.set_page_config(page_title="AI Simulation - Alphabet Wizard", page_icon="🔤")
st.title("📘 محاكاة الذكاء الاصطناعي - Alphabet Wizard Smart Book")

st.write("🧠 هذا النموذج يحاكي طريقة تفاعل الذكاء الاصطناعي مع نطق الحروف من قبل الطفل.")

letters = list(string.ascii_uppercase)  # A to Z
target = random.choice(letters)

st.markdown(f"### 🔤 نرجو من الطفل نطق الحرف التالي: **{target}**")

user_input = st.text_input("📣 أدخل الحرف الذي نطقته (للمحاكاة):")

if user_input:
    if user_input.strip().upper() == target:
        st.success("✅ أحسنت! نطق صحيح.")
    else:
        st.error("❌ حاول مرة أخرى.")
