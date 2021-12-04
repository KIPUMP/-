from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
import database.data as data

#coupon 입력 화면
def open_coupon_view():
    if data.OrderInfo.total_order_id == None:
         messagebox.showerror('오류', '할인할 항목이 없습니다.')
    else:
        w = Tk()
        w.title("할인 쿠폰 입력")
        w.geometry("600x220+0+0")

        lblCoupon = Label(w, font=( 'aria' ,16, 'bold' ),text="쿠폰입력", fg="steel blue",bd=10,anchor='w')
        lblCoupon.pack()
        txtCoupon = Entry(w, font=('ariel' ,16,'bold'), textvariable= coupon, bd=6 , insertwidth=4 , bg="powder blue" ,justify='right')
        txtCoupon.pack()
        btncoupon= Button(w,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="입력", bg="powder blue",command=lambda: coupon(txtCoupon, w))
        btncoupon.pack()
        w.mainloop()

#입력된 쿠폰 처리 
def coupon(txtCoupon, root_view):
    b = txtCoupon.get()
    if b == 'coupon3000':
        if data.OrderInfo.total_sum >= 3000:
            data.OrderInfo.total_ordered_product_list.append(("할인쿠폰", 1, -3000))
            data.OrderInfo.total_sum-=3000
            messagebox.showinfo('resturant','3000원 할인!')
        else:
            data.OrderInfo.total_ordered_product_list.append(("할인쿠폰", 1, -data.OrderInfo.total_sum))
            messagebox.showinfo('resturant',str(data.OrderInfo.total_sum) + '원 할인!')
            data.OrderInfo.total_sum=0
        root_view.destroy()
                
    elif b == 'coupon5000':
        if data.OrderInfo.total_sum >= 5000:
            data.OrderInfo.total_ordered_product_list.append(("할인쿠폰", 1, -5000))
            data.OrderInfo.total_sum-=5000
            messagebox.showinfo('resturant','5000원 할인!')
        else:
            data.OrderInfo.total_ordered_product_list.append(("할인쿠폰", 1, -data.OrderInfo.total_sum))
            messagebox.showinfo('resturant',str(data.OrderInfo.total_sum) + '원 할인!')
            data.OrderInfo.total_sum=0
        root_view.destroy()
    else:
        messagebox.showerror('오류', '등록되지 않은 쿠폰입니다.', parent=root_view)