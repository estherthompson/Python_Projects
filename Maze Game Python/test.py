import math
import numpy as np


# class game_map:
#     def __init__(self, map_file=" ", guard_file=" "):
# #
# try:
#     open_map_file = open("map.text", "r")
# except:
#     print("Map file not found")
#     pass
# I am opening the map file and attributing the variable texts to read the map file
open_map_file = open("map.txt", "r")
texts = open_map_file.readlines()
# creating an empty list
game_map = []
# From looking at the map file, the only valid characters are #PE,
# later I am going to makes sure that only these valid characters can be used.
chars_valid = "#PE "
# creating try/except block to check if map file is formatted correctly.
try:
    # Here I am making a for loop, that will loop through the entire map file. I am using the enumerate
    # function, so that we can get the value of texts, and at each of its index. This loop represents the
    # rows, hence why I am making it row, text in enumerate(texts), and will run for all rows.
    for row, text in enumerate(texts):
        # I'm taking the string of each row and removing whitespace characters.
        # I put the list fuction around the string, so that the string will be put into a list.
        text_list = list(text.rstrip())
        # similar as the for loop before, but instead it is taking the text_list, outputing each character at
        # their - index. this will represent the columns.
        for col, c in enumerate(text_list):
            # here I am using the assert function to check if it True that all the characters in the map are
            # valid
            assert (c in chars_valid)
            # once the code reaches P in the map file, I create a row and col a variable's of the location of
            # the player in the file. in this case that is row 10 and col 1
            if c == 'P':
                # at the end of this for loops, text_list will be appended to the empty map list  because
                # will use it later.
                player_row = row
                player_col = col
        game_map.append(text_list)
    player_row = 10
    assert (player_row >= 0)


except:
    print("Map file incorrectly formatted")
    # break

open_map_file.close()

# try:
#     open_guard_file = open(guard_file, "r")
# except:
#     pass
#     # print("Guard file not found")
#     # break

guards = []
open_guard_file = open("guards.txt", "r")
texts = open_guard_file.readlines()
chars_valid = "LRUD"
try:
    for text in texts:
        text = text.rstrip()
        row = int(text[0])  #
        col = int(text[1])  #
        att_rg = int(text[2])  #
        mvmt = text[3:]  #
        for c in mvmt:
            assert (c in chars_valid)
        guards.append(guard(row, col, att_rg, mvmt))
        game_map[row][col] = 'G'
except:
    pass
    # # print("Guard file incorrectly formatted")
    # break
open_guard_file.close()

#     def get_grid(self):
#         return self.map
#
#     def get_guards(self):
#         return self.guards
#
#     def update_player(self, direction=" "):
#         self.player_direction = direction
#         direction = " " + "U" + "D" + "L" + "R"
#         pass
#
#     def update_guards(self):
#         for g in self.guards:
#             row_old, col_old = g.get_location()
#             self.map[row_old][col_old] = ' '
#             row_new, col_new = g.move(self.map)
#             # self.map[row_old][col_old] = 'G'
#             self.map[row_new][col_new] = 'G'
#
#     def player_wins(self):
#         return self.map[self.player_row][self.player_col] == 'E'
#
#     def player_loses(self):
#         for g in self.guards:
#             if g.enemy_in_range(self.player_row, self.player_col):
#                 return True
#         return False
#
#
# class guard:
#     def __init__(self, row, col, attack_range, movements):
#         self.row = row
#         self.col = col
#         self.attack_range = attack_range
#         self.movements = movements
#
#     def get_location(self):
#         return (self.row, self.col)
#
#     def move(self,current_grid):
#
#
#
#         pass
#
#     def enemy_in_range(self, enemy_row, enemy_col):
#         return abs(enemy_row-self.row) + abs(enemy_col-self.col) <= self.attack_range
