from tkinter import *
from Building import Building
from Street import Street

class Gui:
    def __init__(self, map_obj):
        self.map_obj = map_obj
        self.size_x = len(map_obj[0])  # number of columns
        self.size_y = len(map_obj)  # number of rows
        self.window = Tk()
        self.window.title = "City Map Generator"

        # arrays to hold reference to PhotoImage
        self.street_pictures = []
        self.buildings_pictures = []

    def create_map(self):

        for row in range(self.size_y):

            for column in range(self.size_x):
                r = 0
                l = 0
                u = 0
                d = 0

                # first row
                if row == 0:

                    u = 0

                    # building
                    if isinstance(self.map_obj[row][column], Building):

                        self.buildings_pictures.append(self.pick_building_type(self.map_obj[row][column].building_type))

                        button = Button(self.window, image=self.buildings_pictures[len(self.buildings_pictures)-1], width=50, height=50, border=0)
                        button.grid(column=column, row=row)

                    # street
                    else:

                        # first column
                        if column == 0:
                            l = 0

                            if isinstance(self.map_obj[row][column + 1], Street):
                                r = 1
                            if isinstance(self.map_obj[row+1][column], Street):
                                d = 1

                        # other columns
                        elif self.size_x-1 > column > 0:

                            if isinstance(self.map_obj[row][column - 1], Street):
                                l = 1
                            if isinstance(self.map_obj[row][column + 1], Street):
                                r = 1
                            if isinstance(self.map_obj[row+1][column], Street):
                                d = 1

                        # last column
                        else:

                            r = 0
                            if isinstance(self.map_obj[row][column - 1], Street):
                                l = 1
                            if isinstance(self.map_obj[row+1][column], Street):
                                d = 1

                        self.street_pictures.append(self.pick_street_element(l, r, u, d))

                        button = Button(self.window, image=self.street_pictures[len(self.street_pictures)-1], width=50, height=50, border=0)
                        button.grid(column=column, row=row)

                # other rows
                elif self.size_y - 1 > row > 0:

                    # building
                    if isinstance(self.map_obj[row][column], Building):

                        self.buildings_pictures.append(self.pick_building_type(self.map_obj[row][column].building_type))

                        button = Button(self.window, image=self.buildings_pictures[len(self.buildings_pictures)-1], width=50, height=50, border=0)
                        button.grid(column=column, row=row)

                    # street
                    else:

                        # first column
                        if column == 0:
                            l = 0
                            if isinstance(self.map_obj[row][column + 1], Street):
                                r = 1
                            if isinstance(self.map_obj[row+1][column], Street):
                                d = 1
                            if isinstance(self.map_obj[row-1][column], Street):
                                u = 1

                        # other columns
                        elif self.size_x-1 > column > 0:

                            if isinstance(self.map_obj[row][column - 1], Street):
                                l = 1
                            if isinstance(self.map_obj[row][column + 1], Street):
                                r = 1
                            if isinstance(self.map_obj[row+1][column], Street):
                                d = 1
                            if isinstance(self.map_obj[row-1][column], Street):
                                u = 1

                        # last column
                        else:

                            r = 0
                            if isinstance(self.map_obj[row][column - 1], Street):
                                l = 1
                            if isinstance(self.map_obj[row+1][column], Street):
                                d = 1
                            if isinstance(self.map_obj[row-1][column], Street):
                                u = 1

                        self.street_pictures.append(self.pick_street_element(l, r, u, d))

                        button = Button(self.window, image=self.street_pictures[len(self.street_pictures)-1], width=50, height=50, border=0)
                        button.grid(column=column, row=row)

                # last row
                else:

                    # building
                    if isinstance(self.map_obj[row][column], Building):

                        self.buildings_pictures.append(self.pick_building_type(self.map_obj[row][column].building_type))

                        button = Button(self.window, image=self.buildings_pictures[len(self.buildings_pictures)-1], width=50, height=50, border=0)
                        button.grid(column=column, row=row)

                    # street
                    else:

                        # first column
                        if column == 0:
                            l = 0
                            d = 0
                            if isinstance(self.map_obj[row][column + 1], Street):
                                r = 1
                            if isinstance(self.map_obj[row - 1][column], Street):
                                u = 1

                        # other columns
                        elif self.size_x - 1 > column > 0:
                            d = 0
                            if isinstance(self.map_obj[row][column - 1], Street):
                                l = 1
                            if isinstance(self.map_obj[row][column + 1], Street):
                                r = 1
                            if isinstance(self.map_obj[row - 1][column], Street):
                                u = 1

                        # last column
                        else:
                            r = 0
                            d = 0
                            if isinstance(self.map_obj[row][column - 1], Street):
                                l = 1
                            if isinstance(self.map_obj[row - 1][column], Street):
                                u = 1

                        self.street_pictures.append(self.pick_street_element(l, r, u, d))

                        button = Button(self.window, image=self.street_pictures[len(self.street_pictures)-1], width=50, height=50, border=0)
                        button.grid(column=column, row=row)

        self.window.mainloop()

    def pick_street_element(self, l, r, u, d):

        street_element = PhotoImage()

        if l == 0 and r == 0 and u == 0 and d == 0:
            street_element = PhotoImage(file="img\street\streetRound.png")

        elif l == 1 and r == 1 and u == 1 and d == 1:
            street_element = PhotoImage(file="img\street\streetCross.png")

        elif l == 0 and r == 0 and u == 1 and d == 1:
            street_element = PhotoImage(file="img\street\streetUpDown.png")

        elif l == 1 and r == 1 and u == 0 and d == 0:
            street_element = PhotoImage(file="img\street\streetLR.png")

        elif l == 0 and r == 1 and u == 1 and d == 1:
            street_element = PhotoImage(file="img\street\streetUDR.png")

        elif l == 1 and r == 0 and u == 1 and d == 1:
            street_element = PhotoImage(file="img\street\streetUDL.png")

        elif l == 1 and r == 1 and u == 1 and d == 0:
            street_element = PhotoImage(file="img\street\streetULR.png")

        elif l == 1 and r == 1 and u == 0 and d == 1:
            street_element = PhotoImage(file="img\street\streetDLR.png")

        elif l == 1 and r == 0 and u == 1 and d == 0:
            street_element = PhotoImage(file="img\street\streetUL.png")

        elif l == 0 and r == 1 and u == 1 and d == 0:
            street_element = PhotoImage(file="img\street\streetUR.png")

        elif l == 1 and r == 0 and u == 0 and d == 1:
            street_element = PhotoImage(file="img\street\streetDL.png")

        elif l == 0 and r == 1 and u == 0 and d == 1:
            street_element = PhotoImage(file="img\street\streetDR.png")

        elif l == 0 and r == 0 and u == 1 and d == 0:
            street_element = PhotoImage(file="img\street\streetUEnd.png")

        elif l == 0 and r == 0 and u == 0 and d == 1:
            street_element = PhotoImage(file="img\street\streetDEnd.png")

        elif l == 1 and r == 0 and u == 0 and d == 0:
            street_element = PhotoImage(file="img\street\streetLEnd.png")

        elif l == 0 and r == 1 and u == 0 and d == 0:
            street_element = PhotoImage(file="img\street\streetREnd.png")

        return street_element

    def pick_building_type(self, building):

        building_icon = PhotoImage()

        if building == "bank":
            building_icon = PhotoImage(file="img\\buildings\\bank.png")

        elif building == "house":
            building_icon = PhotoImage(file="img\\buildings\house.png")

        elif building == "pharmacy":
            building_icon = PhotoImage(file="img\\buildings\pharmacy.png")

        elif building == "shop":
            building_icon = PhotoImage(file="img\\buildings\shop.png")

        elif building == "office":
            building_icon = PhotoImage(file="img\\buildings\office.png")

        elif building == "police station":
            building_icon = PhotoImage(file="img\\buildings\police.png")

        elif building == "fire station":
            building_icon = PhotoImage(file="img\\buildings\\fire.png")

        elif building == "hospital":
            building_icon = PhotoImage(file="img\\buildings\hospital.png")

        elif building == "big apartment building":
            building_icon = PhotoImage(file="img\\buildings\\buildingHigh.png")

        elif building == "medium apartment building":
            building_icon = PhotoImage(file="img\\buildings\\buildingMedium.png")

        elif building == "small apartment building":
            building_icon = PhotoImage(file="img\\buildings\\buildingSmall.png")

        elif building == "school":
            building_icon = PhotoImage(file="img\\buildings\school.png")

        elif building == "kindergarten":
            building_icon = PhotoImage(file="img\\buildings\kindergarten.png")

        return building_icon
