class Customer:
  def __init__(self):
    self.name = ''
    self.orders = []
    self.id = ''
#This is counting the orders
def get_order_count(self):
  return len(self.orders)
#This will find the total   
def get_total(self):
  newSum = 0
  for i in self.orders:
    newSum += i.get_total()
    return newSum
#This will append the order
def add_order(self, order):
  self.orders.append(order)
#This will display a summary of the orders
def display_summary(self):
  print("Summary for customer '{}':".format(self.id))
  print('Name: {}'.format(self.name))
  print('Orders: {}'.format(self.get_order_count()))
  print('Total: ${:.2f}'.format(self.get_total()))
#This is a display of the reciept
def display_receipts(self):
  for i in self.orders:
    i.display_receipt()