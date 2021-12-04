import sqlite3
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
import database.data as datapath

#재고관리 컨트롤러
#재고 삽입 버튼 리스너
def insertbtn_listener(tree_view, name, price, stock):
    con = sqlite3.connect(datapath.path)
    cur = con.cursor()
    print(name, price, stock)
    try:
        sql = "INSERT INTO stock (name, price, stock) values (\'" + name + "\', " + price + ", " + stock + ")"
        cur.execute(sql)
    except Exception as e:
        messagebox.showerror('오류', '데이터 입력 오류가 발생하였습니다.', parent=tree_view)
        print(e)
    else:
        messagebox.showinfo('성공', '데이터 입력 성공', parent=tree_view)

    con.commit()
    con.close()

    # 기존에 입력한 입력 박스값 내용삭제
    for i in tree_view.get_children():
      tree_view.delete(i)
    selectbtn_controller(tree_view)

#재고 출력 버튼 리스너
def selectbtn_controller(tree_view):
    con = sqlite3.connect(datapath.path)
    cur = con.cursor()
    cur.execute("SELECT * FROM stock")

    tuples = []
    while True:
        row = cur.fetchone()
        if row == None:
            break
        tuples.append((row[0], row[1], row[2]))
        
    # 기존에 입력한 입력 박스값 내용삭제
    for i in tree_view.get_children():
      tree_view.delete(i)
    
    for i, (name, price, stock) in enumerate(tuples):
        tree_view.insert('', 'end', text= i + 1, values=(name, price, stock))
    con.close()
    tree_view.update()