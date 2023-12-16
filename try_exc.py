#x = 20
#try:
#  print(x)
#except NameError:
#  print('Variable x is not defined')
#finally:
#  print("The 'try except' is finished")

x = -1

#if x < 0:
#  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")