# BOX = [
#     ["A", "B", "C"],
#     ["D", "E", "F"],
#     ["G", "H", "I"],
# ]

BOX = [
    ["O", "X", "O"],
    ["-", "X", "O"],
    ["-", "X", "-"],
]

def searching(total: int, flow: str, box: list[list[str]], x: int, y: int) -> int:
    if total == 3:
        return 3

    if x < 0 or x >= len(box) or y < 0 or y >= len(box[x]) or box[y][x] != "X":
        return 0

    match flow:
        case "a":
            return searching(total + 1, flow, box, x+1, y)
        case "b":
            return searching(total + 1, flow, box, x-1, y)
        case "c":
            return searching(total + 1, flow, box, x, y+1)
        case "d":
            return searching(total + 1, flow, box, x, y-1)
        case "e":
            return searching(total + 1, flow, box, x+1, y+1)
        case "f":
            return searching(total + 1, flow, box, x-1, y-1)
        case "g":
            return searching(total + 1, flow, box, x-1, y+1)

def pattern_matching():
    result = "lose"
    
    for index_y, value_y in enumerate(BOX):
        for index_x, value_x in enumerate(value_y):
            # print( index_x, index_y, BOX[index_x][index_y])
            if value_y[index_x] == "X" and value_x == "X":
                a = searching(0, "a", BOX, index_x, index_y)
                b = searching(0, "b", BOX, index_x, index_y)
                c = searching(0, "c", BOX, index_x, index_y)
                d = searching(0, "d", BOX, index_x, index_y)
                e = searching(0, "e", BOX, index_x, index_y)
                f = searching(0, "f", BOX, index_x, index_y)
                g = searching(0, "g", BOX, index_x, index_y)
                if (
                    a == 3
                    or b == 3
                    or c == 3
                    or d == 3
                    or e == 3
                    or f == 3
                    or g == 3
                ):
                    result = "win"

    print(result)
    


def main():
    pattern_matching()


if __name__ == "__main__":
    main()
