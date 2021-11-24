class Order():
  _stock = {}
  def add(self, entity, num):
    if(self._stock.get(entity.name)==None):
      self._stock[entity.name] = num
    else:
      self._stock[entity.name] += num
      
 
    
#test logic
import tkinter
import tkinter.ttk

root = tkinter.Tk()
root.geometry("1600x700+0+0")
root.title("주문 리스트")
order = Order()

treeView = tkinter.ttk.Treeview(root, columns=["주문 내역", "가격", "결제 시각"], displaycolumns=["주문 내역", "가격", "결제 시각"])
treeView.pack()

treeView.column("#0", width=70)
treeView.heading("#0", text="주문번호", anchor="center")

treeView.column("주문 내역", width=100, anchor="center")
treeView.heading("주문 내역", text="주문 내역", anchor="center")

treeView.column("가격", width=100, anchor="center")
treeView.heading("가격", text="가격", anchor="center")

treeView.column("결제 시각", width=100, anchor="w")
treeView.heading("결제 시각", text="결제 시각", anchor="center")




root.mainloop()