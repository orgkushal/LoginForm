from tkinter import *
from functools import partial

def register(username,password,rollNum,sem):
    info=username.get()
    pas=password.get()
    info+=pas
    info+='.txt'
    file=open(info,'w')
    file.write('Username:'+username.get()+'\n'+'Password:'+password.get()+'\n'+'Roll Number:'+rollNum.get()+'\n'+'Semester:'+sem.get())
    file.close()
    success()

def success():
    ok.geometry('150x100')
    ok.title('Success')
    Label(ok,text="Registration is Successful",font=('Times New Roman bold',10)).pack()
    login=Button(ok,text='OK',font=('Times New Roman bold',10),command=dest).pack()
    reg.destroy()

def dest():
    ok.destroy()
    
reg=Tk()
ok=Tk()
reg.geometry('500x300')
reg.title('Login Form')

ti=Label(reg,text='USER SIGNUP',font=('Times New Roman bold',20)).place(x=180,y=10)

usernameLabel=Label(reg,text="User Name",font=('Times New Roman bold',10)).place(x=100,y=45)
username=StringVar()
usernameEntry=Entry(reg,textvariable=username).place(x=200,y=45)

passwordLabel=Label(reg,text="Password",font=('Times New Roman bold',10)).place(x=100,y=80)
password=StringVar()
passwordEntry=Entry(reg,textvariable=password).place(x=200,y=80)

rollLabel=Label(reg,text="Roll Number",font=('Times New Roman bold',10)).place(x=100,y=115)
rollNum=StringVar()
rollEntry=Entry(reg,textvariable=rollNum).place(x=200,y=115)

semLabel=Label(reg,text="Semester",font=('Times New Roman bold',10)).place(x=100,y=150)
sem=StringVar()
semEntry=Entry(reg,textvariable=sem).place(x=200,y=150)

register=partial(register,username,password,rollNum,sem)

registerButton=Button(reg,text='Register',font=('Times New Roman bold',10),command=register).place(x=130,y=215)
reg.mainloop()
