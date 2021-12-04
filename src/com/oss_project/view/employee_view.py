#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
from tkinter import*
import controller.employee_view_controller as employee_view_controller

#직원 관리화면
def open_employee_view():
  window = Tk()
  window.geometry("650x400")
  window.title("직원 관리")

  editFrame = Frame(window)
  editFrame.pack()
  listFrame = Frame(window)
  listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

  edit1 = Entry(editFrame, width=10);
  edit1.pack(side=LEFT, padx=10, pady=10)
  edit2 = Entry(editFrame, width=10);
  edit2.pack(side=LEFT, padx=10, pady=10)
  edit3 = Entry(editFrame, width=10);
  edit3.pack(side=LEFT, padx=10, pady=10)
  edit4 = Entry(editFrame, width=10);
  edit4.pack(side=LEFT, padx=10, pady=10)

  btnInsert = Button(editFrame, text="입력", command= lambda:employee_view_controller.insertData(edit1, edit2, edit3, edit4))
  btnInsert.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
  btnSelect = Button(editFrame, text="조회", command= lambda:employee_view_controller.selectData(listData1, listData2, listData3, listData4))
  btnSelect.pack(side=LEFT, padx=10, pady=10)

  listData1 = Listbox(listFrame, bg='gray')
  listData1.pack(side=LEFT, fill=BOTH, expand=1)
  listData2 = Listbox(listFrame, bg='gray')
  listData2.pack(side=LEFT, fill=BOTH, expand=1)
  listData3 = Listbox(listFrame, bg='gray')
  listData3.pack(side=LEFT, fill=BOTH, expand=1)
  listData4 = Listbox(listFrame, bg='gray')
  listData4.pack(side=LEFT, fill=BOTH, expand=1)

  window.mainloop()