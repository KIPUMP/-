#개발 중
# class Stock():
#   _stock = {}
#   @staticmethod
#   def add(product_name, num):
#     if(product_name in Product.get_product_info_dict()):
#       if product_name not in Stock._stock:
#         Stock._stock[product_name] = num
#       else:
#         Stock._stock[product_name] += num
#     else:
#       raise Exception("없는 물품입니다. 물품 등록을 먼저 해주세요.")
      
#   @staticmethod
#   def get_stock_dic():
#     return Stock._stock
    
# class Product:
#   _product_info = {}
#   @staticmethod
#   def regist(name, price):
#     Product._product_info[name] = price
  
#   @staticmethod
#   def get_product_info_dict():
#     return Product._product_info
    
# #test logic
# import tkinter
# import tkinter.ttk

# #---------------------------------------------------------------------
# #view 영역에서 새 창만들기 시작
# root = tkinter.Tk()
# root.geometry("1280x720+0+0")
# root.title("재고 리스트")
# root.resizable(0, 0)

# #스크롤 바 생성
# scroll_bar_y = tkinter.ttk.Scrollbar()
# scroll_bar_y.pack(side = "right", fill = "y")
# scroll_bar_x = tkinter.ttk.Scrollbar(orient=tkinter.HORIZONTAL)
# scroll_bar_x.pack(side = "bottom", fill = "x")


# #Treeview 생성 및 초기 설정
# treeView = tkinter.ttk.Treeview(root, columns=["상품명", "가격", "개수"], xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
# treeView.column("#0", width=70)
# treeView.heading("#0", text="순번", anchor="center")

# treeView.column("상품명", width=100, anchor="center")
# treeView.heading("상품명", text="상품명", anchor="center")

# treeView.column("가격", width=100, anchor="center")
# treeView.heading("가격", text="가격", anchor="center")

# treeView.column("개수", width=100, anchor="w")
# treeView.heading("개수", text="개수", anchor="center")
# treeView.pack(fill="both", expand=1)

# #스크롤 바 연결
# scroll_bar_y.config(command = treeView.yview )
# scroll_bar_x.config(command = treeView.xview )

# #---------------------------------------------------------------------
# #버튼이 눌리면 컨트롤러 영역에서 entity들을 view에 넣어준다음 출력한다

# #테스트를 위해 넣는 부분
# Product.regist(name="감자", price=1000)
# Stock.add("감자", 10)
# for i, (k, v) in enumerate(Stock.get_stock_dic().items()):
#   treeView.insert('', 'end', text=i, values=(k, Product.get_product_info_dict()[k], v))

# #---------------------------------------------------------------------


# root.mainloop()