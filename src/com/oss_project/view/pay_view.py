#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

#주문화면
from tkinter import*
import controller.pay_view_controller as controller


def open_pay_view():
  #view 영역에서 새 창만들기 시작
  manage_root = Toplevel()
  manage_root.title("결제 창")
  manage_root.resizable(0, 0)
  
  btnstock = Button(manage_root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="CASH", bg="powder blue", command=lambda: controller.cash_button_listener(manage_root))
  btnstock.grid(row=0, column=0)
  
  btnorder = Button(manage_root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="QR", bg="powder blue", command=lambda: controller.qr_button_listener(manage_root))
  btnorder.grid(row=0, column=1)
  
  btnemployee = Button(manage_root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="CANCEL", bg="powder blue", command=manage_root.destroy)
  btnemployee.grid(row=1, columnspan=2)