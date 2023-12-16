#mytuple = ("apple", "banana", "cherry")
#mystr = "mango"
#myit = iter(mytuple)
#myit_2 = iter(mystr)

#print(next(myit))
#print(next(myit))
#print(next(myit))


#print(next(myit_2))
#print(next(myit_2))
#print(next(myit_2))
#print(next(myit_2))
#print(next(myit_2))

class MyStudents:
  def __iter__(self):
    self.a = iter('APSRM')
    self.i = 0
    return self

  def __next__(self):
    if self.i <= 2:
      x = next(self.a)
      self.i = self.i + 1
      return x
    else:
      StopIteration
  
#def __getitem__(self, index):

myclass = MyStudents()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))