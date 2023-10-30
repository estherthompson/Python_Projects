from turtlesetup_plot import *

# creating a variable to ask the user how many data points they want to enter
num_point = int(input("How many points do you want to plot?"))

# creating a variable that adds number of points depending on how many points the user entered

count = 1

# create a variable to makes sure that the years are not repeated and in chronological order,
# will be important later for error checking
years_order = 0

# These are the lists made for both birth years and birth rates so that we can interpolate later
birth_years = []
birth_rates = []

# creating a boolean variable
is_error = False

if num_point <= 0:
    print("Error.")
# starting the looping statement
# we start num_point has to be greater than 0 because is while is less than or equal to 0 then no points will be plotted
else:
    while num_point > 0:
        # Here we are asking the user to input there first x coordinate.
        # With every coordinate input we convert count to string to add the strings together

        x1_coordinate = int(input("What is the x coordinate of data point" + str(count) + "?"))

        # here we are appending the birth year list, to ask the user input, so we can use later for interpolation

        birth_years.append(x1_coordinate)

        # We know that all x coordinates must be inbetween years 1910 and 2022

        # so the x coordinate must be greater than 1920 and less than 2022 or the while loop breaks
        if x1_coordinate < 1910:
            print("Error.")
            # making the error checking, have boolean value to equal true so that if code breaks
            # it will stop
            is_error = True
            break
        elif x1_coordinate > 2022:
            print("Error.")
            is_error = True
            break
        # here where we bring back years_order, when the loop runs for the first time it will ignore this statement
        # after it runs the years_order = x1_coordinate will make a new x coordinate, so if x coordinate is less than
        # or equal the code will break, making sure that it runs in chronlogical order and no repetition
        elif x1_coordinate <= years_order:
            print("Error.")
            is_error = True
            break

        else:

            # now we are going to asking the user for the y-coordinate, place it in the else statement because after
            # it goes through error checking we can now start plotting

            y1_coordinate = float(input("What is the y coordinate of data point" + str(count) + "?"))

            # appending the list for birth rates

            birth_rates.append(y1_coordinate)

            # just like checking the years, we are also making sure that y values are between 0.2 and 4.5
            if y1_coordinate < 0.2:
                print("Error.")
                is_error = True
                break
            if y1_coordinate > 4.5:
                print("Error.")
                is_error = True
                break

            # Here were rounding y1_coordinate to the second decimal
            round_point = round(y1_coordinate, 2)
            # after running the loop for first time we equal years_order = x1_coordinate so that when it reruns that
            # loop it, compares the last x1_coordinate to makes sure it is chronlogical or doesn't repeat
        years_order = x1_coordinate

        # we are making the num_point subtract everytime so that it only loops the exact amount the user inputs
        num_point = num_point - 1
        # count is making the code at number to end when code ask at the end of every point
        count += 1
        # asking turtle to go to the x and y coordinates that the user inputted
        t.speed(0)
        t.goto(x1_coordinate, y1_coordinate)
        # drawing data markers
        t.down()
        t.forward(-0.4)
        t.left(90)
        t.forward(0.04)
        t.left(90)
        t.forward(-0.4)
        t.left(90)
        t.forward(0.04)
        t.left(90)
        t.up()
        t.goto(x1_coordinate, y1_coordinate)
        t.down()

    t.hideturtle()

    # basically saying that when every boolean equals false it will run this if statement

    if not is_error:
        # starting the interpolation
        x1_year_start = int(input("Which year would you like to start with?"))
        x2_year_end = int(input("Which year would you like to end with?"))
        # creating statements to makes sure that enter data points are in the lost

        if x1_year_start not in birth_years:
            print("The entered data point does not exist.")
        if x2_year_end not in birth_years:
            print("The entered data point does not exist.")

        else:
            # making the range the values that the user entered, adding 1 so that it doesn't start at 160
            # creating for loop so that it loop in the ranger user inputted
            for i in range(x1_year_start + 1, x2_year_end):
                # we are making variable for the index to find where the first year position is the list
                years_start = birth_years.index(x1_year_start)
                # making second  variable for index to find for the end of the year's position
                years_end = birth_years.index(x2_year_end)
                # this is the beginning of the interpolation formula representing y1
                beginning_interpolation = (birth_rates[years_start])
                # this is the end of the interpolation formula representing (x-x1) * (y2-y1)/(x2 - x1)
                middle_interpolation = (i - x1_year_start)
                end_interpolation = (birth_rates[years_end] - birth_rates[years_start]) / (x2_year_end - x1_year_start)
                # combing both the beginning and end of the interpolation to have the complete formula
                y_interpolation_data = beginning_interpolation + (middle_interpolation * end_interpolation)
                # rounding the interpolation data
                rounded_interpolation = float("% .2f" % y_interpolation_data)
                # printing the years and interpolation
                print(i, "", rounded_interpolation)

                # asking turtle to go to new x and y coordinates that the user inputted

                t.up()
                t.goto(i, rounded_interpolation)
                # drawing a square
                t.down()
                t.forward(-0.4)
                t.left(90)
                t.forward(0.04)
                t.left(90)
                t.forward(-0.4)
                t.left(90)
                t.forward(0.04)
                t.left(90)
                t.up()
                t.goto(i, rounded_interpolation)
                t.down()
screen.exitonclick()
