cars = 100
space_in_cars = 4
drivers = 30
passengers = 79
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars
average_per_car = passengers / cars_driven
print "there are", cars, "cars available"
print "there are only", drivers, "drivers available"
print "there will be", cars_not_driven, "cars not driven"
print "there are", passengers, "passengers"
print "we can transport", carpool_capacity, "people today"
print "we need to put", average_per_car, "in each car"
print "GOODBYE"
