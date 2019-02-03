import random

from operator import xor  # either operator

from Building import Building
from Street import Street


class Generator:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

        # types of buildings (name of type and level of inhabitants in scale from 0 to 4)
        self.building_types = (("bank", 0),
                          ("house", 1),
                          ("pharmacy", 0),
                          ("shop", 0),
                          ("office", 0),
                          ("police station", 0),
                          ("fire station", 0),
                          ("hospital", 0),
                          ("big apartment building", 4),
                          ("medium apartment building", 3),
                          ("small apartment building", 2),
                          ("school", 0),
                          ("kindergarten", 0))

        self.generated_map = []  # map
        self.flagB = False
        self.flagS = False  # not in yet in

    # creating a map of given size
    def create_map(self):

        for line in range(self.size_y):
            self.generated_map.append([])

            for row in range(self.size_x):

                # choose randomly type of element (street or building), higher range gives more chance to get street
                # max ratio is about 55:45 for roads
                types = random.randrange(0, 6)

                # first line of map
                if line == 0:

                    # first line can have bigger chance to get building
                    types = random.randrange(0, 4)

                    # 0-1 == building
                    if types < 2:
                        self.generated_map[line].append(Building("building", self.building_types[random.randrange(0, 13)]))

                    # 2-4 == street
                    else:
                        self.generated_map[line].append(Street("street"))

                # other lines of map
                else:

                    # 0-1 == building
                    if types < 2:

                        # row object has to be other than first
                        if row > 0:
                            if isinstance(self.generated_map[line][row-1], Building) and isinstance(self.generated_map[line-1][row], Building) and not self.flagB:
                                self.generated_map[line].append(Building("building", self.building_types[random.randrange(0, 13)]))
                                self.flagB = True
                            elif isinstance(self.generated_map[line][row-1], Building) and isinstance(self.generated_map[line-1][row], Building) and self.flagB:
                                self.generated_map[line].append(Street("street"))
                                self.flagB = False
                            else:
                                self.generated_map[line].append(Building("building", self.building_types[random.randrange(0, 13)]))

                        # first row object is independent
                        else:
                            self.generated_map[line].append(Building("building", self.building_types[random.randrange(0, 13)]))

                    # 2-4 == street
                    else:

                        # row object has to be other than first
                        if row > 0:

                            # street can only have 1 neighbour street (either up or left)...
                            if xor(bool(isinstance(self.generated_map[line][row-1], Street)), bool(isinstance(self.generated_map[line-1][row], Street))):
                                self.generated_map[line].append(Street("street"))  # ... if so, place street

                            # if street cannot be placed, try to place building
                            else:
                                if isinstance(self.generated_map[line][row - 1], Building) and isinstance(self.generated_map[line - 1][row], Building) and not self.flagB:
                                    self.generated_map[line].append(Building("suilding", self.building_types[random.randrange(0, 13)]))
                                    self.flagB = True
                                elif isinstance(self.generated_map[line][row - 1], Building) and isinstance(self.generated_map[line - 1][row], Building) and self.flagB:
                                    self.generated_map[line].append(Street("street"))
                                    self.flagB = False
                                else:
                                    self.generated_map[line].append(Building("suilding", self.building_types[random.randrange(0, 13)]))

                        # first row object is independent
                        else:
                            self.generated_map[line].append(Street("street"))
        return self.generated_map
