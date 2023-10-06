nums = (16, 2, 19, 22, 10, 23, 16, 2, 27, 29, 19, 26, 12, 20, 16, 29, 6, 2, 12, 20)

# Checkpoint 1 code goes here.
filtered = filter(lambda x: x%2==0, nums)
print(tuple(filtered))

# Checkpoint 2 code goes here.
mult = map(lambda x: x*3, nums)
print(tuple(mult))

# Checkpoint 3 code goes here.
from functools import reduce
mapped = reduce(lambda x, y: x + y, nums)
print(mapped)