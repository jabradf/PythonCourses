from collections import UserString
str_name = 'python powered patterned products'
str_word = 'patterned '

# Write your code below!
class SubtractString(UserString):
  def __sub__(self, input):
    if input in self:
      self.data = self.data.replace(input, '')

subtract_string = SubtractString(str_name)
subtract_string - str_word

print(subtract_string)