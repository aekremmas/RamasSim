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

# --- محاكاة دافعة أرخميدس (عبر رابط PhET العالمي) ---
if page == ar_text("وحدة الميكانيك: دافعة أرخميدس"):
    st.header(ar_text("محاكاة دافعة أرخميدس والطفو (تجربة تفاعلية)"))
    
    st.info(ar_text("ملاحظة: يمكنك سحب الأجسام بيدك ووضعها في الماء، وتغيير السوائل من القائمة داخل المحاكاة."))
    
    # تضمين رابط المحاكاة العالمية (PhET) مباشرة في صفحتك
    phet_url = "https://phet.colorado.edu/sims/html/buoyancy/latest/buoyancy_all.html?locale=ar"
    st.components.v1.iframe(phet_url, height=700, scrolling=True)

# --- محاكاة راسم الاهتزاز (التي أعجبتك) ---
elif page == ar_text("وحدة الكهرباء: راسم الاهتزاز"):
    st.header(ar_text("معاينة توتر كهربائي جيبي"))
    
    f = st.sidebar.slider(ar_text("التواتر (Hz)"), 1, 50, 10)
    
    t = np.linspace(0, 0.1, 1000)
    y = 5 * np.sin(2 * np.pi * f * t)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, y, color='#39FF14', lw=3) # اللون الفسفوري
    ax.set_facecolor('#001100')
    ax.grid(color='#004400', linestyle='-', lw=1)
    ax.set_ylim(-6, 6)
    ax.set_title(ar_text("شاشة راسم الاهتزاز المهبطي"), color='black')
    st.pyplot(fig)
