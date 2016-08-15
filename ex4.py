# Number of cars available today
cars = 100
# The number of passengers we can fit in each car
space_in_a_car = 4
# Number of drivers available today
drivers = 30
# Number of passengers we need to transport
passengers = 90
# Cars that will not be driven due to lack of drivers
cars_not_driven = cars - drivers
# Number of cars driven today
cars_driven = drivers
# Number of total people we can transport today
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers in each car today
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Study drills
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

#   The error occurs because in line 8 this calculation refers to "passenger" when
#   the variable is defined in line 4 as "passengers".


#1  4.0 is not necessary.  When it is taken out an integer is a result of the multiplication using it.
#   Since the result of the multiplication is not used in any downstream calculations that need floating
#   point numbers then it is fine in this case.

#2
