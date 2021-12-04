#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import tkinter
import tkinter.ttk
import controller.stock_view_controller as controller

#재고화면
def open_stock_view():
  #view 영역에서 새 창만들기 시작
  stock_root = tkinter.Tk()
  stock_root.geometry("640x480+0+0")
  stock_root.title("재고 리스트")
  stock_root.resizable(0, 0)
  

  editFrame = tkinter.ttk.Frame(stock_root)
  editFrame.pack()

  edit1 = tkinter.Entry(editFrame, width=12);
  edit1.pack(side=tkinter.LEFT, padx=10, pady=10)
  edit2 = tkinter.Entry(editFrame, width=12);
  edit2.pack(side=tkinter.LEFT, padx=10, pady=10)
  edit3 = tkinter.Entry(editFrame, width=12);
  edit3.pack(side=tkinter.LEFT, padx=10, pady=10)



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
  
  btnInsert = tkinter.Button(editFrame, text="입력", command=lambda: controller.insertbtn_listener(treeView, edit1.get(), edit2.get(), edit3.get()))
  btnInsert.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=10, pady=10)
  btnSelect = tkinter.Button(editFrame, text="조회", command=lambda: controller.selectbtn_controller(treeView))
  btnSelect.pack(side=tkinter.LEFT, padx=10, pady=10)

  #스크롤 바 연결
  scroll_bar_y.config(command = treeView.yview )
  scroll_bar_x.config(command = treeView.xview )

  stock_root.mainloop()