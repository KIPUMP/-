class Stock():
  _stock = {}
  def add(self, product, num):
    if(self._stock.get(product.name)==None):
      self._stock[product.name] = num
    else:
      self._stock[product.name] += num
      
    
    
class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
 
    
#test logic
import tkinter
import tkinter.ttk

root = tkinter.Tk()
root.geometry("1600x700+0+0")
root.title("재고 리스트")
stock = Stock()


# def new():
#    global new 
#  new = tkinter.Toplevel(root)
# testCtockBtn = tkinter.Button(root, padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="powder blue", command=lambda:new())
# testCtockBtn.grid(row=1,column=1)


treeView = tkinter.ttk.Treeview(root, columns=["상품명", "재고", "가격"], displaycolumns=["상품명", "재고", "가격"])
treeView.pack()

treeView.column("#0", width=70)
treeView.heading("#0", text="순번", anchor="center")

treeView.column("상품명", width=100, anchor="center")
treeView.heading("상품명", text="상품명", anchor="center")

treeView.column("재고", width=100, anchor="center")
treeView.heading("재고", text="재고", anchor="center")

treeView.column("가격", width=100, anchor="w")
treeView.heading("가격", text="가격", anchor="center")




root.mainloop()