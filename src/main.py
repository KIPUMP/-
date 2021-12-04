from tkinter import*
import time
from tkinter import Tk
import com.oss_project.controller.main_frame_controller as main_frame_controller

#엔트리포인트 지정
if __name__=="__main__":
   #프레임 생성
   root = Tk()
   root.geometry("1600x700+0+0")
   root.title("Restaurant Management System")
   root.resizable(0,0)
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
         
   #--------------------------------------------menus--------------------------------------------
   menus = []
   rand = StringVar()


   Fries = StringVar()
   menus.append(Fries)
   Largefries = StringVar()
   menus.append(Largefries)
   Burger = StringVar()
   menus.append(Burger)
   Filet = StringVar()
   menus.append(Filet)
   Service_Charge = StringVar()
   menus.append(Service_Charge)
   Drinks = StringVar()
   menus.append(Drinks)
   Cheese_burger = StringVar()
   menus.append(Cheese_burger)

   Tax = StringVar()
   menus.append(Tax)


   Total = StringVar()

   #--------------------------------------------labels--------------------------------------------
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
      
   #--------------------------------------------buttons--------------------------------------------
   btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=lambda: main_frame_controller.total_button_listener(rand, menus, Total))
   btnTotal.grid(row=7, column=1)

   btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=lambda: main_frame_controller.reset_button_listener(rand, menus, Total))
   btnreset.grid(row=7, column=2)

   btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=lambda: main_frame_controller.exit_button_listener(root))
   btnexit.grid(row=8, column=4)

   btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="MENU", bg="powder blue",command=main_frame_controller.menu_button_listener)
   btnprice.grid(row=8, column=1)

   btnpay=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PAY", bg="powder blue",command=main_frame_controller.pay_button_listener)
   btnpay.grid(row=7, column=4)

   btncalender=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="CALENDER", bg="powder blue",command=main_frame_controller.calender_button_listener)
   btncalender.grid(row=8, column=3)

   btncoupon=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="COUPON", bg="powder blue",command=main_frame_controller.coupon_button_listener)
   btncoupon.grid(row=7, column=3)

   btnmanage=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="MANAGE", bg="powder blue",command=main_frame_controller.manage_button_litener)
   btnmanage.grid(row=8, column=2)

   root.mainloop()