class Employee():
    def __init__(self):
        self.id = None
        # Write your code below
        self._id = 40
        self.__id = 70

e = Employee()
print(dir(e))

# When you run the code you can see _id as the second to last element in the output list.
# When you run the code you can see a new variable _Employee__id as the first element in the output list. This is the result of name-mangling the variable self.__id.