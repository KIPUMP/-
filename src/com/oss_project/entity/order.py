#주문정보
class Order():
  def __init__(self, order_num, purchase_history, total_price, purchase_time):
    self.order_num = order_num
    self.purchase_history = purchase_history
    self.total_price = total_price
    self.purchase_time = purchase_time
    
  def to_tuple(self):
    return (self.purchase_history, self.total_price, self.purchase_time)
  
  def get_order_num(self):
    return self.order_num