#메인프레임 버튼 등의 이벤트리스너
#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import view.order_view as order_view
import view.stock_view as stock_view
import view.employee_view as employee_view

#관리 영역 컨트롤러
def order_button_litener():
  order_view.open_order_view()
  
def stock_button_litener():
  stock_view.open_stock_view()
  
def employee_button_listener():
  employee_view.open_employee_view()
  