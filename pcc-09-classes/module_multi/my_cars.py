from car import Car
from car_electric import ElectricCar

audi = Car('audi', 'a4', '2025')
print(audi.describe_car())

my_leaf = ElectricCar('nissan', "leaf", "2025")
print(my_leaf.describe_car())