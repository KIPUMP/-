#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

#주문화면
import tkinter
import tkinter.ttk
import data as data


def open_order_view():
  #view 영역에서 새 창만들기 시작
  order_root = tkinter.Toplevel()
  order_root.geometry("1280x720+0+0")
  order_root.title("주문 리스트")
  order_root.resizable(0, 0)

  #스크롤 바 생성
  scroll_bar_y = tkinter.ttk.Scrollbar(master=order_root)
  scroll_bar_y.pack(side = "right", fill = "y")
  scroll_bar_x = tkinter.ttk.Scrollbar(master=order_root, orient=tkinter.HORIZONTAL)
  scroll_bar_x.pack(side = "bottom", fill = "x")


  #Treeview 생성 및 초기 설정
  treeView = tkinter.ttk.Treeview(order_root, columns=["주문 내역", "가격", "결제 시각"], xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
  treeView.column("#0", width=70)
  treeView.heading("#0", text="주문번호", anchor="center")

  treeView.column("주문 내역", width=100, anchor="center")
  treeView.heading("주문 내역", text="주문 내역", anchor="center")

  treeView.column("가격", width=100, anchor="center")
  treeView.heading("가격", text="가격", anchor="center")

  treeView.column("결제 시각", width=100, anchor="w")
  treeView.heading("결제 시각", text="결제 시각", anchor="center")
  treeView.pack(fill="both", expand=1)

  #스크롤 바 연결
  scroll_bar_y.config(command = treeView.yview )
  scroll_bar_x.config(command = treeView.xview )

#-----------------데이터 넣는 부분-------------------------------------
  list = data.order_list
  for o in list:
    treeView.insert('', 'end', text=o.get_order_num(), values=(o.to_tuple()))
#---------------------------------------------------------------------    
    

  order_root.mainloop()