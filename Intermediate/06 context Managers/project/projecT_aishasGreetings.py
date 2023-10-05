# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type, senders_name, recipientArg):
  card = open(f'{card_type}.txt', 'r+')
  try:
    card.write(f"Dear {recipientArg},\n{card.read()} \nSincerely, {senders_name}")
    yield card
  finally:
    card.close()

'''with generic("thankyou_card", 'Mwenda', 'Amanda') as file:
  print("Card Generated!")
  print(file.read())'''

class personalised:
  def __init__(self, sender_name, receiver_name):
    self.sender_name = sender_name
    self.receiver_name = receiver_name
    self.file = open(f'{sender_name}_personalised.txt', 'w')

  def __enter__(self):
    self.file.write(f'Dear {self.receiver_name},\n')
    return self.file

  def __exit__(self, exc_type, exc_value, traceback):
    self.file.write(f'\nSincerely {self.sender_name}.')
    self.file.close()

with personalised("John", "Michael") as card:
  card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")


with generic("happy_bday", "Josiah", "Remy") as b_day_card:
  with personalised("Josiah", "Ester") as personalised_card:
    b_day_card.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")
