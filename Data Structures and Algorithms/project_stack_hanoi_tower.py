#from stack import Stack
from stacks import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("\nEnter a number that is at least 3\n"))

for item in range(num_disks, 0, -1):
  left_stack.push(item)

num_optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

# Get User Input
def get_input():
  choices = [i.get_name()[0] for i in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f"Enter {letter} for {name}")
    user_input = input("")
    #print("choices are: ", choices)
    #print("input was", user_input)
    if user_input in choices:
      #print("matched!")
      for i in range(len(stacks)):
        if user_input == choices[i]:
          print(choices[i])
          return stacks[i]

#Play the Game
num_user_moves = 0

while (right_stack.get_size() != num_disks):
  print("\n\n...Current Stacks...")
  for st in stacks:
    st.print_items()
  while True:
    print("Which stack do you want to move from?\n")
    from_stack = get_input()
    print("Which stack do you want to move to?\n")
    to_stack = get_input()
    print(f"from: {from_stack.get_name()} to: {to_stack.get_name()}")
    if from_stack.is_empty():
      print("\nInvalid move, stack is empty! Try again")
    elif (to_stack.is_empty() or from_stack.peek()<to_stack.peek()):
      print("good move!")
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("Cannot put larger disk onto smaller disk. Try again!")
print(f"You completed the game in {num_user_moves} moves. The optimal number of moves were {num_optimal_moves}.")

