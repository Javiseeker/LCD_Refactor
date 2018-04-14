#!/usr/bin/python3

#prints the top of the number
def print_top_part(number,  columns):
    if number in {'0', '2', '3', '5', '6', '7', '8', '9'}:
        print(' '+'_'*(columns-2)+' ', end=' ')
    elif number in {'1','4'}:
        print(' ' * columns, end=' ')

#prints the lines from the top to the center of the number
def print_center_up(number,  columns):
    if number in {'0', '4',  '8', '9'}:
        print('|'+' '*(columns-2) + '|', end=' ')
    elif number in {'1', '7', '3', '2'}:
        print(' ' * (columns - 1) + '|', end=' ')
    elif number in {'5', '6'}:
        print('|'+' '*(columns - 1), end=' ')
    else:
        print(' ' * columns, end=' ')

#prints the center of the number
def print_center(number, columns):
    if number in {'2', '4', '3', '5', '6', '8', '9'}:
        print(' ' + '_' * (columns - 2) + ' ', end=' ')
    elif number in {'1', '0', '7'}:
        print(' ' * columns, end=' ')


#prints the lines from the center to the bottom of the number
def print_center_down(number, columns):
    if number in {'0', '8','6'}:
        print('|'+' '*(columns-2) + '|', end=' ')
    elif number in {'1', '7', '3', '4', '5', '9'}:
        print(' ' * (columns - 1) + '|', end=' ')
    elif number in {'6'}:
        print('|'+' '*(columns - 2)+'|', end=' ')
    elif number in {'2'}:
        print('|'+' '*(columns - 1), end=' ')
    else:
        print(' ' * columns, end=' ')


#Prints the bottom of the number
def print_bottom_part(number, columns):
    if number in {'0', '2', '3', '5', '6', '8', '9'}:
        print(' ' + '_' * (columns - 2) + ' ', end=' ')
    elif number in {'4', '7','1'}:
        print(' ' * columns, end=' ')




#print_message_full prints the number in the required size.
def print_message_full(message,size, columns):
    for c in message:
        print_top_part(c,columns)
    print()

    for i in range(size):
        for c in message:
            print_center_up(c,columns)
        print()

    for c in message:
        print_center(c,columns)
    print()

    for i in range(size):
        for c in message:
            print_center_down(c, columns)
        print()

    for c in message:
        print_bottom_part(c, columns)
    print()

#arrange_variables sends the variables needed to print the number.
def arrange_variables(raw_data):
    for data in raw_data:
        section = data.split(",")
        size = int(section[0])
        columns = c_calculation(size)
        print_message_full(section[1],size,columns)


#c_calculation calculates the number of columns according to the size acquired.
def c_calculation(size):
    columns = size+2
    return columns


#Main Function where the number to print is extracted.
def main():
    c = ""
    raw_data = list()
    while c != "0,0":
        print("Enter number's size and value separated by a comma (0,0 to end process): ")
        raw_data.append(input())
        c = str(raw_data[-1])
        arrange_variables(raw_data)
        print()


if __name__ == "__main__":
    main()