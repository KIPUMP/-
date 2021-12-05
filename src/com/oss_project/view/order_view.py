import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
import tkinter
import tkinter.ttk
import sqlite3
import database.data as datapath
from tkinter import messagebox

#주문화면
def open_order_view():
  #view 영역에서 새 창만들기 시작
  order_root = tkinter.Toplevel()
  order_root.geometry("640x480+0+0")
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
  
  #값 삽입------------------------------------------------------------------------------------------------------------
  try:
    con = sqlite3.connect(datapath.path)
    cur = con.cursor()
    cur.execute("""select o.id, p.product_name, p.num, p.unit_price, o.purchase_time from "order" o
      left join "ordered_product" p on o.ID = p.order_id
      order by o.id;""")
  except:
      messagebox.showerror('오류', '데이터 오류가 발생하였습니다.', parent=order_root)

  tuples = []
  while True:
      row = cur.fetchone()
      if row == None:
          break
      tuples.append((row[0], row[1], row[2], row[3], row[4]))
      
  # 기존에 입력한 입력 박스값 내용삭제
  for i in treeView.get_children():
    treeView.delete(i)
  
  before_id =""
  for i, (id, detail, num, price, time) in enumerate(tuples):
      if before_id != id:
        treeView.insert('', 'end', text= "==========", values=("", "", ""))
        treeView.insert('', 'end', text= id, values=(detail+ "*" + str(num), price*num, time))
        before_id = id
      else:
        treeView.insert('', 'end', text= id, values=(detail+ "*" + str(num), price*num, time))

  con.close()
  treeView.update()
  #--------------------------------------------------------------------------------------------------------------------

  order_root.mainloop()