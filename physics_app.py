import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# 1. دالة معالجة اللغة العربية (أساسية للرسوم)
def ar_text(text):
    return get_display(reshape(text))

# 2. إعدادات الصفحة وتنظيم الملاحة
st.set_page_config(page_title="منصة الأستاذ رماس للفيزياء", layout="wide")

st.sidebar.title("🗂️ " + ar_text("قائمة المحاكاة"))
page = st.sidebar.radio(ar_text("اختر التجربة:"), 
                         [ar_text("الرئيسية"), 
                          ar_text("حركة القذيفة"), 
                          ar_text("دراسة التواتر"), 
                          ar_text("دافعة أرخميدس")])

# --- صفحة الترحيب ---
if page == ar_text("الرئيسية"):
    st.title(ar_text("مرحباً بك في منصة الأستاذ رماس التعليمية"))
    st.write(ar_text("هذه المنصة مخصصة لتلاميذ المتوسط لتبسيط مفاهيم الفيزياء والكيمياء عبر المحاكاة التفاعلية."))
    st.info(ar_text("اختر تجربة من القائمة الجانبية للبدء."))

# --- محاكاة القذيفة ---
elif page == ar_text("حركة القذيفة"):
    st.title(ar_text("محاكاة حركة قذيفة"))
    v0 = st.sidebar.slider(ar_text("السرعة الابتدائية"), 1, 50, 20)
    angle = st.sidebar.slider(ar_text("الزاوية"), 0, 90, 45)
    # (هنا نضع كود الرسم الخاص بالقذيفة الذي جربناه سابقاً)
    st.success(ar_text("تم تشغيل محاكاة القذيفة بنجاح"))

# --- محاكاة التواتر ---
elif page == ar_text("دراسة التواتر"):
    st.title(ar_text("دراسة التواتر Fréquence"))
    f = st.sidebar.slider(ar_text("التواتر (Hz)"), 1, 10, 2)
    # (هنا نضع كود الرسم الخاص بالموجة الجيبية)

# --- محاكاة دافعة أرخميدس (بناءً على ملفك) ---
elif page == ar_text("دافعة أرخميدس"):
    st.title(ar_text("دافعة أرخميدس - السنة 4 متوسط"))
    liquid = st.sidebar.selectbox(ar_text("نوع السائل"), ["ماء", "زيت", "كحول"])
    v_obj = st.sidebar.slider(ar_text("الحجم (cm³)"), 100, 1000, 500)
    # (هنا نضع كود دافعة أرخميدس المطور الأخير)
    st.info(ar_text("تمت المحاكاة بناءً على قوانين التوازن"))
