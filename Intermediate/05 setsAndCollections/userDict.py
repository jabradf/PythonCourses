
data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
from collections import UserDict

class OrderProcessingDict(UserDict):
  def clean_orders(self):
    del_list = []
    for key, item in self.data.items():
      if item['order_status'] == 'complete':
        del_list.append(key)
    
    for item in del_list:
      del self.data[item]


process_dict = OrderProcessingDict(data)
print(process_dict)
process_dict.clean_orders()
print(process_dict)