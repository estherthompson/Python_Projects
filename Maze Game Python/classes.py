# Importing classes from main.py
# main.py, created by Richard Zhao, is the property of the University of Calgary
# classes.py, authored by Esther Thompson, references main.py


import math
import numpy as np


class game_map:
    def __init__(self, map_file=" ", guard_file=" "):

        try:
            open_map_file = open(map_file, "r")
        except:
            print("Map file not found")
            return
        # I am opening the map file and attributing the variable texts to read the map file
        texts = open_map_file.readlines()
        # creating an empty list
        self.map = []
        # From looking at the map file, the only valid characters are #PE,
        # later I am going to makes sure that only these valid characters can be used.
        chars_valid = "#PE "
        # creating try/except block to check if map file is formatted correctly.
        try:
            # Here I am making a for loop, that will loop through the entire map file. I am using the enumerate
            # function, so that I can get the value of texts, and at each of its index. This loop represents the
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
                    if c == 'P':
                        # once the code reaches P in the map file, I create a row and col a variable's of the
                        # location of the player in the file. in this case that is row 10 and col 1
                        self.player_row = row
                        self.player_col = col
                # at the end of this for loops, text_list will be appended to the empty map list  because
                # will use it later on
                self.map.append(text_list)
            # I am using the assert function to make sure that the player row is greater than or equal to 0 because,
            # there can't be negative rows.
            assert (self.player_row >= 0)

        # After checking if the map file is formatted correctly, if it isn't it will run the except block.
        except:
            print("Map file incorrectly formatted")
            return

        open_map_file.close()

        try:
            open_guard_file = open(guard_file, "r")

        except:
            print("Guard file not found")
            return

        self.guards = []
        texts = open_guard_file.readlines()
        chars_valid = "LRUD"
        # Here I am doing a similar thing as the map file but with the guard file.
        try:
            for text in texts:
                # I am turning the string in the file into a list, so that I can find the indexes
                text = text.rstrip().split()
                # here I am finding the integer values of the row, col, att_rg at each of their index in the guard file.
                row = int(text[0])
                col = int(text[1])
                att_rg = int(text[2])
                # I will take the index of the remaining characters starting at index 3 in the list,
                # mvmt represent the direction of the guards, so this just a string.
                mvmt = text[3:]
                # here I am checking that all the characters in the mvmt list are valid characters.
                for c in mvmt:
                    assert (c in chars_valid)
                # after checking if the chars are valid and finding the index. I appended row,col,att_rg,
                # and mvmt to the empty self.guards list
                self.guards.append(guard(row, col, att_rg, mvmt))
                # I am placing G (the guard) in the correct row and column of the game map file
                self.map[row][col] = 'G'
        # if the guard file is incorrectly formatted it will run the except line
        except:
            print("Guard file incorrectly formatted")
            return
        open_guard_file.close()

    def get_grid(self):
        # here I am using the work done in the init function and just returning the map file
        return self.map

    def get_guards(self):
        # here I am using the work done in the init function and just returning the guard file
        return self.guards

    def update_player(self, direction=" "):
        # here I am creating two new variables to represent the player row and column
        new_row = self.player_row
        new_col = self.player_col
        # here i am adding a space to very end of the new row and col of the map file
        self.map[new_row][new_col] = " "
        # these if statements are based on what the player types during the game.
        if direction == "U":
            # moves player up
            new_row = new_row - 1
        elif direction == "D":
            # moves player down
            new_row = new_row + 1
            # moves player left
        elif direction == "L":
            new_col = new_col - 1
        elif direction == "R":
            # moves player right
            new_col = new_col + 1
        # this represents the number of columns and rows
        m = 12
        n = 16

        # this section makes sure that the player cannot move into the walls
        if ((0 <= new_row < m) and
                (0 <= new_col < n) and
                self.map[new_row][new_col] == ' '):
            # player will move to the new row and column
            self.player_row = new_row
            self.player_col = new_col
            # adding the player to the map file
        self.map[self.player_row][self.player_col] = "P"

    def update_guards(self):
        for g in self.guards:
            # I am equating the old row and old col of the guards using the get location function
            row_old, col_old = g.get_location()
            # the array of map at row_old and col_old to equate and empty space
            self.map[row_old][col_old] = ' '
            # not creating a new row and column and using the move function to move the guards on the map
            row_new, col_new = g.move(self.map)
            # representing G has the guard in the new row and new col
            self.map[row_new][col_new] = 'G'

    def player_wins(self):
        # when the player reaches it at the player row and col the game will return true
        return self.map[self.player_row][self.player_col] == 'E'

    def player_loses(self):
        for g in self.guards:
            # if the player ends up in the enemy range of the guards then it will return true
            if g.enemy_in_range(self.player_row, self.player_col):
                return True
        # if the player isn't in the enemy range then it will return False
        return False


class guard:

    def __init__(self, row, col, attack_range, movements):
        # these are the parameters of the init
        self.row = row
        self.col = col
        self.attack_range = attack_range
        self.movements = movements

    def get_location(self):
        # I am returning the location of the guard at the row and column
        return (self.row, self.col)

    def move(self, current_grid):

        # similar to the update player function, we make the step variable at the first index of the movements
        step = self.movements[0]
        self.movements = self.movements[1:] + [step]
        new_row = self.row
        new_col = self.col
        if step == "U":
            # moves guard up
            new_row = new_row - 1
        elif step == "D":
            # moves guard down
            new_row = new_row + 1
        elif step == "L":
            # moves guard left
            new_col = new_col - 1
        elif step == "R":
            # moves guard right
            new_col = new_col + 1

        # is total num of rows and num of columns
        num_rows, num_col = 12, 16

        # if the new_row that guard has mode in is less than the num of columns that means that the guard can move there
        if ((0 <= new_row < num_rows) and
                # if the new_col is less than the number of columns the guard can move there
                (0 <= new_col < num_col) and
                current_grid[new_row][new_col] == ' '): # I'm saying that code has to check that there nothing but
            # spaces around the guard in the current grid

            # if this is true then is will attribute self.row and self.col to new location of the guards
            self.row = new_row
            self.col = new_col

        return self.row, self.col

    def enemy_in_range(self, enemy_row, enemy_col):
        # if
        return abs(enemy_row - self.row) + abs(enemy_col - self.col) <= self.attack_range
