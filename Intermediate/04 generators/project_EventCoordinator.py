guests = {}

def read_guestlist(file_name):
    text_file = open(file_name,'r')
    val = None
    while True:
        if val is not None:
            line_data = val.strip().split(",")
        else:
            line_data = text_file.readline().strip().split(",")

        if len(line_data) < 2:
        # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        val = yield name, age

guestlist = read_guestlist('guest_list.txt')
# for guest in guestlist:
for i in range(10):
    print(next(guestlist))
guestlist.send('Jane,35')
print("---")
for guest in guestlist:
  print(guest)

print("---")
'''for person in guests:
  print(guests[person])'''
#print(guests)

newList = (guests[person]>=21 for person in guests)
# evaluates true, not returning the person!
#over_21 = (key for key, val in  guests.items() if int(val) > 21)
over_21 = (key for key, val in  guests.items() if int(val) > 21)
for guest in over_21:
  print(guest)

print('---')

#Part 5
def chicken():
  food = 'Chicken'
  table = 1
  for i in range(5):
    seat = i + 1
    yield food, table, seat

def beef():
  food = 'Beef'
  table = 1
  for i in range(5):
    seat = i + 1
    yield food, table, seat

def fish():
  food = 'Fish'
  table = 1
  for i in range(5):
    seat = i + 1
    yield food, table, seat

def all_tables():
  yield from chicken()
  yield from beef()
  yield from fish()

tab = all_tables()

assign = ((guest, table) for guest, table in zip(guests, tab))

for i in range(15):
  print(next(assign))