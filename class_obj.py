class vehicle:
  def __init__(car, brand, model):
    car.Brand = brand
    car.Model = model
  def display(car):
    print("I am ", car.Brand)
  def __str__(car):
    return f"{car.Brand}({car.Model})"

class bike(vehicle):
    def __init__(bike, brand, model):
        super().__init__(brand, model)
        bike.Year = 2019
    def welcome(bike):
        print("I am ", bike.Brand, bike.Model, bike.Year)
        
m1 = bike("Hero", "Hunk")
m1.display()
m1.welcome()
print(m1)

v1 = vehicle("Toyota", 2023)
v1.Model = 2020
#del v1.Model

#print(v1.Brand)
#print(v1.Model)
#print(v1)
#v1.display()