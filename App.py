import streamlit as st

st.set_page_config(page_title="الحاسبة الذكية", page_icon="🧮")

st.title("🧮 الحاسبة الذكية للمعدلات")
st.write("أداة احترافية للمدارس والأساتذة")

st.sidebar.header("⚙️ تخصيص")
school_name = st.sidebar.text_input("اسم مؤسستكم", "مدرسة النجاح")
color = st.sidebar.color_picker("اللون الرئيسي", "#0066cc")

st.markdown(f"<h2 style='color: {color};'>{school_name}</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    sub1 = st.text_input("المادة 1", "الرياضيات")
    grade1 = st.number_input(f"نقطة {sub1}", 0.0, 20.0, 15.0)
    w1 = st.slider(f"وزن {sub1} %", 0, 100, 50)

with col2:
    sub2 = st.text_input("المادة 2", "الفيزياء") 
    grade2 = st.number_input(f"نقطة {sub2}", 0.0, 20.0, 14.0)
    w2 = st.slider(f"وزن {sub2} %", 0, 100, 30)

sub3 = st.text_input("المادة 3", "اللغة")
grade3 = st.number_input(f"نقطة {sub3}", 0.0, 20.0, 16.0)
w3 = 100 - w1 - w2
st.info(f"وزن {sub3}: {w3}%")

if st.button("احسب المعدل", type="primary"):
    if w1 + w2 + w3 == 100:
        avg = (grade1*w1 + grade2*w2 + grade3*w3) / 100
        st.success(f"المعدل النهائي: {avg:.2f}/20")
        st.balloons()
        st.warning("💡 تريد نسخة خاصة بمدرستكم؟ abdullah.dev.pro@gmail.com")
    else:
        st.error("مجموع الأوزان يجب أن يكون 100%")

st.caption("Developed by AtlasCode")
