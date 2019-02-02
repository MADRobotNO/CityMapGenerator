from Generator import *
from GUI import *

x = int(input("Enter number of columns: "))
y = int(input("Enter number of rows: "))

generator = Generator(x, y)
map_one = generator.create_map()

number_of_buildings = 0
number_of_streets = 0
# iterate thru array and print out
for line in map_one:
    for obj in line:
        if isinstance(obj, Building):
            number_of_buildings += 1
            print("B", end=" ")
        if isinstance(obj, Street):
            number_of_streets += 1
            print("*", end=" ")
    print("")

print("")
print("Number of buildings:", number_of_buildings)
print("Number of streets:", number_of_streets)

gui = Gui(map_one)
gui.create_map()