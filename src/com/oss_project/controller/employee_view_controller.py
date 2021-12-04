import sqlite3
from tkinter import*
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
import database.data as datapath

#직원 관리 컨트롤러
#데이터 베이스 사용하기 위한 메소드
#데이터 삽입
def insertData(edit1, edit2, edit3, edit4):
    con, cur = None, None
    data1, data2, data3, data3 = "", "", "", ""
    sql = ""

    con = sqlite3.connect(datapath.path) #여기의 주소에 있는 db파일을 불러온다
    cur = con.cursor()
    data1 = edit1.get();data2 = edit2.get();data3 = edit3.get();data4 = edit4.get()
    try:
        sql = "insert into employee_data (id,name,department,start_work) values ('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
        cur.execute(sql)
    except:
        messagebox.showerror('오류', '데이터 입력 오류가 발생하였습니다.')
    else:
        messagebox.showinfo('성공', '데이터 입력 성공')

    con.commit()
    con.close()

    # 기존에 입력한 입력 박스값 내용삭제
    edit1.delete(0, END);edit2.delete(0, END);edit3.delete(0, END);edit4.delete(0, END)
    selectData()

#데이터 출력
def selectData(listData1, listData2, listData3, listData4):
    strData1, strData2, strData3, strData4 = [], [], [], []
    con = sqlite3.connect(datapath.path)
    cur = con.cursor()
    cur.execute("SELECT * FROM employee_data")

    strData1.append("직원ID");strData2.append("직원이름");strData3.append("부서");strData4.append("입사일")
    strData1.append("-------");strData2.append("-------");strData3.append("-------");strData4.append("-------")

    while True:
        row = cur.fetchone()
        if row == None:
            break
        strData1.append(row[0]);strData2.append(row[1]);strData3.append(row[2]);strData4.append(row[3])

    # 기존의 listBox 화면들을 모두 지움
    listData1.delete(0, listData1.size() - 1);listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1);listData4.delete(0, listData4.size() - 1)

    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)
    con.close()

    # 메인
    

