import streamlit as st

st.set_page_config(
    page_title="Code Memo"
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

st.header("Code Memo")

st.subheader("การแสดงผลข้อมูล",divider=True)
st.code(code1,language="python")

st.subheader("การนำเข้าข้อมูล",divider=True)
st.code(code2,language="python")
st.text("เมื่อมีการใช้ input() ชนิดข้อมูลที่ออกมาเป็น string เสมอ")

st.subheader("การสร้างเงื่อนไข",divider=True)
st.code(code3,language="python")
st.text("เมื่อเข้าเงื่อนไขใดเช่น ข้อมูลเข้าเงื่อนไข if จะแสดงผลลัพธ์ใน if ข้อมูลเข้าเงื่อนไข elif จะแสดงผลลัพธ์ใน elif หากไม่เข้าเงื่อนไขที่กล่าวมา จะแสดงผลลัพธ์ใน else")

st.subheader("การสร้างฟังก์ชัน",divider=True)
st.code(code4,language="python")
st.text("เมื่อมีการสร้างฟังก์ชันก็ต้องมีการเรียกใช้ฟังก์ชัน")

st.subheader("การสร้างวนลูป (For)",divider=True)
st.code(code5,language="python")
st.text("ถึงแม้กำหนดให้ range(5) แต่ผลลัพธ์สุดท้ายของลูปนี้คือ 4 เพราะมันเริ่มจาก 0 1 2 3 และ 4 เป็นจำนวนตัวเลข 5 ตัว")

st.subheader("การสร้างวนลูป (While)",divider=True)
st.code(code6,language="python")
st.text("ผลลัพธ์จากลูปของ While คือ 0 1 2 3 4 5 เพราะกำหนดเงื่อนไข i <= 5 จึงจะออกจากลูปได้")

st.divider()
with st.bottom:
    st.caption("Kunanon Surasorn Code Memo Project")