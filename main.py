from math import *

BOX = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


def searching(
    total: int, flow: str, pattern: str, box: list[list[str]], x: int, y: int
) -> int:
    if total == 3:
        return 3

    if x < 0 or x >= len(box) or y < 0 or y >= len(box[x]) or box[y][x] != pattern:
        return 0

    match flow:
        case "a":
            return searching(total + 1, flow, pattern, box, x + 1, y)
        case "b":
            return searching(total + 1, flow, pattern, box, x - 1, y)
        case "c":
            return searching(total + 1, flow, pattern, box, x, y + 1)
        case "d":
            return searching(total + 1, flow, pattern, box, x, y - 1)
        case "e":
            return searching(total + 1, flow, pattern, box, x + 1, y + 1)
        case "f":
            return searching(total + 1, flow, pattern, box, x - 1, y - 1)
        case "g":
            return searching(total + 1, flow, pattern, box, x - 1, y + 1)


def pattern_matching(pattern: str) -> bool:
    for index_y, value_y in enumerate(BOX):
        for index_x, value_x in enumerate(value_y):
            if value_y[index_x] == pattern and value_x == pattern:
                a = searching(0, "a", pattern, BOX, index_x, index_y)
                b = searching(0, "b", pattern, BOX, index_x, index_y)
                c = searching(0, "c", pattern, BOX, index_x, index_y)
                d = searching(0, "d", pattern, BOX, index_x, index_y)
                e = searching(0, "e", pattern, BOX, index_x, index_y)
                f = searching(0, "f", pattern, BOX, index_x, index_y)
                g = searching(0, "g", pattern, BOX, index_x, index_y)
                if a == 3 or b == 3 or c == 3 or d == 3 or e == 3 or f == 3 or g == 3:
                    return True
    return False


def detect_coordinate(position: int) -> tuple[int, int]:
    y = 0
    x = 0
    for val in range(1, position):
        if val % 3 == 0:
            x = x + 1
            y = 0
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
