
import streamlit as st
import random
import string

# إعداد الصفحة
st.set_page_config(page_title="Alphabet AI Simulation", page_icon="🔤")
st.title("📘 Alphabet Wizard Smart Book - AI Simulation")
st.write("🧠 هذه محاكاة تفاعلية لتدريب الطفل على نطق الحروف باستخدام الذكاء الاصطناعي.")

# توليد الحرف فقط مرة واحدة في بداية الجلسة
if 'target' not in st.session_state:
    st.session_state.target = random.choice(string.ascii_uppercase)

# عرض الحرف
st.markdown(f"### 🔤 نطق الحرف المطلوب: **{st.session_state.target}**")

# إدخال المستخدم
user_input = st.text_input("📣 أدخل الحرف الذي نطقته:")

# التحقق من الإجابة
if user_input:
    if user_input.strip().upper() == st.session_state.target:
        st.success("✅ صحيح! أحسنت!")
    else:
        st.error("❌ غير صحيح. حاول مرة أخرى.")

# زر لإعادة توليد حرف جديد
if st.button("🔄 توليد حرف جديد"):
    st.session_state.target = random.choice(string.ascii_uppercase)
    st.experimental_rerun()
