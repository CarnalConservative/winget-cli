class Product:
  def __init__(self, id, name, price, quantity):
    self.name = name
    self.id = id
    self.price = price
    self.quantity = quantity
  
#This will find the total price
def get_total_price(self):
  return self.price * self.quantity
  
  
#This will display the price
def display(self):
  print('{}({}) - ${:.2f}'.format(self.name,self.quantity,self.get_total_price()))