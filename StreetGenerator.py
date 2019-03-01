import random

from operator import xor  # either operator

from Building import Building
from Street import Street


class StreetGenerator:
    def __init__(self, size_x, size_y):
        self.size_rows = size_x
        self.size_columns = size_y
        self.number_of_main_road_elements = round((size_x * size_y)/2.5)
        self.road = []
        # self.startpoint = 0

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

        self.maps = []  # map
        # self.flagB = False
        # self.flagS = False  # not in yet in
        # print("X:", self.size_rows, "Y:", self.size_columns)
        print("number of main road elements:", self.number_of_main_road_elements)
        #print("###########################")

    # creating a map of given size
    def create_map(self):

        for row in range(self.size_rows):
            self.maps.append([])

            for col in range(self.size_columns):
                self.maps[row].append(Building("building", self.building_types[random.randrange(0, 13)]))

        while self.number_of_main_road_elements != 0:
            self.generate_next_element()

        print("")
        for line in self.maps:
            for element in line:
                if isinstance(element, Building):
                    print("B", end=" ")
                elif isinstance(element, Street):
                    print(".", end=" ")
                else:
                    print("*", end=" ")
            print("")

        print("")
        # print(self.road)
        # print("")

        return self.maps

    def set_start_point(self):
        startpoint = [random.randrange(0, len(self.maps)), random.randrange(0, len(self.maps[0]))]
        generated = self.generate(startpoint)
        return generated

    def set_new_start_point(self):
        startpoint = [random.randrange(0, len(self.maps)), random.randrange(0, len(self.maps[0]))]
        generated = self.generate(startpoint)
        print("NEw Startpoint:", generated)
        return generated

    def generate_next_element(self):

        # first element
        if len(self.road) == 0:
            # print("First element")
            startpoint = self.set_start_point()
            self.maps[startpoint[0]][startpoint[1]] = Street()
            self.number_of_main_road_elements -= 1
            self.road.append(startpoint)
            print("First element:", self.road[len(self.road) - 1])
            print("Number of main road elements left:", self.number_of_main_road_elements)
            print("road:", self.road)
            print("###########################")

        # second element
        elif len(self.road) == 1:
            # print("Second element")
            last_element = [self.road[len(self.road)-1][0], self.road[len(self.road)-1][1]]
            position = self.generate(last_element)  # generate new element with last element as...
            # ...an argument

            self.number_of_main_road_elements -= 1
            self.maps[position[0]][position[1]] = Street()
            self.road.append(position)
            print("Second element:", self.road[len(self.road)-1])
            print("Number of main road elements left:", self.number_of_main_road_elements)
            print("road:", self.road)
            print("###########################")

        # other elements
        else:
            print("Other elements")
            # new_position = [self.road[len(self.road) - 1][0], self.road[len(self.road) - 1][1]]
            last_element = [self.road[len(self.road) - 1][0], self.road[len(self.road) - 1][1]]

            print("---Generating...---")
            new_position = self.generate(last_element)
            print("---Generated!!!--- POINT:", new_position)


            shuffle_counter = 0
            while new_position in self.road:
                print("Point detected in array, shuffling for ", shuffle_counter, ". time")
                last_element = [self.road[len(self.road) - 1][0], self.road[len(self.road) - 1][1]]
                new_position = self.generate(last_element)
                shuffle_counter += 1
                print("New point after shuffle is:", new_position)

                if shuffle_counter == 20:
                    print("shuffle counter reached", shuffle_counter)
                    print("Cannot shuffle more............................. Generating new starting point")

                    new_position = self.set_new_start_point()
                    while new_position in self.road:
                        new_position = self.set_new_start_point()
                    print("Starting whole new road at point:", new_position)

            print("New position:", new_position)

            self.maps[new_position[0]][new_position[1]] = Street()
            self.road.append(new_position)
            self.number_of_main_road_elements -= 1

            print("Road:", self.road)
            print("###########################")

    def generate(self, last_element):

        pos = [last_element[0], last_element[1]]  # last element of road arr

        # directions = [X-axis, Y-axis] or in other words [UP-DOWN, LEFT-RIGHT]
        directions = self.set_direction(pos)

        # 0 is left and up
        # 1 is right and down
        # 2 is none

        # print("Directions X:", directions[0], "Y:", directions[1])

        # which_way = random.randrange(1, 101)  # 0-50 = left or right, 51-100 = up or down
        # which_way = -1

        if directions[0] != 2 and directions[1] != 2:
            self.which_way = random.randrange(1, 101)  # 0-50 = left or right, 51-100 = up or down

        elif directions[0] == 2 and directions[1] != 2:
            self.which_way = 10  # 0-50 = left or right, 51-100 = up or down
            # only left or right

        elif directions[0] != 2 and directions[1] == 2:
            self.which_way = 60  # 0-50 = left or right, 51-100 = up or down
            # only up or down

        else:
            self.which_way = -1  # 0-50 = left or right, 51-100 = up or down
            # neither left, right, up, down

        # left or right
        if 0 < self.which_way < 51:

            if directions[1] == 0:
                pos[1] = pos[1] - 1
                # print("left")
            elif directions[1] == 1:
                pos[1] = pos[1] + 1
                # print("right")
            elif directions[1] == 2:
                pass
                # print("Neither left nor right 2")

        # up or down
        elif self.which_way > 50:

            if directions[0] == 0:
                pos[0] = pos[0] - 1
                # print("up")
            elif directions[0] == 1:
                pos[0] = pos[0] + 1
                # print("down")
            elif directions[0] == 2:
                pass
                # print("Neither up nor down 2")

        else:
            # print("Not possible to add new element")
            new_position = self.set_start_point()
            while new_position in self.road:
                new_position = self.set_start_point()

        return pos

    def set_direction(self, got_el):

        element = [got_el[0], got_el[1]]

        # last_element[0] = X axis (up and down)
        # last_element[1] = Y axis (left and right)

        # In results:
        # 0 is left or up
        # 1 is right or down
        # 2 is none

        # Rows (X axis - UP and DOWN) ===========================
        crash_array = self.check_for_crash(element)

        # print("crash val:", crash_array)

        # first row
        if element[0] == 0:
            up_down = 1  # only down

        # middle row
        elif 0 < element[0] < len(self.maps) - 1:


            # up and down
            if (crash_array[0] == 1) and (crash_array[1] == 0):
                # up only
                up_down = 0

            elif (crash_array[0] == 1) and (crash_array[1] == 1):
                up_down = random.randrange(0, 2)

            elif (crash_array[0] == 0) and (crash_array[1] == 1):
                # down only
                up_down = 1

            elif (crash_array[0] == 0) and (crash_array[0] == 0):
                # none
                up_down = 2

            # else:
            #     up_down = 2

        # last row
        else:
            up_down = 0  # only up

        # Columns (Y axis - LEFT and RIGHT) =====================

        # first Columns
        if element[1] == 0:
            left_right = 1  # only right

        elif 0 < element[1] < len(self.maps[0]) - 1:


            # left and right
            if (crash_array[2] == 1) and (crash_array[3] == 0):
                # left only
                left_right = 0

            elif (crash_array[2] == 1) and (crash_array[3] == 1):
                left_right = random.randrange(0, 2)

            elif (crash_array[2] == 0) and (crash_array[3] == 1):
                # right only
                left_right = 1

            elif (crash_array[2] == 0) and (crash_array[3] == 0):
                # none
                left_right = 2

            # else:
            #     left_right = 2

        # last Columns
        else:
            left_right = 0  # only left

        # 0 is left or up
        # 1 is right or down

        return [up_down, left_right]

    def check_for_crash(self, rec_el):

        element = rec_el

        left_up = 0
        left_down = 0
        right_up = 0
        right_down = 0

        frame_up = 1  # not allowed as a default
        frame_down = 1  # not allowed as a default
        frame_l = 1  # not allowed as a default
        frame_r = 1  # not allowed as a default
        frame = 1

        # 0 is ok, 1 is not ok

        # middle rows
        if len(self.maps)-1 > element[0] > 0:

            # middle columns
            if len(self.maps[0])-1 > element[1] > 0:
                # LEFT UP
                if isinstance(self.maps[element[0] - 1][element[1] - 1], Street):
                    # print("Street detected... left-UP")
                    # print("pos-:", element[0] - 1, element[1] - 1, "element:",
                    # self.maps[element[0] - 1][element[1] - 1])
                    left_up = 1

                else:
                    pass
                    # print("Left-UP accepted")

                # RIGHT UP
                if isinstance(self.maps[element[0] - 1][element[1] + 1], Street):
                    # print("Street detected...  right-UP")
                    # print("pos-:", element[0] - 1, element[1] + 1, "element:",
                    # self.maps[element[0] - 1][element[1] + 1])
                    right_up = 1

                else:
                    pass
                    # print("Right-UP accepted")

                # LEFT DOWN
                if isinstance(self.maps[element[0] + 1][element[1] - 1], Street):
                    # print("Street detected...  left-DOWN")
                    # print("pos+:", element[0] + 1, element[1] - 1, "element:",
                    # self.maps[element[0] + 1][element[1] - 1])
                    left_down = 1

                else:
                    pass
                    # print("Left-DOWN accepted")

                # RIGHT DOWN
                if isinstance(self.maps[element[0] + 1][element[1] + 1], Street):
                    # print("Street detected...  right-DOWN")
                    # print("pos+:", element[0] + 1, element[1] + 1, "element:",
                          # self.maps[element[0] + 1][element[1] + 1])
                    right_down = 1

                else:
                    pass
                    # print("Right-DOWN accepted")

            # first column in middle rows
            elif element[1] == 0:
                # print("first column in middle rows")
                left_down = 1
                left_up = 1



            # last column in middle rows
            elif element[1] == len(self.maps[0])-1:
                # print("last column in middle rows")
                right_down = 1
                right_up = 1



        # first row
        elif element[0] == 0:

            # no up allowed
            left_up = 1
            right_up = 1

            # middle columns
            if len(self.maps[0])-1 > element[1] > 0:

                # LEFT DOWN
                if isinstance(self.maps[element[0] + 1][element[1] - 1], Street):
                    # print("Star detected...  left-DOWN")
                    # print("pos+:", element[0] + 1, element[1] - 1, "element:",
                         # self.maps[element[0] + 1][element[1] - 1])
                    left_down = 1

                    frame_up = 0

                else:
                    pass
                    # print("Left-DOWN accepted")

                # RIGHT DOWN
                if isinstance(self.maps[element[0] + 1][element[1] + 1], Street):
                    # print("Star detected...  right-DOWN")
                    # print("pos+:", element[0] + 1, element[1] + 1, "element:",
                      #    self.maps[element[0] + 1][element[1] + 1])
                    right_down = 1

                    frame_up = 0

                else:
                    pass
                    # print("Right-DOWN accepted")

            # first column in first row : 0,0
            elif element[1] == 0:
                # print("first column in first rows")
                left_down = 1

                frame = 0

            # last column in first row : 0, last
            elif element[1] == len(self.maps[0]) - 1:
                # print("last column in first rows")
                right_down = 1

                frame = 0

        # last row
        elif element[0] == len(self.maps)-1:

            # no down allowed
            left_down = 1
            right_down = 1

            if len(self.maps[0])-1 > element[1] > 0:
                # LEFT UP
                if isinstance(self.maps[element[0] - 1][element[1] - 1], Street):
                    # print("Star detected... left-UP")
                    # print("pos-:", element[0] - 1, element[1] - 1, "element:",
                    # self.maps[element[0] - 1][element[1] - 1])
                    left_up = 1

                    frame_down = 0

                else:
                    frame_down = 0

                    # print("Left-UP accepted")

                # RIGHT UP
                if isinstance(self.maps[element[0] - 1][element[1] + 1], Street):
                    # print("Star detected...  right-UP")
                    # print("pos-:", element[0] - 1, element[1] + 1, "element:",
                    # self.maps[element[0] - 1][element[1] + 1])
                    right_up = 1

                    frame_down = 0

                else:
                    frame_down = 0
                    # print("Right-UP accepted")

            # first column in last row
            elif element[1] == 0:
                # print("first column in last rows")
                left_up = 1

                frame = 0


            # last column in last row
            elif element[1] == len(self.maps[0])-1:
                # print("last column in last rows")
                right_up = 1

                frame = 0


        left_return = 0
        right_return = 0
        up_return = 0
        down_return = 0

        if (left_up == 0) and (left_down == 0):
            # Left side OK
            left_return = 1

        if (right_up == 0) and (right_down == 0):
            # Right side OK
            right_return = 1

        if (left_up == 0) and (right_up == 0):
            # Up side OK
            up_return = 1

        if (left_down == 0) and (right_down == 0):
            # Down side OK
            down_return = 1

        # if (left_up == 1) and (left_down == 1) and (right_up == 1) and (right_down == 0) and (frame == 0):
        #     # point 0,0
        #     right_return = 1
        #     down_return = 1
        #
        # if (left_up == 1) and (left_down == 0) and (right_up == 1) and (right_down == 1) and (frame == 0):
        #     # point 0, last
        #     left_return = 1
        #     down_return = 1
        #
        # if (left_up == 1) and (left_down == 1) and (right_up == 0) and (right_down == 1) and (frame == 0):
        #     # point last, 0
        #     up_return = 1
        #     right_return = 1
        #
        # if (left_up == 0) and (left_down == 1) and (right_up == 1) and (right_down == 1) and (frame == 0):
        #     # point last, last
        #     up_return = 1
        #     left_return = 1
        #
        # if (left_up == 1) and (left_down == 1) and (right_up == 0) and (right_down == 1) and (frame_down == 0):
        #     # frame down - right and up
        #     up_return = 1
        #     left_return = 0
        #     right_return = 1
        #
        # if (left_up == 0) and (left_down == 1) and (right_up == 1) and (right_down == 1) and (frame_down == 0):
        #     # frame down - left and up
        #     up_return = 1
        #     left_return = 1
        #     right_return = 0
        #
        # if (left_up == 0) and (left_down == 1) and (right_up == 0) and (right_down == 1) and (frame_down == 0):
        #     # frame down - left and right and up
        #     up_return = 1
        #     left_return = 1
        #     right_return = 1

        # returned value = [up, down, left, right}
        return [up_return, down_return, left_return, right_return]

