# original class with restrictions:
class Box:
  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

# -------------------

'''
Running these commands:

box = Box(10)

box.setWeight(-5) 
print(box.getWeight())

box.setWeight(5)
print(box.getWeight())


#returns this:
10 
5
'''


# -------------------
# add the property method
class Box:
  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

  def delWeight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")


'''
box = Box(10)

print(box.weight) #this calls .getWeight()

box.weight = 5 #this called .setWeight()

del box.weight #this calls .delWeight()

box.weight = -5 #box.__weight is unchanged 


With this change, our program gains some immediate benefits:

We can now use the weight attribute as if it was public. We no longer have to call the setters, 
getters, and deleter methods directly and thus giving our program a simpler syntax.
Even though we no longer call the methods directly, we still can maintain constraints such as the 
weight limit in setWeight(). It’s the best of both worlds!
If we had a huge codebase that used our methods multiple times in multiple places, a single change 
to the method name would seriously mess up our program since we would have to change it everywhere! 
We no longer have this issue using the property() method since we never call it directly.
While this is a big advantage for our programs to be more “pythonic”, we can go even further by using 
the decorator pattern to replace the need to call the property() function altogether.
'''
# -------------------

# the @property decorator
class Box:
 def __init__(self, weight):
   self.__weight = weight

 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight


 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight

 @weight.deleter
 def weight(self):
   del self.__weight

'''
This is a cleaner way of the property method!

box = Box(10)

box.weight = 5

del box.weight
'''


'''
To summarize, we learned:

The limitations of using regular setter and getter methods.
How to use the property() function to create cleaner getters, setters, and deleters.
The @property decorator is the most “pythonic” way to use the property() function.
When using the decorator, remember three rules:

All three methods must use the same member name (ex. weight).
The first method must be the getter and is identified using @property.
The decorators for the setter and deleter are defined by the name of the method @property is used with.
Keep the @property decorator in mind when approaching any object-oriented program! 
It will save time and keep code cleaner and more maintainable.
'''