from tkinter import *
from tkinter import Tk

#메뉴 화면
def open_menu_view():
  roo = Tk()
  roo.geometry("600x220+0+0")
  roo.title("Price List")
  
  
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
  lblinfo.grid(row=0, column=0)
  lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
  lblinfo.grid(row=0, column=2)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
  lblinfo.grid(row=0, column=3)
  
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="감자튀김", fg="steel blue", anchor=W)
  lblinfo.grid(row=1, column=0)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2500", fg="steel blue", anchor=W)
  lblinfo.grid(row=1, column=3)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="런치팩", fg="steel blue", anchor=W)
  lblinfo.grid(row=2, column=0)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="4000", fg="steel blue", anchor=W)
  lblinfo.grid(row=2, column=3)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="햄버거", fg="steel blue", anchor=W)
  lblinfo.grid(row=3, column=0)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3500", fg="steel blue", anchor=W)
  lblinfo.grid(row=3, column=3)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="피자", fg="steel blue", anchor=W)
  lblinfo.grid(row=4, column=0)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5000", fg="steel blue", anchor=W)
  lblinfo.grid(row=4, column=3)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="스파게티", fg="steel blue", anchor=W)
  lblinfo.grid(row=5, column=0)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3000", fg="steel blue", anchor=W)
  lblinfo.grid(row=5, column=3)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="콜라", fg="steel blue", anchor=W)
  lblinfo.grid(row=6, column=0)
  lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3500", fg="steel blue", anchor=W)
  lblinfo.grid(row=6, column=3)

  roo.mainloop()