import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# 1. دالة معالجة اللغة العربية للرسوم البيانية
def ar_text(text):
    return get_display(reshape(text))

# 2. إعدادات الصفحة
st.set_page_config(page_title="منصة الأستاذ رماس التعليمية", layout="wide")

# 3. نظام التنقل في القائمة الجانبية
st.sidebar.title("📑 " + ar_text("المختبر الافتراضي"))
st.sidebar.info(ar_text("متوسطة الشهيد فراح عيسى - سعيدة"))
page = st.sidebar.radio(ar_text("اختر المحاكاة:"), 
                         [ar_text("الرئيسية"), 
                          ar_text("دافعة أرخميدس"), 
                          ar_text("حركة القذيفة"), 
                          ar_text("دراسة التواتر")])

# --- 1. الصفحة الرئيسية ---
if page == ar_text("الرئيسية"):
    st.title("🔬 " + ar_text("منصة الأستاذ رماس للعلوم الفيزيائية"))
    st.markdown(f"### {ar_text('مرحباً بكم تلاميذنا الأعزاء')}")
    st.write(ar_text("هذه المنصة صُممت لتسهيل فهم الظواهر الفيزيائية عبر التجريب الرقمي. اختر تجربة من القائمة الجانبية للبدء."))
    st.image("https://img.freepik.com/free-vector/science-concept-illustration_114360-1205.jpg", width=500)

# --- 2. دافعة أرخميدس (تصميم مرئي يعتمد على ملفك PDF) ---
elif page == ar_text("دافعة أرخميدس"):
    st.header(ar_text("محاكاة قياس دافعة أرخميدس (الربيعة والإناء)"))
    
    col_input, col_canvas = st.columns([1, 2])
    
    with col_input:
        st.subheader(ar_text("إعدادات التجربة"))
        liquid = st.selectbox(ar_text("نوع السائل (الوثيقة 08)"), ["ماء نقي", "ماء مالح", "زيت"])
        v_obj_cm3 = st.slider(ar_text("حجم الجسم المغمور (cm³)"), 100, 800, 400)
        m_obj_g = st.slider(ar_text("كتلة الجسم (g)"), 200, 1500, 800)
        
        # الحسابات الفيزيائية
        rho_map = {"ماء نقي": 1000, "ماء مالح": 1100, "زيت": 800}
        rho_l = rho_map[liquid]
        g = 9.81
        v_l_m3 = v_obj_cm3 / 1000000 
        p_real = round((m_obj_g / 1000) * g, 2)
        fa = round(rho_l * v_l_m3 * g, 2)
        p_app = round(p_real - fa, 2)

    with col_canvas:
        # رسم الأجهزة (الربيعة والبيشر)
        fig, ax = plt.subplots(figsize=(5, 7))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.2)
        
        # رسم البيشر والسائل
        ax.add_patch(plt.Rectangle((0.2, 0.1), 0.6, 0.5, color='skyblue', alpha=0.4)) 
        ax.plot([0.2, 0.2, 0.8, 0.8], [0.7, 0.1, 0.1, 0.7], color='black', lw=3) 
        
        # رسم الربيعة (Dynamomètre)
        ax.add_patch(plt.Rectangle((0.45, 0.85), 0.1, 0.25, color='lightgray', ec='black'))
        ax.plot([0.5, 0.5], [0.65, 0.85], color='black', lw=2) # خيط التعليق
        
        # رسم الجسم المغمور
        ax.add_patch(plt.Rectangle((0.4, 0.45), 0.2, 0.2, color='orange', ec='black'))
        
        # قراءة الربيعة وتسميات القوى
        ax.text(0.57, 0.95, f"{p_app} N", color='red', fontsize=14, fontweight='bold')
        ax.arrow(0.5, 0.55, 0, -0.2, head_width=0.03, color='red') # شعاع الثقل P
        ax.arrow(0.5, 0.55, 0, 0.2, head_width=0.03, color='green') # شعاع الدافعة Fa
        
        ax.text(0.53, 0.35, "P", color='red', fontsize=12)
        ax.text(0.53, 0.75, "Fa", color='green', fontsize=12)
        
        ax.axis('off')
        st.pyplot(fig)
    
    st.success(f"💡 {ar_text('الاستنتاج:')} {ar_text('الثقل الحقيقي')} = {p_real}N | {ar_text('الدافعة')} = {fa}N | {ar_text('الثقل الظاهري')} = {p_app}N")

# --- 3. حركة القذيفة ---
elif page == ar_text("حركة القذيفة"):
    st.header(ar_text("دراسة حركة قذيفة في حقل الجاذبية"))
    v0 = st.sidebar.slider(ar_text("السرعة v0 (m/s)"), 5, 50, 25)
    angle = st.sidebar.slider(ar_text("الزاوية α (درجة)"), 0, 90, 45)
    
    t_flight = 2 * v0 * np.sin(np.radians(angle)) / 9.81
    t = np.linspace(0, t_flight, 100)
    x = v0 * np.cos(np.radians(angle)) * t
    y = v0 * np.sin(np.radians(angle)) * t - 0.5 * 9.81 * t**2
    
    fig, ax = plt.subplots()
    ax.plot(x, y, lw=3, color='darkblue')
    ax.set_xlabel(ar_text("المدى (متر)"))
    ax.set_ylabel(ar_text("الارتفاع (متر)"))
    ax.grid(True, ls='--')
    st.pyplot(fig)

# --- 4. دراسة التواتر ---
elif page == ar_text("دراسة التواتر"):
    st.header(ar_text("راسم الاهتزاز المهبطي - دراسة التواتر"))
    f = st.sidebar.slider(ar_text("التواتر f (Hz)"), 1, 20, 5)
    t = np.linspace(0, 0.5, 1000)
    y = np.sin(2 * np.pi * f * t)
    
    fig, ax = plt.subplots()
    ax.plot(t, y, color='lime', lw=2)
    ax.set_facecolor('black') # محاكاة شاشة راسم الاهتزاز
    ax.set_xlabel(ar_text("الزمن (ثانية)"))
    ax.grid(color='gray', ls=':')
    st.pyplot(fig)
    st.info(f"{ar_text('الدور T = ')} {1/f:.3f} s")
