from tkinter import*
import random
import time
import math
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkcalendar import Calendar
from tkinter import Tk

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")
root.resizable(True,True)
Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=BOTTOM)
#------------------TIME--------------
def clock(): # 현재 시간 표시 / 반복
   live_T = time.strftime('%c')
   clock_width.config(text=live_T)
   clock_width.after(200, clock) # .after(지연시간{ms}, 실행함수)

txt_frame = Frame(root)
txt_frame.pack()

txt_width = Label(txt_frame, text="현재 시간",font =('aria' ,20, 'bold'), bg="white",anchor=W)
txt_width.pack()

clock_frame = Frame(root)
clock_frame.pack()

clock_width = Label(clock_frame, font=("Times",30,"bold"), bg="white", bd=5)
clock_width.pack()
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, 'bold' ),text=clock(),fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)
#---------------Calculate------------------------------------------------------------------
text_Input=StringVar()
operator =""

def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*2500
    costoflargefries = colfries*4000
    costofburger = cob*3500
    costoffilet = cofi*5000
    costofcheeseburger = cochee*5000
    costofdrinks = codr*3500

    costofmeal = str(math.ceil(0.1% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))),'won'
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.1)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks) 
 
    
    OverAllCost= str( PayTax + Totalcost ),'won'
    PaidTax=str('%.1f'% PayTax),'won'

    Tax.set(PaidTax)

    Total.set(OverAllCost)

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")

    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")

    Cheese_burger.set("")

def error():
    if float(Fries.get()) < 0 or float(Burger.get())< 0  or  float(Filet.get())< 0  or float(Cheese_burger.get())< 0  or float(Drinks.get()) < 0 :
        messagebox.showinfo('오류','잘못된 입력입니다 정확한 수량을 입력해주세요')




#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="주문번호",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="감자튀김",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="런치 팩",fg="steel blue",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="햄버거",fg="steel blue",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="피자",fg="steel blue",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="스파게티",fg="steel blue",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="콜라",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax(VAT)",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=1,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=1,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=2,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=10,bg="powder blue" ,justify='right')
txtTotal.grid(row=2,column=3)

lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=3,columnspan=3)
#-----------------------------------------buttons------------------------------------------


btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=lambda:[Ref(),error()])
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=3)



def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="감자튀김", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2500", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="런치팩", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="4000", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="햄버거", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3500", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="피자", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5000", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="스파게티", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3000", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="콜라", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3500", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()



btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="MENU", bg="powder blue",command=price)
btnprice.grid(row=8, column=1)

def pay():
    window = Tk()
    window.title("결제")
    window.geometry("300x220+100+100")

    btn1 = Button(window,text = "KAKAO_QR_PAY",fg = "white", bg = "blue" ,padx=20,pady=8, bd=10, command = qrcode)
    btn1.pack(side = LEFT)
    btn2 = Button(window,text = "CASH",fg = "white",bg = "blue" ,padx=20,pady=8, bd=10, command = cash)
    btn2.pack(side= RIGHT)
        
def qrcode():
            w = Tk()
            w.title("kakao_pay")
            w.geometry("400x400")


            btncancel = Button(w,text = "QR 결제 취소",fg = "white", bg = "blue" ,padx=20,pady=8, bd=10, command = qrcode)
            btncancel.pack(side=BOTTOM)
            photo = PhotoImage(file= "kakaopay.gif",master=w)
            pLabel = Label(w, image = photo)
            pLabel.pack()
            w.mainloop()

def cash():

    roo = Tk()
    roo.title("현금결제")
    roo.geometry("600x220+0+0")

    lblTotal = Label(roo, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
    lblTotal.pack()
    txtTotal = Entry(roo,font=('ariel' ,16,'bold'), textvariable= 0.1*(float(Fries.get()) + float(Largefries.get()) + float(Burger.get()) + float(Filet.get()) + float(Cheese_burger.get()) +float(Drinks.get())) , bd=6,insertwidth=4 , bg="powder blue" ,justify='right')
    txtTotal.pack()
    btn1 = Button(roo,font=( 'aria' ,16, 'bold' ),text="결제",fg="steel blue",bd=10,anchor='w')
    btn1.pack()
    btn2 = Button(roo,font=( 'aria' ,16, 'bold' ),text="결제 취소",fg="steel blue",bd=10,anchor='w')
    btn2.pack()
    roo.mainloop()
    

btnpay=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PAY", bg="powder blue",command=pay)
btnpay.grid(row=8, column=2)
#-----------------------------------------------------------calender----------------------------------------------------------
class MyCalendar(Calendar):
    def _next_month(self):
        Calendar._next_month(self)
        self.event_generate('<<CalendarMonthChanged>>')
    def _prev_month(self):
        Calendar._prev_month(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _next_year(self):
        Calendar._next_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _prev_year(self):
        Calendar._prev_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def get_displayed_month_year(self):
        return self._date.month, self._date.year
        
    def on_change_month(event):
        Calendar.calevent_remove('all')
        year, month = Calendar.get_displayed_month_year()
        print(year, month)

def clickcalender():
    w = Tk()
    w.title("calendar")
    cal = MyCalendar(w)
    cal.pack()
    cal.bind('<<CalendarMonthChanged>>')
    w.mainloop()
    

btncalender=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="CALENDER", bg="powder blue",command=clickcalender)
btncalender.grid(row=8, column=3)

def coupon():
    a = 0.1*(float(Fries.get()) + float(Largefries.get()) + float(Burger.get()) + float(Filet.get()) + float(Cheese_burger.get()) +float(Drinks.get()))
    b = input()
    if b == 'coupon3000':
        a -= 3000
        messagebox.showinfo('resturant','3000원 할인!')
        return a
    if b == 'coupon5000':
        a -= 5000
        messagebox.showinfo('resturant','5000원 할인!')
        return a

def insertcoupon():
    w = Tk()
    w.title("할인 쿠폰 입력")
    w.geometry("600x220+0+0")

    lblCoupon = Label(w, font=( 'aria' ,16, 'bold' ),text="쿠폰입력", fg="steel blue",bd=10,anchor='w')
    lblCoupon.pack()
    txtCoupon = Entry(w, font=('ariel' ,16,'bold'), textvariable= coupon, bd=6 , insertwidth=4 , bg="powder blue" ,justify='right')
    txtCoupon.pack()
    btncoupon= Button(w,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="입력", bg="powder blue",command=coupon)
    btncoupon.pack()
    w.mainloop()

btncoupon=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="COUPON", bg="powder blue",command=insertcoupon)
btncoupon.grid(row=8, column=4)


root.mainloop()
