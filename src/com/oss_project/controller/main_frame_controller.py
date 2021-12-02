#메인프레임 버튼 등의 이벤트리스너
#모듈 연결용 임시코드
import sys
import os
from tkinter import messagebox
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
import database.data as data
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import view.manage_view as manage_view
import view.pay_view as pay_view

def manage_button_litener():
  manage_view.open_manage_view()
  
def total_button_listener(order_id, ordered_product_list, tax):
  data.OrderInfo.total_order_id = order_id
  data.OrderInfo.total_ordered_product_list = ordered_product_list
  data.OrderInfo.total_tax = tax
  
def reset_button_listener():
  data.OrderInfo.total_order_id = None
  data.OrderInfo.total_ordered_product_list = []
  data.OrderInfo.total_tax = None
  
def pay_button_listener():
  if data.OrderInfo.total_order_id == None:
    messagebox.showerror('오류', '결제할 항목이 없습니다.')
  else:
    pay_view.open_pay_view()