#메인프레임 버튼 등의 이벤트리스너
#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
import database.data as data
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import view.manage_view as manage_view
import view.pay_view as pay_view
import view.menu_view as menu_view
import view.calender_view as calender_view
import view.coupon_view as coupon_view
import datetime
from tkinter import messagebox

#메인화면 버튼 리스너 메서드들
#manage 버튼
def manage_button_litener():
  manage_view.open_manage_view()
  
#pay 버튼
def pay_button_listener():
  if data.OrderInfo.total_order_id == None:
    messagebox.showerror('오류', '결제할 항목이 없습니다.')
  else:
    pay_view.open_pay_view()
    
#total 버튼
def total_button_listener(order_id, menus, total_view):
  ordered_product_list = []
  total = 0
  for index, i in enumerate(menus):
    try:
      if i.get() == "":
        pass
      elif(int(i.get())<=0):
          raise Exception()
      else:
        
        if index == 0:
          ordered_product_list.append(("감자튀김", int(i.get()), 2500))
          total+=int(i.get())*2500
        elif index == 1:
          ordered_product_list.append(("런치 팩", int(i.get()), 4000))
          total+=int(i.get())*4000
        elif index == 2:
          ordered_product_list.append(("햄버거", int(i.get()), 3500))
          total+=int(i.get())*3500
        elif index == 3:
          ordered_product_list.append(("피자", int(i.get()), 5000))
          total+=int(i.get())*5000
        elif index == 4:
          ordered_product_list.append(("스파게티", int(i.get()), 3000))
          total+=int(i.get())*3000
        elif index == 5:
          ordered_product_list.append(("콜라", int(i.get()), 3500))
          total+=int(i.get())*3500
        elif index == 6:
          ordered_product_list.append(("Tax(VAT)", 1, int(i.get())))
          total+=int(i.get())
    except:
      messagebox.showinfo('오류','잘못된 입력입니다 정확한 수량을 입력해주세요')
      reset_button_listener(order_id, menus, total_view)
      return
  
  now = datetime.datetime.now()
  order_id.set(now.strftime("%Y")+now.strftime("%m")+now.strftime("%d")+now.strftime("%f"))
  total_view.set(str(total))
  
  if total!=0:
    data.OrderInfo.total_order_id = order_id.get()
    data.OrderInfo.total_ordered_product_list = ordered_product_list
    data.OrderInfo.total_sum = total
  else:
    data.OrderInfo.total_order_id = None
    data.OrderInfo.total_ordered_product_list = []
    data.OrderInfo.total_sum = None

def reset_button_listener(order_id, menus, total):
  data.OrderInfo.total_order_id = None
  data.OrderInfo.total_ordered_product_list = []
  data.OrderInfo.total_sum = None
  order_id.set("")
  total.set("")
  for i in menus:
    i.set("")

#coupon 버튼
def coupon_button_listener():
  coupon_view.open_coupon_view()

#menu 버튼
def menu_button_listener():
  menu_view.open_menu_view()

#calender 버튼
def calender_button_listener():
  calender_view.clickcalender()

#exit 버튼
def exit_button_listener(root_view):
  root_view.destroy()