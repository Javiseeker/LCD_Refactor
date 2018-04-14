def print_upper_part(number,  columns):
    if number in {'0', '2', '3', '5', '6', '7', '8', '9'}:
        print(' '+'_'*(columns-2)+' ', end=' ')
    elif number in {'1','4'}:
        print(' ' * columns, end=' ')


def print_center_up(number,  columns):
    if number in {'0', '4',  '8', '9'}:
        print('|'+' '*(columns-2) + '|', end=' ')
    elif number in {'1', '7', '3', '2'}:
        print(' ' * (columns - 1) + '|', end=' ')
    elif number in {'5', '6'}:
        print('|'+' '*(columns - 1), end=' ')
    else:
        print(' ' * columns, end=' ')


def print_center(number, columns):
    if number in {'2', '4', '3', '5', '6', '8', '9'}:
        print(' ' + '_' * (columns - 2) + ' ', end=' ')
    elif number in {'1', '0', '7'}:
        print(' ' * columns, end=' ')



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



def print_bottom_part(number, columns):
    if number in {'0', '2', '3', '5', '6', '8', '9'}:
        print(' ' + '_' * (columns - 2) + ' ', end=' ')
    elif number in {'4', '7','1'}:
        print(' ' * columns, end=' ')





def print_message_full(message,size, columns):
    for c in message :
        print_upper_part(c,columns)
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


def print_lcd(raw_data):
    for data in raw_data:
        section = data.split(",")
        size = int(section[0])
        rows, columns = rc_selection(size)
        print_message_full(section[1],size,columns)



def rc_selection(size):
    rows = 2*size+3
    columns = size+2
    return rows, columns


def main():
    c = ""
    raw_data = list()
    while c != "0,0":
        print("Enter number's size and value separated by a comma (0,0 to end process): ")
        raw_data.append(input())
        c = str(raw_data[-1])
        print_lcd(raw_data)
        print()


if __name__ == "__main__":
    main()