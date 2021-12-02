#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

#주문화면
from tkinter import*
import controller.manage_view_controller as controller


def open_manage_view():
  #view 영역에서 새 창만들기 시작
  manage_root = Toplevel()
  manage_root.title("관리 창")
  manage_root.resizable(0, 0)
  
  btnstock = Button(manage_root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="STOCK", bg="powder blue", command=controller.stock_button_litener)
  btnstock.grid(row=0, column=0)
  
  btnorder = Button(manage_root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="ORDER", bg="powder blue", command=controller.order_button_litener)
  btnorder.grid(row=0, column=1)
  
  btnemployee = Button(manage_root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EMPLOYEE", bg="powder blue")
  btnemployee.grid(row=1, column=0)