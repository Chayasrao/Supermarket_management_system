import mysql.connector as sqltor
from tkinter import *
from PIL import Image,ImageTk
from PIL import Image,ImageDraw,ImageFont
import random
import math
import datetime

mycon=sqltor.connect(host="localhost",user="root",passwd="",database="proj")
pid=0
q=0
cph=0
amouttobe=0
balance=0

class login:
    def __init__(self) -> None:
        self.root=Tk()
        self.loginid=StringVar()
        self.username=StringVar()
        self.password=StringVar()

    def next(self):
        self.loginid=self.loginid.get()
        self.loginid=int(self.loginid)
        self.username=self.username.get()
        self.password=self.password.get()
        curobj=mycon.cursor()
        curobj.execute("select * from logins where elid = {} and username = '{}' and pwd = '{}'".format(self.loginid,self.username,self.password))
        curobj.fetchone()
        self.count=curobj.fetchone()
        if self.count!=-1 and self.username!='admin':
            self.root.destroy()
            billing().main()
        else:
            self.root.destroy()
            dbentry().main()
    
    def main(self):
        root=self.root
        root.geometry("666x461")
        root.title("Supermarket")
        imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
        imag=imag.resize((666,461))
        img=ImageTk.PhotoImage(imag)
        Label(root,image=img).place(x=-2,y=0)
        canvas_width=440
        canvas_height=225
        Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
        self.username.set("")
        self.password.set("")
        self.loginid.set("")
        Label(root,text="Login id:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=120)
        Entry(root,textvariable=self.loginid,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=123)
        Label(root,text="Username:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=170)
        Entry(root,textvariable=self.username,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=173)
        Label(root,text="Password:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=220)
        Entry(root,textvariable=self.password,font="calibri 18 bold",show="*",relief=SUNKEN).place(x=300,y=223)
        Button(root,text="Login",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.next).place(x=490,y=276)
        root.mainloop()

class dbentry:
    def __init__(self) -> None:
        self.root=Tk()
        self.productid=StringVar()
        self.qty=StringVar()
        self.pname=StringVar()
        self.ptype=StringVar()
        self.cp=StringVar()
        self.mrp=StringVar()

    def enter(self):
        global pid,q
        self.pname=self.pname.get()
        self.ptype=self.ptype.get()
        self.cp=self.cp.get()
        self.cp=int(self.cp)
        self.mrp=self.mrp.get()
        self.mrp=int(self.mrp)
        curobj=mycon.cursor()
        curobj.execute("insert into product values({},'{}','{}',{},{},{})".format(pid,self.pname,self.ptype,q,self.cp,self.mrp))
        mycon.commit()
        self.root.destroy()
        dbentry().main()

    def next(self):
        global pid,q
        self.productid=self.productid.get()
        self.productid=int(self.productid)
        self.qty=self.qty.get()
        self.qty=int(self.qty)
        pid=self.productid
        q=self.qty
        curobj=mycon.cursor()
        curobj.execute("select * from product where pid={}".format(self.productid))
        self.count=curobj.fetchone()
        if not self.count:
            self.root.destroy()
            dbentry().enternext()
        else:
            curobj=mycon.cursor()
            curobj.execute("update product set qty=qty+{} where pid={}".format(self.qty,self.productid))
            mycon.commit()
            self.root.destroy()
            dbentry().main()

    def enternext(self):
        root=self.root
        root.geometry("666x461")
        root.title("Supermarket")
        imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
        imag=imag.resize((666,461))
        img=ImageTk.PhotoImage(imag)
        Label(root,image=img).place(x=-2,y=0)
        canvas_width=440
        canvas_height=250
        Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
        self.ptype.set("")
        self.pname.set("")
        self.productid.set("")
        self.qty.set("")
        self.cp.set("")
        self.mrp.set("")
        Label(root,text="Product name:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=120)
        Entry(root,textvariable=self.pname,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=123)
        Label(root,text="Product Type:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=170)
        Entry(root,textvariable=self.ptype,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=173)
        Label(root,text="Costprice:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=220)
        Entry(root,textvariable=self.cp,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=223)
        Label(root,text="MRP:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=270)
        Entry(root,textvariable=self.mrp,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=273)
        Button(root,text="Done",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.enter).place(x=490,y=300)
        root.mainloop()

    def main(self):
        root=self.root
        root.geometry("666x461")
        root.title("Supermarket")
        imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
        imag=imag.resize((666,461))
        img=ImageTk.PhotoImage(imag)
        Label(root,image=img).place(x=-2,y=0)
        canvas_width=440
        canvas_height=225
        Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
        Label(root,text="Productid:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=120)
        Entry(root,textvariable=self.productid,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=123)
        Label(root,text="Quantity:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=170)
        Entry(root,textvariable=self.qty,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=173)
        Button(root,text="Next",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.next).place(x=498,y=223)
        Button(root,text="Finish",font="calibri 16",bg="red",fg="white",relief=RAISED,command=root.destroy).place(x=489,y=273)
        root.mainloop()

class billing:
    def __init__(self) -> None:
        self.root=Tk()
        self.cphno=StringVar()
        self.cname=StringVar()
        self.cgen=StringVar()
        self.productid=StringVar()
        self.qty=StringVar()
        self.at=StringVar()

    def finalbill(self):
        global amouttobe,balance
        root=self.root
        root.geometry("450x1200")
        root.title("Bill")
        curobj=mycon.cursor()
        curobj.execute("select * from bill")
        ans=curobj.fetchall()
        Label(root,text="A2Z",font="calibri 12 bold",fg="black").place(x=205,y=0)
        Label(root,text="Supermarket",font="calibri 12 bold",fg="black").place(x=175,y=20)
        Label(root,text="High Tension Double Road",font="calibri 12 bold",fg="black").place(x=130,y=40)
        Label(root,text="Vijaynagar Mysore-17",font="calibri 12 bold",fg="black").place(x=145,y=60)
        Label(root,text="Bill No:",font="calibri 12 bold",fg="black").place(x=20,y=90)
        Label(root,text=random.randrange(1000000000,9999999999),font="calibri 12 bold",fg="black").place(x=75,y=90)
        Label(root,text="FSSAI Lic No:",font="calibri 12 bold",fg="black").place(x=20,y=110)
        Label(root,text=624895135748625,font="calibri 12 bold",fg="black").place(x=112,y=110)
        cur=datetime.datetime.now()
        day,mon,yea=cur.day,cur.month,cur.year
        hr,min,sec=cur.hour,cur.minute,cur.second
        date=str(day)+"/"+str(mon)+"/"+str(yea) 
        time=str(hr)+":"+str(min)+":"+str(sec)
        Label(root,text="Date:",font="calibri 12 bold",fg="black").place(x=340,y=90)
        Label(root,text=date,font="calibri 12 bold",fg="black").place(x=380,y=90)
        Label(root,text="Time:",font="calibri 12 bold",fg="black").place(x=340,y=110)
        Label(root,text=time,font="calibri 12 bold",fg="black").place(x=380,y=110)
        Label(root,text="ITEM",font="calibri 12 bold",fg="black").place(x=20,y=145)
        Label(root,text="MRP",font="calibri 12 bold",fg="black").place(x=138,y=145)
        Label(root,text="QTY",font="calibri 12 bold",fg="black").place(x=250,y=145)
        Label(root,text="TOTAL",font="calibri 12 bold",fg="black").place(x=365,y=145)
        Label(root,text="-"*105,font="calibri 10 bold",fg="black").place(x=10,y=165)
        y1=185
        for data in ans:
            x1=20
            for i in range(4):
                Label(root,text=data[i],fg="black",font="calibri 12").place(x=x1,y=y1)
                x1+=115
            y1+=21
        curobj=mycon.cursor()
        curobj.execute("select sum(mrpxqty) from bill")
        ans=curobj.fetchall()
        Label(root,text="-"*105,font="calibri 10 bold",fg="black").place(x=10,y=y1)
        Label(root,text="Total amount :",font="calibri 12 bold",fg="black").place(x=20,y=y1+20)
        Label(root,text=ans[0],font="calibri 12 bold",fg="black").place(x=365,y=y1+20)
        Label(root,text="-"*105,font="calibri 10 bold",fg="black").place(x=10,y=y1+40)
        Label(root,text="Tax :",font="calibri 12 bold",fg="black").place(x=20,y=y1+55)
        Label(root,text="CGST :",font="calibri 12 bold",fg="black").place(x=20,y=y1+77)
        Label(root,text="2.5%",font="calibri 12 bold",fg="black").place(x=365,y=y1+77)
        Label(root,text="SGST :",font="calibri 12 bold",fg="black").place(x=20,y=y1+97)
        Label(root,text="2.5%",font="calibri 12 bold",fg="black").place(x=365,y=y1+97)
        Label(root,text="-"*105,font="calibri 10 bold",fg="black").place(x=10,y=y1+117)
        y1=y1+117
        ans=ans[0]
        ans=ans[0]
        res=ans+float(ans)*0.05
        Label(root,text="Amount to be paid :",font="calibri 12 bold",fg="black").place(x=20,y=y1+20)
        Label(root,text=res,font="calibri 12 bold",fg="black").place(x=365,y=y1+20)
        Label(root,text="Amount paid :",font="calibri 12 bold",fg="black").place(x=20,y=y1+40)
        Label(root,text=amouttobe,font="calibri 12 bold",fg="black").place(x=365,y=y1+40)
        Label(root,text="Change due :",font="calibri 12 bold",fg="black").place(x=20,y=y1+60)
        Label(root,text=math.trunc(amouttobe-res),font="calibri 12 bold",fg="black").place(x=365,y=y1+60)
        Label(root,text="-"*105,font="calibri 10 bold",fg="black").place(x=10,y=y1+81)
        y1=y1+81
        Label(root,text="Customer Care Ph No : 1800-102-7385",font="calibri 12 bold",fg="black").place(x=90,y=y1+20)
        Label(root,text="No Cash Refunds",font="calibri 12 bold",fg="black").place(x=155,y=y1+40)
        Label(root,text="Terms and Conditions Apply",font="calibri 12 bold",fg="black").place(x=115,y=y1+60)
        Label(root,text="*Thank You For Shopping*",font="calibri 12 bold",fg="black").place(x=120,y=y1+80)
        img=Image.open("bill image.jpg")
        d=ImageDraw.Draw(img)
        d.text((220,1),"A2Z",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((198,17),"Supermarket",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((165,37),"High Tension Double Road",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((178,57),"Vijaynagar Mysore-17",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((20,85),"Bill No:",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        bilno=random.randrange(1000000000,9999999999)
        bilno=str(bilno)
        d.text((60,85),bilno,font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((20,107),"FSSAI Lic No:",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        fsno=624895135748625
        d.text((87,107),str(fsno),font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))   
        date=str(day)+"/"+str(mon)+"/"+str(yea) 
        time=str(hr)+":"+str(min)+":"+str(sec)
        d.text((345,85),"Date :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((380,85),date,font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((345,107),"Time :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((380,107),time,font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((24,140),"ITEM",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((138,140),"MRP",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((250,140),"QTY",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((365,140),"TOTAL",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((10,160),"-"*140,font=ImageFont.truetype('calibrib.ttf',10),fill=(0,0,0))
        curobj=mycon.cursor()
        curobj.execute("select * from bill")
        ans=curobj.fetchall()
        y1=185
        for data in ans:
            x1=22
            for i in range(4):
                d.text((x1,y1),str(data[i]),font=ImageFont.truetype('calibri.ttf',12),fill=(0,0,0))
                x1+=115
            y1+=21
        curobj=mycon.cursor()
        curobj.execute("select sum(mrpxqty) from bill")
        ans=curobj.fetchall()
        rans=ans[0]
        rans=rans[0]
        d.text((10,y1),"-"*140,font=ImageFont.truetype('calibrib.ttf',10),fill=(0,0,0))
        d.text((20,y1+20),"Total Amount :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((367,y1+20),str(rans),font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((10,y1+40),"-"*140,font=ImageFont.truetype('calibrib.ttf',10),fill=(0,0,0))
        d.text((20,y1+55),"Tax :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((20,y1+77),"CGST :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((367,y1+77),"2.5%",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((20,y1+97),"SGST :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((367,y1+97),"2.5%",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((10,y1+117),"-"*140,font=ImageFont.truetype('calibrib.ttf',10),fill=(0,0,0))
        y1+=117
        ans=ans[0]
        ans=ans[0]
        res=ans+float(ans)*0.05
        d.text((20,y1+20),"Amount to be paid :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((367,y1+20),str(res),font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((20,y1+40),"Amount paid :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((367,y1+40),str(amouttobe),font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((20,y1+60),"Change due :",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((367,y1+60),str(math.trunc(amouttobe-res)),font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((10,y1+81),"-"*140,font=ImageFont.truetype('calibrib.ttf',10),fill=(0,0,0))
        y1+=81
        d.text((135,y1+20),"Customer Care Ph No : 1800-102-7385",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((184,y1+40),"No Cash Refunds",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((157,y1+60),"Terms and Condition Apply",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        d.text((158,y1+80),"*Thank You For Shopping*",font=ImageFont.truetype('calibrib.ttf',12),fill=(0,0,0))
        img.save("bill report.jpeg")
        root.mainloop()
 
    def lastbillcard(self):
        global amouttobe
        amouttobe=self.amt
        self.root.destroy()
        billing().finalbill()

    def lastbillcash(self):
        global amouttobe
        self.at=self.at.get()
        amouttobe=int(self.at)
        self.root.destroy()
        billing().finalbill()

    def amount(self):
        root=self.root
        root.geometry("666x461")
        root.title("Supermarket")
        imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
        imag=imag.resize((666,461))
        img=ImageTk.PhotoImage(imag)
        Label(root,image=img).place(x=-2,y=0)
        canvas_width=440
        canvas_height=225
        self.at.set("")
        Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
        Label(root,text="Enter the amount the customer has paid:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=120)
        Entry(root,textvariable=self.at,font="calibri 18 bold",relief=SUNKEN).place(x=215,y=175)
        Button(root,text="Done",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.lastbillcash).place(x=475,y=235)
        root.mainloop()

    def bill(self):
        root=self.root
        root.geometry("666x461")
        root.title("Supermarket")
        imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
        imag=imag.resize((666,461))
        img=ImageTk.PhotoImage(imag)
        Label(root,image=img).place(x=-2,y=0)
        canvas_width=440
        canvas_height=225
        Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
        curobj=mycon.cursor()
        curobj.execute("select sum(mrpxqty) from bill")
        self.count=curobj.fetchone()
        self.amt=self.count[0]
        self.amt+=float(self.amt)*0.05
        Label(root,text="Your total bill is :",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=210,y=150)
        Label(root,text=self.amt,fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=385,y=150)
        Button(root,text="UPI",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.lastbillcard).place(x=235,y=220)
        Button(root,text="Card",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.lastbillcard).place(x=305,y=220)
        Button(root,text="Cash",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.amount).place(x=380,y=220)
        root.mainloop()

    def function(self):
        self.root.destroy()
        billing().putitems()

    def nextitems(self):
        self.productid=self.productid.get()
        self.productid=int(self.productid)
        self.qty=self.qty.get()
        self.qty=int(self.qty)
        curobj=mycon.cursor()
        curobj.execute("select * from product where pid={}".format(self.productid))
        self.count=curobj.fetchone()
        if not self.count:
            root=self.root
            root.geometry("666x461")
            root.title("Supermarket")
            imag1=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
            imag1=imag1.resize((666,461))
            img1=ImageTk.PhotoImage(imag1)
            Label(root,image=img1).place(x=-2,y=0)
            canvas_width=440
            canvas_height=225
            Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
            Label(root,text="You have entered the wrong product id",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=145,y=150)
            Button(root,text="Next",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.function).place(x=315,y=220)
            root.mainloop()
        else:
            curobj=mycon.cursor()
            curobj.execute("update product set qty=qty-{} where pid={}".format(self.qty,self.productid))
            mycon.commit()
            curobj=mycon.cursor()
            curobj.execute("insert into bill values('{}',{},{},{})".format(self.count[1],self.count[5],self.qty,self.count[5]*self.qty))
            mycon.commit()
            self.root.destroy()
            billing().putitems()

    def putitems(self):
        root=self.root
        root.geometry("666x461")
        root.title("Supermarket")
        imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
        imag=imag.resize((666,461))
        img=ImageTk.PhotoImage(imag)
        Label(root,image=img).place(x=-2,y=0)
        canvas_width=440
        canvas_height=225
        self.productid.set("")
        self.qty.set("")
        Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
        Label(root,text="Productid:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=120)
        Entry(root,textvariable=self.productid,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=123)
        Label(root,text="Quantity:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=170)
        Entry(root,textvariable=self.qty,font="calibri 18 bold",relief=SUNKEN).place(x=300,y=173)
        Button(root,text="Next",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.nextitems).place(x=498,y=223)
        Button(root,text="Finish",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.bill).place(x=489,y=273)
        root.mainloop()

    def enter(self):
        global cph
        self.cname=self.cname.get()
        self.cgen=self.cgen.get()
        curobj=mycon.cursor()
        curobj.execute("insert into customer values('{}',{},'{}')".format(self.cname,cph,self.cgen))
        mycon.commit() 
        self.root.destroy()
        billing().putitems()

    def enterdet(self):
        root=self.root
        root.geometry("666x461")
        root.title("Supermarket")
        imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
        imag=imag.resize((666,461))
        img=ImageTk.PhotoImage(imag)
        Label(root,image=img).place(x=-2,y=0)
        canvas_width=440
        canvas_height=225
        Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
        self.cname.set("")
        self.cgen.set("")
        Label(root,text="Cust name:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=120)
        Entry(root,textvariable=self.cname,font="calibri 18 bold",relief=SUNKEN).place(x=290,y=123)
        Label(root,text="Cust gender:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=130,y=180)
        Entry(root,textvariable=self.cgen,font="calibri 18 bold",relief=SUNKEN).place(x=290,y=183)
        Button(root,text="Done",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.enter).place(x=470,y=250)
        root.mainloop()

    def next(self):
        global cph
        self.cphno=self.cphno.get()
        self.cphno=int(self.cphno)
        cph=self.cphno
        curobj=mycon.cursor()
        curobj.execute("select * from customer where cphno={}".format(self.cphno))
        self.count=curobj.fetchone()
        if not self.count:
            self.root.destroy()
            billing().enterdet()
        else:
            self.root.destroy()
            billing().putitems()
        
    def main(self):
        root=self.root
        root.geometry("666x461")
        root.title("Supermarket")
        imag=Image.open(r"C:\Users\Chaya S Rao\Python\Python311\pgms\proj\image2.jpg")
        imag=imag.resize((666,461))
        img=ImageTk.PhotoImage(imag)
        Label(root,image=img).place(x=-2,y=0)
        canvas_width=440
        canvas_height=225
        curobj=mycon.cursor()
        curobj.execute("truncate table bill")
        mycon.commit()
        self.cphno.set("")
        Canvas(root,width=canvas_width,height=canvas_height,bg="white").place(x=120,y=105)
        Label(root,text="Enter the Customer Phone Number:",fg="black",bg="white",font="calibri 18 bold",borderwidth=5).place(x=150,y=120)
        Entry(root,textvariable=self.cphno,font="calibri 18 bold",relief=SUNKEN).place(x=215,y=175)
        Button(root,text="Next",font="calibri 16",bg="red",fg="white",relief=RAISED,command=self.next).place(x=483,y=213)
        root.mainloop()

app=login()
app.main()