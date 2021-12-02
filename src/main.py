from tkinter import*
import random
import time
import com.oss_project.entity.order as order
import com.oss_project.controller.main_frame_controller as main_frame_controller
#import qr_code

#엔트리 포인트 지정
if __name__ == "__main__":
    root = Tk()
    root.geometry("1600x700+0+0")
    root.title("Restaurant Management System")
    root.resizable(0,0)
    Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)

    
    #------------------TIME--------------
    localtime=time.asctime(time.localtime(time.time()))
    def clock(): # 현재 시간 표시 / 반복
        live_T = time.strftime("%H  :  %M  :  %S")
        clock_width.config(text=live_T)
        clock_width.after(200, clock) # .after(지연시간{ms}, 실행함수)

    txt_frame = Frame(root)
    txt_frame.pack(side=TOP)

    txt_width = Label(txt_frame, text="현재 시간",font =('aria' ,20, 'bold'),anchor=W)
    txt_width.pack(side=TOP)

    clock_frame = Frame(root)
    clock_frame.pack(side=TOP, pady=30)

    clock_width = Label(clock_frame, font=("Times",30,"bold"), bg="white", bd=5)
    clock_width.pack(side=TOP)
    
    f1 = Frame(root,width = 1600,relief=SUNKEN,bg="black")
    f1.pack(side=TOP)
    #-----------------INFO TOP------------
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    lblinfo = Label(Tops, font=( 'aria' ,20, 'bold' ),text=clock(),fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=0)
    lblinfo = Label(Tops, font=( 'aria' ,20, 'bold' ),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=2,column=0)
    #---------------Calculator------------------
    text_Input=StringVar()
    operator =""

    def  btnclick(numbers):
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

        list = []
        cof =float(Fries.get())
        colfries= float(Largefries.get())
        cob= float(Burger.get())
        cofi= float(Filet.get())
        cochee= float(Cheese_burger.get())
        codr= float(Drinks.get())

        costoffries = cof*25
        list.append(('costoffries', cof))
        costoflargefries = colfries*40
        list.append(('costoflargefries', colfries))
        costofburger = cob*35
        list.append(('costofburger', cob))
        costoffilet = cofi*50
        list.append(('costoffilet', cofi))
        costofcheeseburger = cochee*50
        list.append(('costofcheeseburger', cochee))
        costofdrinks = codr*35
        list.append(('costofdrinks', codr))

        costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
        PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
        Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
        Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
        Service="Rs.",str('%.2f'% Ser_Charge)
        OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
        PaidTax="Rs.",str('%.2f'% PayTax)

        Service_Charge.set(Service)
        cost.set(costofmeal)
        Tax.set(PaidTax)
        Subtotal.set(costofmeal)
        Total.set(OverAllCost)
        
        main_frame_controller.total_button_listener(randomRef, list, PaidTax)

    def qexit():
        root.destroy()

    def reset():
        rand.set("")
        Fries.set("")
        Largefries.set("")
        Burger.set("")
        Filet.set("")
        Subtotal.set("")
        Total.set("")
        Service_Charge.set("")
        Drinks.set("")
        Tax.set("")
        cost.set("")
        Cheese_burger.set("")
        main_frame_controller.reset_button_listener()

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
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=3)

        roo.mainloop()


    #---------------------------------------------------------------------------------------
    rand = StringVar()
    Fries = StringVar()
    Largefries = StringVar()
    Burger = StringVar()
    Filet = StringVar()
    Subtotal = StringVar()
    Total = StringVar()
    Service_Charge = StringVar()
    Drinks = StringVar()
    Tax = StringVar()
    cost = StringVar()
    Cheese_burger = StringVar()


    lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
    lblreference.grid(row=0,column=0)
    txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtreference.grid(row=0,column=1)

    lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10,anchor='w')
    lblfries.grid(row=1,column=0)
    txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtfries.grid(row=1,column=1)

    lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10,anchor='w')
    lblLargefries.grid(row=2,column=0)
    txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtLargefries.grid(row=2,column=1)


    lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10,anchor='w')
    lblburger.grid(row=3,column=0)
    txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtburger.grid(row=3,column=1)

    lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10,anchor='w')
    lblFilet.grid(row=4,column=0)
    txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtFilet.grid(row=4,column=1)

    lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="steel blue",bd=10,anchor='w')
    lblCheese_burger.grid(row=5,column=0)
    txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtCheese_burger.grid(row=5,column=1)

    #--------------------------------------------------------------------------------------
    lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
    lblDrinks.grid(row=0,column=2)
    txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtDrinks.grid(row=0,column=3)

    lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue",bd=10,anchor='w')
    lblcost.grid(row=1,column=2)
    txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtcost.grid(row=1,column=3)

    lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
    lblService_Charge.grid(row=2,column=2)
    txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtService_Charge.grid(row=2,column=3)

    lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
    lblTax.grid(row=3,column=2)
    txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtTax.grid(row=3,column=3)

    lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')
    lblSubtotal.grid(row=4,column=2)
    txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtSubtotal.grid(row=4,column=3)

    lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
    lblTotal.grid(row=5,column=2)
    txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtTotal.grid(row=5,column=3)

    lblTotal = Label(f1,text="---------------------",fg="white")
    lblTotal.grid(row=6,columnspan=3)
    #-----------------------------------------buttons------------------------------------------
    button_frame = Frame(root, bg="green", width=1600)
    button_frame.pack(side=BOTTOM)
    
    btnprice=Button(button_frame,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
    btnprice.pack(anchor=CENTER, side='left', padx=12)
    
    btntotal=Button(button_frame,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
    btntotal.pack(anchor=CENTER, side=LEFT, padx=12)

    btnreset=Button(button_frame,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
    btnreset.pack(anchor=CENTER, side=LEFT, padx=12)

    btnpay=Button(button_frame,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PAY", bg="powder blue", command=main_frame_controller.pay_button_listener)
    btnpay.pack(anchor=CENTER, side=LEFT, padx=12)
    
    btnmanage=Button(button_frame,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="MANAGE", bg="powder blue", command=main_frame_controller.manage_button_litener)
    btnmanage.pack(anchor=CENTER, side=LEFT, padx=12)

    btnexit=Button(button_frame,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
    btnexit.pack(anchor=CENTER, side=LEFT, padx=12)
    

    root.mainloop()
