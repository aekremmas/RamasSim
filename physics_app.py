import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# دالة معالجة اللغة العربية
def ar_text(text):
    return get_display(reshape(text))

st.set_page_config(page_title="مختبر الأستاذ رماس", layout="wide")

# القائمة الجانبية للتنقل
st.sidebar.title("🏢 " + ar_text("مختبر الفيزياء الافتراضي"))
page = st.sidebar.radio(ar_text("اختر المحطة:"), 
                         [ar_text("وحدة الميكانيك: دافعة أرخميدس"), 
                          ar_text("وحدة الكهرباء: راسم الاهتزاز")])

# --- محاكاة دافعة أرخميدس الواقعية ---
if page == ar_text("وحدة الميكانيك: دافعة أرخميدس"):
    st.header(ar_text("تجربة غمر أجسام صلبة في سوائل مختلفة"))
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader(ar_text("التحكم في التجربة"))
        liquid = st.selectbox(ar_text("نوع السائل المستعمل"), ["ماء نقي", "زيت الزيتون", "ماء مالح جداً"])
        v_sub = st.slider(ar_text("مقدار الغمر (حجم الجزء المغمور cm³)"), 0, 1000, 500)
        
        # قيم فيزيائية واقعية
        rho = {"ماء نقي": 1000, "زيت الزيتون": 800, "ماء مالح جداً": 1200}[liquid]
        g = 9.81
        p_real = 8.0 # ثقل الجسم في الهواء (8 نيوتن)
        fa = round(rho * (v_sub/1000000) * g, 2)
        p_app = round(p_real - fa, 2)
        
        # عرض النتائج كأجهزة رقمية
        st.metric(label=ar_text("قراءة الربيعة (الثقل الظاهري)"), value=f"{p_app} N")
        st.metric(label=ar_text("شدة الدافعة المحسوبة"), value=f"{fa} N")

    with col2:
        fig, ax = plt.subplots(figsize=(7, 9))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        
        # 1. رسم الحامل المخبري (الواقعية)
        ax.plot([2, 8], [13, 13], color='#444444', lw=8) # القضيب العلوي
        ax.plot([2, 2], [0, 13], color='#444444', lw=5) # العمود الجانبي
        ax.plot([1, 4], [0, 0], color='#444444', lw=10) # القاعدة
        
        # 2. رسم الربيعة (Dynamomètre)
        ax.add_patch(plt.Rectangle((4.2, 8), 1.6, 4, color='#E0E0E0', ec='black', lw=2)) # الهيكل
        ax.text(4.5, 11.2, "NEWTON", fontsize=8, fontweight='bold')
        # تدريجات الربيعة
        for i in range(11):
            y_pos = 8.2 + i*0.35
            ax.plot([4.2, 4.4], [y_pos, y_pos], color='black', lw=1)
            ax.text(4.45, y_pos-0.1, str(10-i), fontsize=7)
        
        # 3. النابض والمؤشر (يتحرك مع القوة)
        spring_length = 1.5 + (p_app * 0.2) # النابض يتمدد حسب الثقل
        ax.plot([5, 5], [12, 12-spring_length], color='blue', lw=2, ls='--') # تمثيل النابض
        ax.plot([4.2, 5.8], [12-spring_length, 12-spring_length], color='red', lw=3) # المؤشر الأحمر
        
        # 4. رسم البيشر والسائل (يرتفع منسوب الماء مع الغمر)
        water_level = 1.5 + (v_sub/1000 * 1.5)
        ax.add_patch(plt.Rectangle((3.5, 0.5), 3, 5, color='#D1E9FF', alpha=0.6)) # السائل
        ax.add_patch(plt.Rectangle((3.5, 0.5), 3, water_level, color='#0077BE', alpha=0.4)) # الجزء الممتلئ
        ax.plot([3.5, 3.5, 6.5, 6.5], [5.5, 0.5, 0.5, 5.5], color='black', lw=3) # حواف الزجاج
        
        # 5. الجسم المغمور (يتصل بالنابض)
        ax.add_patch(plt.Rectangle((4.4, 12-spring_length-1.5), 1.2, 1.5, color='#CD7F32', ec='black'))
        ax.plot([5, 5], [12-spring_length, 12-spring_length-0.1], color='black', lw=2) # السلك

        # 6. تمثيل الأشعة (Fa و P)
        center_y = 12-spring_length-0.75
        ax.arrow(5, center_y, 0, -1.5, head_width=0.2, color='red', lw=2) # الثقل P
        ax.arrow(5, center_y, 0, fa*0.5, head_width=0.2, color='green', lw=2) # الدافعة Fa
        
        ax.axis('off')
        st.pyplot(fig)

# --- محاكاة راسم الاهتزاز ---
elif page == ar_text("وحدة الكهرباء: راسم الاهتزاز"):
    st.header(ar_text("معاينة توتر كهربائي جيبي"))
    
    f = st.sidebar.slider(ar_text("التواتر (Hz)"), 1, 50, 10)
    v_div = st.sidebar.select_slider(ar_text("الحساسية العمودية (V/div)"), [1, 2, 5])
    
    t = np.linspace(0, 0.1, 1000)
    y = 5 * np.sin(2 * np.pi * f * t) # سعة 5 فولط
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, y/v_div, color='#39FF14', lw=3) # اللون الفسفوري
    ax.set_facecolor('#001100')
    ax.grid(color='#004400', linestyle='-', lw=1) # شبكة راسم الاهتزاز
    ax.set_ylim(-5, 5)
    ax.set_title(ar_text("شاشة راسم الاهتزاز المهبطي"), color='black')
    st.pyplot(fig)
