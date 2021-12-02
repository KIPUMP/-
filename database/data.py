import os
path = os.path.dirname(os.path.realpath(__file__)) + "/sqllite_db.db"

class OrderInfo:
  total_order_id = None
  total_ordered_product_list = []
  total_tax = None
  total_sum = None