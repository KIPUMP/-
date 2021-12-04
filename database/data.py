import os
#데이터베이스 경로
path = os.path.dirname(os.path.realpath(__file__)) + "/sqllite_db.db"

#결제 과정 저장 클래스
class OrderInfo:
  total_order_id = None
  total_ordered_product_list = []
  total_sum = None