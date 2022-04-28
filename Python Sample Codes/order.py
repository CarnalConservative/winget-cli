class Order:
  def __init__(self):
    self.id = id
    self.products = []
  
#This will find your subtotal
def get_subtotal(self):
  summ = 0
  for i in self.products:
    summ += i.get_total_price()
    return summ
#This will calulate the tax sum for you
def get_tax(self):
    return self.get_subtotal()*0.065
#This will add the subtotal and the tax   
def get_total(self):
  return self.get_tax()+self.get_subtotal()
#This will append the products
def add_product(self, product):
  self.products.append(product)
#This will display the reciept of the order
def display_receipt(self):
  print('Order: {}'.format(self.id))
  for product in self.products:
    product.display()
  
    print('Subtotal: ${:.2f}'.format(self.get_subtotal()))
    print('Tax: ${:.2f}'.format(self.get_tax()))
    print('Total: ${:.2f}'.format(self.get_total()))