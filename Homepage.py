import streamlit as st
st.set_page_config(
    page_title="Homepage"
)

st.title("My code memo web")
st.divider()

st.subheader("รายละเอียด",divider=True)
st.text("เว็บไซต์จัดทำขึ้นโดยมี 3 ส่วนประกอบด้วย")
st.text("- Code Memo เป็นแหล่งเก็บชุดคำสั่งเกี่ยวกับการเขียนโปรแกรมในภาษา Python แบบง่าย")
st.text("- Code Finding เป็นส่วนที่ผู้ใช้สามารถพิมพ์ข้อความเพื่อหาชุดคำสั่งแบบง่ายและสามารถคัดลอกได้")
st.text("- About Me เป็นรายละเอียดเกี่ยวกับผู้พัฒนาโปรเจกต์และแหล่งข้อมูลที่ใช้ในการพัฒนาเว็บนี้")

st.divider()
with st.bottom:
    st.caption("Kunanon Surasorn Code Memo Project")