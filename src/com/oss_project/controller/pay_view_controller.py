#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
import database.data as data
import controller.main_frame_controller as controller
from tkinter import messagebox
import sqlite3

def cash_button_listener(root_view):
  flag = messagebox.askokcancel('결제 확인', '결제를 승인하시겠습니까?')
  if flag == True:
    print(data.OrderInfo.total_tax)
    root_view.destroy()
  else:
    root_view.destroy()
    
def qr_button_listener(root_view):
  pass
  #QR 결제 로직
  
  #성공하면 재고를 차감하고 주문 리스트에 삽입
  
def query(root_view):
    con = sqlite3.connect(data.path)
    cur = con.cursor()
    
    try:
        sql = "INSERT INTO 'order' ('ID', 'price_sum') values (\'" + data.OrderInfo.total_order_id + "\', " + data.OrderInfo.total_sum + ")"
        cur.execute(sql)
        for (name, num, price) in data.OrderInfo.total_ordered_product_list:
          "INSERT INTO 'ordered_product' ('order_id', 'product_name', 'num', 'unit_price') values (\'" + data.OrderInfo.total_order_id + "\', \'" + name + "\', " + num + ", " + price +")"
        for (name, num, price) in data.OrderInfo.total_ordered_product_list:
          "UPDATE SET 'stock' 'stock'=" + "(""(select 'stock' from 'stock' where 'name'=\'"+ name + "\')-" + num + ")" + "where 'name' = \'" + name + "\'"
    except Exception as e:
        messagebox.showerror('오류', '데이터 입력 오류가 발생하였습니다.', parent=root_view)
        print(e)
    else:
        messagebox.showinfo('성공', '데이터 입력 성공', parent=root_view)

    con.commit()
    con.close()