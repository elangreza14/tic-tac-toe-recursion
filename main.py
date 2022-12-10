from math import *

BOX = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


def searching(
    total: int, flow: str, pattern: str, box: list[list[str]], x: int, y: int
) -> int:
    # if len of pattern equal with total pattern will return
    if total == len(box):
        return len(box)

    # if position x is less than zero or
    # if position x more than equal length of x-box or
    # if position y is less than zero or
    # if position y more than equal length of y-box or
    # if box[y][x] is not equal with current pattern
    # just return zero
    if x < 0 or x >= len(box) or y < 0 or y >= len(box[x]) or box[y][x] != pattern:
        return 0

    # we're continue searching with specific flow
    match flow:
        # if flow is going to right side
        case "right":
            return searching(total + 1, flow, pattern, box, x + 1, y)
        # if flow is going to right side
        case "down":
            return searching(total + 1, flow, pattern, box, x, y + 1)
        # if flow is going to right and down side
        case "right-down":
            return searching(total + 1, flow, pattern, box, x + 1, y + 1)
        # if flow is going to left and down side
        case "left-down":
            return searching(total + 1, flow, pattern, box, x - 1, y + 1)


def pattern_matching(pattern: str) -> bool:
    # iterate through all position
    for index_y, value_y in enumerate(BOX):
        for index_x, value_x in enumerate(value_y):
            # if we find value with the same pattern
            # execute search function
            if value_y[index_x] == pattern and value_x == pattern:
                if (
                    searching(0, "right", pattern, BOX, index_x, index_y) == len(BOX)
                    or searching(0, "down", pattern, BOX, index_x, index_y) == len(BOX)
                    or searching(0, "right-down", pattern, BOX, index_x, index_y)
                    == len(BOX)
                    or searching(0, "left-down", pattern, BOX, index_x, index_y)
                    == len(BOX)
                ):
                    return True
    return False


def detect_coordinate(position: int) -> tuple[int, int]:
    y = 0
    x = 0
    # iterate position through the size of the box
    for val in range(1, position):
        # if we get the modulo if box length
        # we add x position with one
        # and reset y position back to zero
        if val % 3 == 0:
            x = x + 1
            y = 0
        # else we add new y with one 
        else:
            y = y + 1

    return x, y


def detect_coordinate_is_empty(position: int) -> bool:
    x, y = detect_coordinate(position)
    if BOX[x][y] == "-":
        return True

    return False


def print_box(position: int, char: str):
    x, y = detect_coordinate(position)

    for index_y, value_y in enumerate(BOX):
        for index_x, value_x in enumerate(value_y):
            remove_pos = value_x

            if y == index_x and x == index_y:
                BOX[x][y] = char
                remove_pos = char

            if index_x == 2:
                print(remove_pos)
            else:
                print(remove_pos, end=" ")


def detect_input():
    round = 0
    while True:
        if round == 9:
            print(f"finish")
            break

        input_player = input(f"round {round+1}: ")

        if input_player.isdigit():
            num = int(input_player)
            if 0 < num < 10:
                if detect_coordinate_is_empty(num):
                    if round % 2 == 0:
                        print_box(num, "X")
                        if pattern_matching("X"):
                            print("player 1 win")
                            break
                    else:
                        print_box(num, "O")
                        if pattern_matching("O"):
                            print("player 2 win")
                            break

                    round = round + 1
                else:
                    print(f"cannot use position")
            else:
                print(f"please input number from 1 and 9")
        else:
            print(f"please input number")


def main():
    print("welcome to tic tac toe! ")
    print("Please input number from 1 and 9! ")
    detect_input()


if __name__ == "__main__":
    main()
