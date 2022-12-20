import random

total_time = 0
# Make sure the total bombs is always equal or less than rows/columns
rows = columns = bombs = 10

while len(symbol := input("give a symbol: ")) != 1 or symbol.isalnum():
    continue

table2 = [[str(symbol) for q in range(columns)] for Q in range(rows)]


# stores table(input) after each iteration
def plane_list(table):
    return table2


# this function is only called once to make sure 2 or more random tables are'nt created
# noinspection PyTypeChecker
def bombs_list():
    end_it = False
    table = "*" * (bombs - 1)  # to make sure bombs are not placed in the same place.
    while not end_it and table.count("*") != bombs:
        try:
            table = [[0 for x in range(columns)] for t in range(rows)]
            row_r = [x for x in range(rows)]
            col_r = [x for x in range(columns)]
            for x in range(bombs):
                a = (random.sample(row_r, 1)).pop()
                b = (random.sample(col_r, 1)).pop()
                row_r.remove(a)
                col_r.remove(b)
                table[a][b] = "*"
                # # print(row_r,col_r)
                # top left corner
                if a == 0 and b == 0:
                    table[a][b + 1] += 1
                    table[a + 1][b] += 1
                    table[a + 1][b + 1] += 1
                # top right corner
                elif a == 0 and b == (columns - 1):
                    table[a][b - 1] += 1
                    table[a + 1][b] += 1
                    table[a + 1][b - 1] += 1
                # bottom left corner
                elif a == rows - 1 and b == 0:
                    table[a - 1][b] += 1
                    table[a][b + 1] += 1
                    table[a - 1][b + 1] += 1
                # bottom right corner
                elif a == rows - 1 and b == columns - 1:
                    table[a][b - 1] += 1
                    table[a - 1][b] += 1
                    table[a - 1][b - 1] += 1
                # centre
                elif a in range(1, rows - 1) and b in range(1, columns - 1):
                    table[a][b + 1] += 1
                    table[a][b - 1] += 1
                    table[a - 1][b] += 1
                    table[a + 1][b] += 1
                    # edges
                    table[a - 1][b - 1] += 1
                    table[a - 1][b + 1] += 1
                    table[a + 1][b - 1] += 1
                    table[a + 1][b + 1] += 1
                # left edge
                elif a in range(1, rows - 1) and b == 0:
                    table[a + 1][b] += 1
                    table[a - 1][b] += 1
                    table[a][b + 1] += 1
                    # edges
                    table[a - 1][b + 1] += 1
                    table[a + 1][b + 1] += 1
                # right edge
                elif a in range(1, rows - 1) and b == columns - 1:
                    table[a + 1][b] += 1
                    table[a - 1][b] += 1
                    table[a][b - 1] += 1
                    # edges
                    table[a - 1][b - 1] += 1
                    table[a + 1][b - 1] += 1
                # top edge
                elif a == 0 and b in range(1, columns - 1):
                    table[a][b + 1] += 1
                    table[a][b - 1] += 1
                    table[a + 1][b] += 1
                    # edges
                    table[a + 1][b - 1] += 1
                    table[a + 1][b + 1] += 1
                # bottom edge
                elif a == rows - 1 and b in range(1, columns - 1):
                    table[a][b + 1] += 1
                    table[a][b - 1] += 1
                    table[a - 1][b] += 1
                    # edges
                    table[a - 1][b - 1] += 1
                    table[a - 1][b + 1] += 1
            end_it = True
        except:
            pass
            # #print("*******")

    return table


# called once and assigned to a variable to make a mine_list object


mine_list = bombs_list()


# converts the 2D lists(in 'list' form) into an actual designed table(in 'str' form)
def table_conv(list1):
    top_row = ""
    for y in range(1, columns + 1):
        top_row += f"\t{y}\t"
    table1 = " \tC" + top_row + "\nR\t|" + ("-" * (7 * rows + rows - 1)) + "|\n"
    counter = 1
    for x in list1:
        table1 += f"{counter}\t"
        for t in x:
            table1 += f"|\t{str(t)}\t|"
        table1 += "\n\t|" + ("-" * (7 * rows + rows - 1)) + "|\n"
        counter += 1
    return table1


mine_board = table_conv(list1=mine_list)

try_ = 1


# opens up extra boxes around selected box if it has a zero


def checker(row_present=True, col_present=True, value_col=None, value_row=None):
    global inp_col, inp_row
    global table2
    try:
        while mine_list[inp_row][inp_col] == 0 and inp_row >= 0 and inp_col >= 0:
            table2[inp_row][inp_col] = mine_list[inp_row][inp_col]
            if row_present:
                inp_row += value_row
            if col_present:
                inp_col += value_col
        # if mine_list[inp_row][inp_col] == "*": pass
        if mine_list[inp_row][inp_col] != 0 and inp_row >= 0 and inp_col >= 0:
            table2[inp_row][inp_col] = mine_list[inp_row][inp_col]
    except IndexError:
        pass
    inp_col = c
    inp_row = r


def complete_checker(x=1):
    checker(value_row=x, value_col=x)  # right bottom checker
    checker(value_row=-x, value_col=-x)  # left top checker
    checker(value_row=-x, value_col=x)  # right top checker
    checker(value_row=x, value_col=-x)  # left bottom checker
    checker(value_row=x, col_present=False)  # down checker
    checker(value_row=-x, col_present=False)  # top checker
    checker(value_col=-x, row_present=False)  # left checker
    checker(value_col=x, row_present=False)  # right checker


def full_complete_checker(row_value=0, col_value=0):
    global inp_col, inp_row
    try:
        if mine_list[inp_row + row_value][inp_col + col_value] == 0:
            if row_value != 0:
                inp_row += row_value
            if col_value != 0:
                inp_col += col_value
            complete_checker()
        else:
            global total_time
            total_time += 1
            pass
    except IndexError:
        pass


# for user's beginning reference


print(table_conv(list1=table2))

# loop for game play
while True:
    # for correcting user input
    while True:
        try:
            inp_row = r = int(input("row(R): ")) - 1
            inp_col = c = int(input("column(C): ")) - 1
            while (inp_row not in range(rows)) or (inp_col not in range(columns)):
                print(f"There are only {rows} rows\nand {columns} columns[starts from 1]")
                inp_row = int(input("row(R): ")) - 1
                inp_col = int(input("column(C): ")) - 1

            break
        except ValueError:
            print(f"Dude only numbers from 1 to {columns}")

    # if else statement for checking bombs lose and continue
    if mine_list[inp_row][inp_col] == "*":
        print(mine_board)
        print("\nYOU LOSE")
        break
    else:
        table2 = plane_list(table=table2)

        # if else statement to check the presence of (non-zero) and zero (block)
        if mine_list[inp_row][inp_col] != 0:
            table2[inp_row][inp_col] = mine_list[inp_row][inp_col]
            print(table_conv(list1=table2))

        else:
            table2[inp_row][inp_col] = mine_list[inp_row][inp_col]

            complete_checker()

            print(table_conv(list1=table2))

    # if statement to check the bombs present to show did i win
    if table_conv(list1=table2).count(str(symbol)) == bombs:
        print(mine_board)
        print("\nYOU WIN")
        break

print("game over")
