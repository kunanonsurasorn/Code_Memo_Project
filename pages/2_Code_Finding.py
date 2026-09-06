import streamlit as st

st.set_page_config(
    page_title="Code Finding"
)

code1 = '''print("Hello Everyone")'''
code2 = '''data = input("Enter the data : ")
print(data)'''
code3 = '''data = input("Enter the data : ")
data = int(data)
if data >= 80:
    print("Great")
elif data >= 50:
    print("Pass")
else:
    print("Fail")'''
code4 = '''
def calculationTwoValues(x,y):
    z = x + y
    return z

a = int(input("Enter the first :"))
b = int(input("Enter the second :"))
c = calculationTwoValues(a,b)
print(c)'''

code5 = '''for i in range(5):
    print(i)'''

code6 = '''i = 0
while i <= 5:
    print(i)
    i = i + 1'''

st.title("My code memo web")
st.divider()

st.header("Code Finding")
st.text("เป็นส่วนที่จัดทำขึ้นมาโดยนำไอเดียจาก Rule-Based Chatbot แบบง่ายโดยผู้ใช้จะพิมพ์ข้อความเข้าไปสู่เงื่อนไขที่กำหนดโดยพิจารณาจากคำสำคัญในข้อความที่ส่งมาเพื่อให้โปรแกรมส่งผลลัพธ์กลับมาที่ผู้ใช้")

name_input =  st.text_input("กรอกชื่อของคุณก่อนเริ่มการสนทนา : ")
if st.button("Enter"):
    st.text(f"สวัสดีคุณ{name_input}ครับ ยินดีที่ได้รู้จักอย่างเป็นทางการ อยากทราบว่าคุณ{name_input}มีอะไรอยากให้ผมช่วยครับ")
conversation_input = st.chat_input("กรอกข้อความเพื่อสนทนา : ")
st.divider()
if conversation_input:
    message_text = st.chat_message("assistant")
    if ("แสดงผลข้อมูล" or "print" or "output") in conversation_input:
          message_text.write("การแสดงผลข้อมูล")
          st.code(code1,language="python")
    elif ("นำเข้าข้อมูล" or "input") in conversation_input:
          message_text.write("การนำเข้าข้อมูล")
          st.code(code2,language="python")
    elif ("เงื่อนไข" or "ifelse" or "condition") in conversation_input:
          message_text.write("การสร้างเงื่อนไข")
          st.code(code3,language="python")
    elif ("ฟังก์ชัน" or "function") in conversation_input:
          message_text.write("การสร้างฟังก์ชัน")
          st.code(code4,language="python")
    elif ("วนลูป (For)" or "forloop") in conversation_input:
          message_text.write("การสร้างวนลูป (For)")
          st.code(code5,language="python")
    elif ("วนลูป (While)" or "whileloop") in conversation_input:
          message_text.write("การสร้างวนลูป (While)")
          st.code(code6,language="python")
    else:
         message_text.write(f"คุณ{name_input}ครับ,คำถามนี้อยู่นอกเหนือจากข้อมูลที่เรามี หรือ คำถามอาจไม่เข้ากับเงื่อนไขที่กำหนดไว้")

with st.bottom:
    st.caption("Kunanon Surasorn Code Memo Project")