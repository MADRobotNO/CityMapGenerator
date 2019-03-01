from Generator import *
from StreetGenerator import *
from StreetGenerator_v2 import *


from GUI import *


x = int(input("Enter number of rows: "))
y = int(input("Enter number of columns: "))
# generator = Generator(x, y)
# streetGenerator = StreetGenerator(x, y)
streetGenerator_v2 = StreetGenerator_v2(x, y)


# map1 = generator.create_map()
# map2 = streetGenerator.create_map()
map3 = streetGenerator_v2.create_map()


# gui1 = Gui(map1)
# gui1.create_map()

# gui2 = Gui(map2)
# gui2.create_map()

print("Number of street elements:", len(streetGenerator_v2.road))

gui3 = Gui(map3)
gui3.create_map()
