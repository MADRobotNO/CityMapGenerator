import random

from Building import Building
from Street import Street

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
for line in range(10):
    arr.append([])
    for row in range(10):
        types = random.randrange(1,5)
        if types < 2:
            arr[line].append(Building("building", building_types[random.randrange(0, 13)]))
            # print("Building", line, row)
        else:
            if line > 0 and row > 0:
                if isinstance(arr[line][row-1], Street) or isinstance(arr[line-1][row], Street):
                        arr[line].append(Street("street"))
                        # print("Street2", line, row)
                else:
                    # print("ExceptB", line, row)
                    arr[line].append(Building("building", building_types[random.randrange(0, 13)]))
            else:
                arr[line].append(Street("street"))  # first line is independent
                # print("Street1", line, row)

# iterate thru array and print out
for line in arr:
    for obj in line:
        if isinstance(obj, Building):
            print("B", end=" ")
        if isinstance(obj, Street):
            print("*", end=" ")
    print("")


