from tkinter import *
from tkinter import ttk
from tkinter import messagebox



GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูลสำหรับการเช็คสต็อคของคลังสินค้า')
GUI.geometry('800x600')

L1 = Label(GUI,text='เช็คสต็อกคลังสินค้าของโรงงาน' ,font=('Angsana New',30),fg='Blue')
L1.place(x=5,y=5)

def Button1():
    text = 'สินค้าคงเหลือเท่ากับ 30 เครื่อง'
    messagebox.showinfo('จำนวนคงเหลือของสินค้า',text)
    
def Button2():
    text = 'สินค้าคงเหลือเท่ากับ 1 เครื่อง กรุณาทำการสต็อกสินค้าเพิ่ม เพื่อการขาย'
    messagebox.showwarning('จำนวนคงเหลือของสินค้า',text)

def Button3():
    text = 'สินค้าคงเหลือเท่ากับ 0 เครื่อง'
    messagebox.showerror('จำนวนคงเหลือของสินค้า',text)

FB1=LabelFrame(GUI,text='โรงงานผลิตเครื่องซักผ้า')
FB1.place(x=80,y=80)
B1 = ttk.Button(FB1,text='กดปุ่มเพื่อเช็คจำนวนสินค้าคงเหลือ',command=Button1)
B1.pack(ipadx=20,ipady=20,padx=30,pady=3)
    
FB2=LabelFrame(GUI,text='โรงงานผลิตเครื่องปรับอากาศ')
FB2.place(x=80,y=180)
B2 = ttk.Button(FB2,text='กดปุ่มเพื่อเช็คเช็คจำนวนสินค้าคงเหลือ',command=Button2)
B2.pack(ipadx=20,ipady=20,padx=30,pady=3)
    
FB3=LabelFrame(GUI,text='โรงงานผลิต TV')
FB3.place(x=80,y=280)
B3 = ttk.Button(FB3,text='กดปุ่มเพื่อเช็คเช็คจำนวนสินค้าคงเหลือ',command=Button3)
B3.pack(ipadx=20,ipady=20,padx=30,pady=3)

GUI.mainloop()























#def Button2():
#    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300บาท'
#    messagebox.showinfo('เงินในบัญชี',text)
#    
#FB1=LabelFrame(GUI,text='Money')
#FB1.place(x=100,y=100)
#B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
#B2.pack(ipadx=20,ipady=20,padx=30,pady=3)






