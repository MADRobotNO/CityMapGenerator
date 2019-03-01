# terrain generator?

import random

from Terrain import Terrain
from Water import Water

building_types = (("bank", 0),
                  ("house", 1),
                  ("pharmacy", 0),
                  ("shop", 0),
                  ("police station", 0),
                  ("fire station", 0),
                  ("hospital", 0),
                  ("big apartment building", 4),
                  ("medium apartment building", 3),
                  ("small apartment building", 2),
                  ("health center", 0),
                  ("school", 0),
                  ("kindergarten", 0))


arr = []  # map

# creating a map 10x10
for line in range(15):
    arr.append([])
    for row in range(15):
        types = random.randrange(0, 6)  # road (0-1) or building (2-4)
        if types < 2:
            arr[line].append(Terrain())
            # print("Building", line, row)
        else:
            if line > 0 and row > 0:
                if isinstance(arr[line][row-1], Water) or isinstance(arr[line-1][row], Water):
                        arr[line].append(Water())
                        # print("Street2", line, row)
                else:
                    # print("ExceptB", line, row)
                    arr[line].append(Terrain())
            else:
                arr[line].append(Water())  # first line is independent
                # print("Street1", line, row)

# iterate thru array and print out
for line in arr:
    for obj in line:
        if isinstance(obj, Terrain):
            print("X", end=" ")
        if isinstance(obj, Water):
            print(".", end=" ")
    print("")
