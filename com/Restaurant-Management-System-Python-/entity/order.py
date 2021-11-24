import time
from tkinter.constants import ANCHOR, HORIZONTAL
class Order():
  def __init__(self, order_num, purchase_history, total_price, purchase_time):
    self.order_num = order_num
    self.purchase_history = purchase_history
    self.total_price = total_price
    self.purchase_time = purchase_time
  
  def get_order_num(self):
    return self.order_num
  
  def toTuple(self):
    return (self.purchase_history, self.total_price, self.purchase_time)

#test logic
import tkinter
import tkinter.ttk

#---------------------------------------------------------------------
#view 영역에서 새 창만들기 시작
root = tkinter.Tk()
root.geometry("1280x720+0+0")
root.title("주문 리스트")
root.resizable(0, 0)

#스크롤 바 생성
scroll_bar_y = tkinter.ttk.Scrollbar()
scroll_bar_y.pack(side = "right", fill = "y")
scroll_bar_x = tkinter.ttk.Scrollbar(orient=tkinter.HORIZONTAL)
scroll_bar_x.pack(side = "bottom", fill = "x")


#Treeview 생성 및 초기 설정
treeView = tkinter.ttk.Treeview(root, columns=["주문 내역", "가격", "결제 시각"], xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
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

#---------------------------------------------------------------------
#버튼이 눌리면 컨트롤러 영역에서 entity들을 view에 넣어준다음 출력한다

#테스트를 위해 넣는 부분
order_list = [Order(10, '이것저것', 10000, time.strftime('%c', time.localtime()))]
treeView.insert('', 'end', text=order_list[0].get_order_num(), values=(order_list[0].toTuple()))



#---------------------------------------------------------------------



root.mainloop()