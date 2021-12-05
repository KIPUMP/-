#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
import database.data as data
from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import Tk
import tkinter

#현금 결제
def cash_button_listener(root_view):
  flag = messagebox.askokcancel('결제 확인', '결제를 승인하시겠습니까?')
  if flag == True:
    query(root_view)
    root_view.destroy()
  else:
    root_view.destroy()

#QR 결제
def qr_button_listener(root_view):
  w = Tk()
  w.title("kakao_pay")
  w.geometry("500x500")
  w.resizable(True,True)
  
  
  btncancel = Button(w,text = "QR 결제 성공",fg = "white", bg = "blue" ,padx=20,pady=8, bd=10, command=lambda: query(root_view))
  btncancel.pack(side = BOTTOM)
  btncancel = Button(w,text = "QR 결제 취소",fg = "white", bg = "blue" ,padx=20,pady=8, bd=10)
  btncancel.pack(side = BOTTOM)
  
  photo = tkinter.PhotoImage(file= "src\com\oss_project\controller\kakaopay.gif",master=w)
  pLabel = Label(w, image = photo)
  pLabel.pack()

  w.mainloop()
  
#주문시 데이터베이스에 쿼리문 실행
def query(root_view):
    con = sqlite3.connect(data.path)
    cur = con.cursor()
    
    try:
        sql = "INSERT INTO 'order' ('ID', 'price_sum') values (\'" + data.OrderInfo.total_order_id + "\', " + str(data.OrderInfo.total_sum) + ")"
        cur.execute(sql)
        for (name, num, price) in data.OrderInfo.total_ordered_product_list:
          sql = "INSERT INTO 'ordered_product' ('order_id', 'product_name', 'num', 'unit_price') values (\'" + data.OrderInfo.total_order_id + "\', \'" + name + "\', " + str(num) + ", " + str(price) +")"
          cur.execute(sql)
    except Exception as e:
        messagebox.showerror('오류', '데이터 입력 오류가 발생하였습니다.', parent=root_view)
        print(e)
    else:
        messagebox.showinfo('성공', '데이터 입력 성공', parent=root_view)

    con.commit()
    con.close()