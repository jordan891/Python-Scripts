class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getName(self):
    return self.name

  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudents
  
  def setNumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return "A {l} school named {n} with {nOS} students. ".format(l = self.level, n = self.name, 
    nOS = self.numberOfStudents)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup polity is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def getSportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    return "The teams are {teams}".format(teams = self.sportsTeams)

mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.getName())
print(mySchool.getLevel())
mySchool.setNumberOfStudents(200)
print(mySchool.getNumberOfStudents())

testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool.getPickupPolicy())
print(testSchool)

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)