class Customer:
 
  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number


class CustomerWrap(Customer):
 
  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)
 
  def display_customer_info(self):
    print('Name: ' + self.customer.name)
    print('Age: ' + str(self.customer.age))
    print('Address: ' + self.customer.address)
    print('Phone Number: ' + self.customer.phone_number)


customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()