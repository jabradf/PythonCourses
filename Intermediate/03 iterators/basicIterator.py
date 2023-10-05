class CustomerCounter:
  # Write your code below:
  def __iter__(self):
      self.count = 0
      return self
  '''def __iter__(self):
    self.index = 0
    return self'''

  def __next__(self):
    self.count += 1
    if self.count > 100:
      raise StopIteration
    
    return self.count


    '''
    if self.index < len(self.available_fish):
      fish_status = self.available_fish[self.index] + " is available!"
      self.index += 1
      return fish_status
    else:
      raise StopIteration'''

customer_counter = CustomerCounter()

for cust in customer_counter:
  print(cust)