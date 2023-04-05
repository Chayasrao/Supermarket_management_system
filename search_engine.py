from tkinter import *
from PIL import Image,ImageTk
import mysql.connector as sqltor

mycon=sqltor.connect(host="localhost",user="root",passwd="",database="proj")

def notfound():
    root=Tk()
    root.geometry("700x500")
    root.title("Supermarket")
    imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\search image.jpg")
    imag=imag.resize((702,500))
    img=ImageTk.PhotoImage(imag)
    Label(root,image=img).place(x=-3,y=0)
    Canvas(root,width=470,height=300,bg="white").place(x=120,y=105)
    Label(root,text="Oops!",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=130)
    Label(root,text="Sorry we don't have what you are looking",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=170)
    Label(root,text="for, we will make sure that we include",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=210)
    Label(root,text="this item in our supermarket by the next",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=250)
    Label(root,text="time you come.",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=290)
    Label(root,text="Have a good day",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=330)
    Button(root,text="Okay",font="calibri 15",bg="blue",fg="white",relief=RAISED,command=root.destroy).place(x=520,y=360)
    root.mainloop()

def found():
    root=Tk()
    root.geometry("700x500")
    root.title("Supermarket")
    imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\search image.jpg")
    imag=imag.resize((702,500))
    img=ImageTk.PhotoImage(imag)
    Label(root,image=img).place(x=-3,y=0)
    Canvas(root,width=470,height=260,bg="white").place(x=120,y=105)
    Label(root,text="Bingo!",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=130)
    Label(root,text="We have the product you are looking for.",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=170)
    Label(root,text="Please do come in.",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=210)
    Button(root,text="Okay",font="calibri 15",bg="blue",fg="white",relief=RAISED,command=root.destroy).place(x=508,y=310)
    root.mainloop()

def next():
    global name,root
    name=name.get()
    curobj=mycon.cursor()
    curobj.execute("select * from product where soundex(pname)=soundex('{}')".format(name))
    count=curobj.fetchone()
    if not count:
        root.destroy()
        notfound()
    else:
        root.destroy()
        found()


root=Tk()
root.geometry("700x500")
root.title("Supermarket")
imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\search image.jpg")
imag=imag.resize((702,500))
img=ImageTk.PhotoImage(imag)
Label(root,image=img).place(x=-3,y=0)
canvas_width=470
canvas_height=260
name=StringVar()
name.set("")
Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
Label(root,text="Welcome",fg="red",bg="white",font="calibri 18 bold",borderwidth=5).place(x=300,y=110)
Label(root,text="We are very much eager to know what you",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=140,y=150)
Label(root,text="are looking for!",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=278,y=190)
Label(root,text="Please enter the name of the product:",fg="blue",bg="white",font="calibri 18 bold",borderwidth=5).place(x=160,y=230)
Entry(root,textvariable=name,font="calibri 15 bold").place(x=250,y=270)
Button(root,text="Search",font="calibri 15",bg="blue",fg="white",relief=RAISED,command=next).place(x=508,y=310)

root.mainloop()