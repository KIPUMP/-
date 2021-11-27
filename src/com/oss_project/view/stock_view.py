#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

#재고화면
import tkinter
import tkinter.ttk
import data as data


def open_stock_view():
  #view 영역에서 새 창만들기 시작
  stock_root = tkinter.Tk()
  stock_root.geometry("1280x720+0+0")
  stock_root.title("재고 리스트")
  stock_root.resizable(0, 0)




  #스크롤 바 생성
  scroll_bar_y = tkinter.ttk.Scrollbar(master=stock_root)
  scroll_bar_y.pack(side = "right", fill = "y")
  scroll_bar_x = tkinter.ttk.Scrollbar(master=stock_root, orient=tkinter.HORIZONTAL)
  scroll_bar_x.pack(side = "bottom", fill = "x")


  #Treeview 생성 및 초기 설정
  treeView = tkinter.ttk.Treeview(stock_root, columns=["상품명", "가격", "개수"], xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
  treeView.column("#0", width=70)
  treeView.heading("#0", text="순번", anchor="center")

  treeView.column("상품명", width=100, anchor="center")
  treeView.heading("상품명", text="상품명", anchor="center")

  treeView.column("가격", width=100, anchor="center")
  treeView.heading("가격", text="가격", anchor="center")

  treeView.column("개수", width=100, anchor="w")
  treeView.heading("개수", text="개수", anchor="center")
  treeView.pack(fill="both", expand=1)
  
  stock_add_btn = tkinter.ttk.Button(stock_root, )

  #스크롤 바 연결
  scroll_bar_y.config(command = treeView.yview )
  scroll_bar_x.config(command = treeView.xview )

  #-----------------데이터 넣는 부분-------------------------------------
  dict = data.product_dict
  for i, k in enumerate(dict.keys()):
    treeView.insert('', 'end', text= i + 1, values=(k, dict[k].num, dict[k].price))
  #---------------------------------------------------------------------



  stock_root.mainloop()