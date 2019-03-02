import random

from Terrain import Terrain
from Water import Water

arr = []  # map

# creating a map 10x10
for line in range(15):
    arr.append([])
    for row in range(15):

        # Random choose if next object is a terrain or water
        types = random.randrange(0, 6)  # water (0-1) or terrain (2-5) - proportion 2:4

        # if object is a terrain
        if types < 2:
            arr[line].append(Terrain())
            # print("Terrain", line, row)

        # if object is a water
        else:

            # for elements other than first
            if line > 0 and row > 0:

                #  Water elements should be connected if possible.
                #  Check last row and last object if it's a water element.
                if isinstance(arr[line][row-1], Water) or isinstance(arr[line-1][row], Water):
                        arr[line].append(Water())
                        # print("Water", line, row)
                else:
                    # print("Terrain", line, row)
                    arr[line].append(Terrain())

            # for first elements
            else:
                arr[line].append(Water())  # first line is independent
                # print("Water", line, row)

# iterate thru array and print out
for line in arr:
    for obj in line:
        if isinstance(obj, Terrain):
            print("X", end=" ")
        if isinstance(obj, Water):
            print(".", end=" ")
    print("")
