def summa():
    yield 'Summa Cum Laude'
def magna():
    yield 'Magna Cum Laude' 
def cum_laude():
    yield 'Cum Laude'
# Write your code below:
def graduation_countdown(days):
  days_left = yield days
  if days_left is not None:
    days = days_left
    #continue
  else:
    days -= 1

def honors_generator(gpas):
  for item in gpas:
    if item > 3.9:
      yield from summa()
    elif item > 3.7:
      yield from magna()
    elif item > 3.5:
      yield from cum_laude()

days = 25
countdown_generator = (day for day in range(days, -1,-1))

grad_days = graduation_countdown(days)

for item in grad_days:
  if item==15:
    grad_days.send(10)
  elif item==3:
    grad_days.close()
  print(f'Days Left: {item}')

gpas = [3.2, 4.0, 3.6, 2.9]
honors = honors_generator(gpas)
for item in honors:
  print(item)