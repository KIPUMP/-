#메인프레임 버튼 등의 이벤트리스너
#모듈 연결용 임시코드
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import view.order_view as order_view
import view.stock_view as stock_view

def order_button_litener():
  order_view.open_order_view()
  
def stock_button_litener():
  stock_view.open_stock_view()