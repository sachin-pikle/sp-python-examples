from car import Car, ElectricCar

audi = Car('audi', 'a4', '2025')
print(audi.describe_car())
audi.read_odometer()

audi.odometer_reading = 20
audi.read_odometer()

audi.update_odometer(1)
audi.update_odometer(23000)
audi.read_odometer()

audi.increment_odometer(-100)
audi.increment_odometer(555)
audi.read_odometer()

print("\n")

my_leaf = ElectricCar('nissan', "leaf", "2024")
print(my_leaf.describe_car())
my_leaf.battery.describe_battery()