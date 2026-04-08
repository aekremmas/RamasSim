import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from arabic_reshaper import reshape
from bidi.algorithm import get_display

def ar_text(text):
    return get_display(reshape(text))

st.set_page_config(page_title="مختبر الأستاذ رماس", layout="wide")

st.sidebar.title("🏢 " + ar_text("مختبر الفيزياء الافتراضي"))
page = st.sidebar.radio(ar_text("اختر المحطة:"), [ar_text("دافعة أرخميدس"), ar_text("راسم الاهتزاز")])

if page == ar_text("دافعة أرخميدس"):
    st.header(ar_text("تجربة غمر الأجسام وقياس الدافعة"))
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader(ar_text("التحكم"))
        liquid = st.selectbox(ar_text("نوع السائل"), ["ماء نقي", "زيت", "ماء مالح"])
        v_sub = st.slider(ar_text("مقدار الغمر (cm³)"), 0, 1000, 500)
        
        rho = {"ماء نقي": 1000, "زيت": 800, "ماء مالح": 1200}[liquid]
        g = 9.81
        p_real = 8.0 
        fa = round(rho * (v_sub/1000000) * g, 2)
        p_app = round(p_real - fa, 2)
        
        st.metric(label=ar_text("قراءة الربيعة (P')"), value=f"{p_app} N")
        st.metric(label=ar_text("شدة الدافعة (Fa)"), value=f"{fa} N")

    with col2:
        fig, ax = plt.subplots(figsize=(7, 9))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        
        # 1. الحامل المعدني
        ax.plot([2, 8], [13, 13], color='#444444', lw=8) 
        ax.plot([2, 2], [0, 13], color='#444444', lw=5) 
        
        # 2. هيكل الربيعة (ثابت في الأعلى)
        ax.add_patch(plt.Rectangle((4.2, 9), 1.6, 3.5, color='#E0E0E0', ec='black', lw=2))
        ax.text(4.5, 12, "NEWTON", fontsize=8, fontweight='bold')
        
        # 3. حساب حركة النابض والمؤشر (المؤشر يتحرك داخل الهيكل)
        # كلما زادت الدافعة (نقص الثقل الظاهري) يرتفع المؤشر للأعلى
        pointer_y = 9.2 + (p_app * 0.3) 
        ax.plot([4.2, 5.8], [pointer_y, pointer_y], color='red', lw=3) # المؤشر الأحمر
        
        # 4. السلك المتدلي من الربيعة إلى الجسم
        # السلك يبدأ من مكان المؤشر وينزل لأسفل
        ax.plot([5, 5], [pointer_y, pointer_y - 4], color='black', lw=1.5) 
        
        # 5. الجسم المغمور (متموضع الآن تماماً تحت الربيعة وفي منطقة السائل)
        obj_y_top = pointer_y - 4
        ax.add_patch(plt.Rectangle((4.2, obj_y_top - 2), 1.6, 2, color='#CD7F32', ec='black', lw=2))
        
        # 6. البيشر والسائل
        ax.add_patch(plt.Rectangle((3, 0.5), 4, 5, color='#D1E9FF', alpha=0.3)) # البيشر
        # منسوب السائل يرتفع قليلاً مع الغمر
        water_level = 1.0 + (v_sub/1000 * 1.0)
        ax.add_patch(plt.Rectangle((3, 0.5), 4, 3.5 + water_level, color='#0077BE', alpha=0.4))
        ax.plot([3, 3, 7, 7], [5.5, 0.5, 0.5, 5.5], color='black', lw=3) 

        # 7. تمثيل الأشعة (تخرج من مركز الجسم)
        center_y = obj_y_top - 1
        ax.arrow(5, center_y, 0, -1.5, head_width=0.2, color='red', lw=2) # الثقل
        ax.arrow(5, center_y, 0, fa*0.4, head_width=0.2, color='green', lw=2) # الدافعة
        
        ax.axis('off')
        st.pyplot(fig)

elif page == ar_text("راسم الاهتزاز"):
    # (كود راسم الاهتزاز السابق الذي أعجبك يبقى كما هو)
    st.header(ar_text("راسم الاهتزاز المهبطي"))
    f = st.sidebar.slider(ar_text("التواتر"), 1, 50, 10)
    t = np.linspace(0, 0.1, 1000)
    y = np.sin(2 * np.pi * f * t)
    fig, ax = plt.subplots()
    ax.plot(t, y, color='#39FF14')
    ax.set_facecolor('black')
    st.pyplot(fig)
