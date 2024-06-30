# You have a water tank with a capacity of 255 liters. On the first line, you
# will receive n – the number of lines, which will follow. On the following n lines,
# you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue
# reading the next line. On the last line, print the liters in the tank.

capacity = 255

number_of_lines = int(input())

tank = 0
for i in range (1, number_of_lines + 1):
    liters_of_water = int(input())
    if tank + liters_of_water > capacity:
        print("Insufficient capacity!")
    else:
        tank += liters_of_water

print(tank)
