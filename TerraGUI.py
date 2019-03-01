from tkinter import *
from generate_terrain import *


class Gui:
    def __init__(self):
        self.map_obj = arr
        self.size_x = len(self.map_obj[0])  # number of columns
        self.size_y = len(self.map_obj)  # number of rows
        self.window = Tk()
        self.window.title = "Terrain map Generator"

        # arrays to hold reference to PhotoImage
        self.water_pictures = []
        self.terrain_pictures = []

        # full screen ratio Y = X*0.528
        # example: 36/19, 54/28 72/38, 108/57
        if self.size_x > 70 or self.size_y > 37:
            print("size 20%")
            self.el_width = 10
            self.el_height = 10

        elif self.size_x > 36 or self.size_y > 19:
            print("size 50%")
            self.el_width = 25
            self.el_height = 25

        else:
            print("size 100%")
            self.el_width = 50
            self.el_height = 50

        self.create_map()

    def create_map(self):

        for row in range(self.size_y):

            for column in range(self.size_x):

                if isinstance(arr[row][column], Water):
                    pict = self.pick_water_element()
                    self.water_pictures.append(pict)
                    button = Button(self.window, image=self.water_pictures[len(self.water_pictures)-1],
                                    width=self.el_width, height=self.el_height, border=0)
                    button.grid(column=column, row=row)
                else:
                    pict = self.pick_terrain_element()
                    self.terrain_pictures.append(pict)
                    button = Button(self.window, image=self.terrain_pictures[len(self.terrain_pictures)-1],
                                    width=self.el_width, height=self.el_height, border=0)
                    button.grid(column=column, row=row)

        self.window.mainloop()

    def pick_water_element(self):

        pict_nr = random.randrange(1, 4)
        file_path = "img\\water\\water"+str(pict_nr)+".png"
        water_element = PhotoImage(file=file_path)

        return water_element

    def pick_terrain_element(self):

        pict_nr = random.randrange(1, 4)
        file_path = "img\\terrain\\terrain"+str(pict_nr)+".png"
        terrain_element = PhotoImage(file=file_path)

        return terrain_element


gui = Gui()
