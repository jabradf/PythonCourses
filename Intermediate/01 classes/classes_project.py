class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  def __repr__(self):
    return "This school's name is " + self.name + ", has " + str(self.numberOfStudents) + " students, and is a " + str(self.level) + " school."

  def get_name(self):
    return str(self.name)
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents
  def set_numberOfStudents(self, newNumber):
    self.numberOfStudents = newNumber

class Primary(School):
  def __init__(self, name, level, numberOfStudents, pickupPolicy="none"):
    super().__init__(name, "Primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def get_pickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parent = super().__repr__()
    return parent + "\nThe pickup policy is " + self.pickupPolicy + "."

class Middle(School):
  def __init__(self, name, level, numberOfStudents):
    super().__init__(name, "Middle", numberOfStudents)
  def __repr__(self):
    parent = super().__repr__()
    return parent

class High(School):
  sportsTeams = []
  def __init__(self, name, level, numberOfStudents, sportsTeams=['none']):
    super().__init__(name, "High", numberOfStudents)
    self.sportsTeams = sportsTeams
  def get_sportsTeams(self):
    return self.sportsTeams


new = School("cool", "Primary", 100)
new.name = "cool"

print(new)
print(new.get_numberOfStudents())
new.set_numberOfStudents(98)
print(new.get_numberOfStudents())

print("---")
newPrim = Primary("Junior Jack's", "Primary", 33)
print(newPrim.get_numberOfStudents())
print(newPrim)

print("---")
teams = ['chess', 'golf', 'volleyball']
newHigh = High("Joe's High", "High", 321, teams)
print(newHigh.get_numberOfStudents())
print(newHigh.get_sportsTeams())