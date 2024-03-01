# arrays used to store multiple values in one single variable:

cars = ["Ford", "BMW", "Volvo"]
x = cars[0]

# modifying an array
cars[0] = "Toyota"
# print(cars)

# length of an Array

x = len(cars)
#print(x)

# Looping Array Elements
for x in cars:
    print(x)
    
# Adding Array Elements
cars.append("Honda")
# print(cars)

# Removng Array Elements
cars.pop(1)
#print(cars)

#cars.remove('volvo') # removes the 1st occurence of a specified value
#print(cars)