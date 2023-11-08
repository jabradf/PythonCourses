# simple recursion with addition:

# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return sum_to_one(n-1) + n

# uncomment when you're ready to test
print(sum_to_one(7))


# recursion with factorial. Going too big will result in a stack overflow here!
# Define factorial() below:
def factorial(n):
  if n<=1:
    return n
  return n*factorial(n-1)


print( factorial(30))