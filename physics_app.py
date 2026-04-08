import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# إعداد عنوان المنصة
st.title("منصة رماس للمحاكاة الفيزيائية 2026")
st.subheader("محاكاة حركة قذيفة - دراسة المسار")

# القائمة الجانبية للتحكم (Inputs)
st.sidebar.header("إعدادات التجربة")
v0 = st.sidebar.slider("السرعة الابتدائية (m/s)", 1, 50, 20)
angle = st.sidebar.slider("زاوية القذف (درجة)", 0, 90, 45)
g = 9.81  # الجاذبية الأرضية

# الحسابات الفيزيائية
theta = np.radians(angle)
t_flight = 2 * v0 * np.sin(theta) / g
t = np.linspace(0, t_flight, num=100)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# رسم المنحنى البياني
fig, ax = plt.subplots()
ax.plot(x, y, color='red', linewidth=2)
ax.set_xlabel("المسافة الأفقية (m)")
ax.set_ylabel("الارتفاع (m)")
ax.set_title(f"مسار القذيفة بزاوية {angle} درجة")
ax.grid(True)

# عرض الرسم البياني في المنصة
st.pyplot(fig)

# النتائج الرقمية
st.write(f"**أقصى مدى أفقي:** {max(x):.2f} متر")
st.write(f"**أقصى ارتفاع:** {max(y):.2f} متر")