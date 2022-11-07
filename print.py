cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = space_in_a_car * cars_driven
average_pessengers_per_car = passengers / cars_driven

print("There are",cars, "cars available.")
print("There are only",drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("we can transport", carpool_capacity, "people today.")
print("we have", passengers, "to carpool today.")
print("we need to put about", average_pessengers_per_car, "in each car.")
