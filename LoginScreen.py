from tkinter import *
from functools import partial
import os

def validate(username,password):
    info=username.get()
    pas=password.get()
    info+=pas
    info+='.txt'
    if(os.path.exists(info)):
        with open(info) as f:
            line=f.read()
            print(line)
            user.destroy()
    else:
        valid()


def valid():
    ok.geometry('250x100')
    ok.title('UnSuccessful')
    Label(ok,text="Username or Password  Invalid",font=('Times New Roman bold',10)).pack()
    login=Button(ok,text='OK',font=('Times New Roman bold',10),command=dest).pack()


def dest():
    ok.destroy()

def sign():
    os.system('register.py')

user=Tk()
user.geometry('500x200')
user.title('Login Form')

ti=Label(user,text='USER LOGIN',font=('Times New Roman bold',20)).place(x=180,y=10)

usernameLabel=Label(user,text="User Name",font=('Times New Roman bold',10)).place(x=100,y=45)
username=StringVar()
usernameEntry=Entry(user,textvariable=username).place(x=200,y=45)

passwordLabel=Label(user,text="Password",font=('Times New Roman bold',10)).place(x=100,y=80)
password=StringVar()
passwordEntry=Entry(user,textvariable=password,show='*').place(x=200,y=80)

validate=partial(validate,username,password)

ok=Tk()
loginButton=Button(user,text='Login',font=('Times New Roman bold',10),command=validate).place(x=130,y=125)
signUpButton=Button(user,text='SignUp',font=('Times New Roman bold',10),command=sign).place(x=250,y=125)
user.mainloop()
