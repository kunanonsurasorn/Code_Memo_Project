import streamlit as st

st.set_page_config(
    page_title="About Me"
)

st.title("My code memo web")
st.divider()

st.header("About Me")
st.subheader("คุณานนต์ สุรศร",divider=True)
st.text("เว็บไซต์นี้จัดทำขึ้นเพื่อฝึกทักษะการใช้ Library ชื่อ streamlit สำหรับการพัฒนา Web App เพื่อหาโอกาสทำงานในสายไอที, เป็นแหล่งเก็บข้อมูลในการเขียนโปรแกรมภาษา Python แบบง่าย และ แบ่งปันความรู้ในการเขียนโปรแกรมเพื่อเป็นประโยชน์ต่อบุคคลอื่น")
st.text("GitHub : https://github.com/kunanonsurasorn")
st.link_button("GitHub","https://github.com/kunanonsurasorn")
st.text("YouTube : https://www.youtube.com/@khemksc")
st.link_button("YouTube","https://www.youtube.com/@khemksc")
st.subheader("แหล่งข้อมูลเกี่ยวกับ Streamlit",divider=True)
st.text("Streamlit Documentation Website : https://docs.streamlit.io/")
st.link_button("Streamlit Documentation","https://docs.streamlit.io/")

st.divider()
with st.bottom:
    st.caption("Kunanon Surasorn Code Memo Project")