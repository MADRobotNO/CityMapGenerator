import random

class Building:
    def __init__(self, name, building_data):
        self.name = name
        self.building_type = building_data[0]
        self.inhabited = building_data[1]
        self.inhabitants = 0
        # self.address = address
        if self.inhabited is 1:
            self.inhabitants_generaotr(1, 8)
        if self.inhabited is 2:
            self.inhabitants_generaotr(6, 24)
        if self.inhabited is 3:
            self.inhabitants_generaotr(12, 36)
        if self.inhabited is 4:
            self.inhabitants_generaotr(18, 54)
        # print("Building", self.name, "of a type", self.building_type, "created with", self.inhabitants, "inhabitants")

    def inhabitants_generaotr(self, start, stop):
        self.inhabitants = random.randrange(start, stop)


