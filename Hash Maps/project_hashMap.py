from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for _ in range(self.array_size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
    
    list_at_array.insert(payload)


  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    
    return None



####################
blossom = HashMap(len(flower_definitions))

for element in flower_definitions:
  print(element)
  blossom.assign(element[0], element[1])

rtr = blossom.retrieve("magnolia")
print(rtr)
