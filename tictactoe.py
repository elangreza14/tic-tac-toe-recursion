class TicTacToe:
    def __init__(self, box: list[list[str]]):
        self.box: list[list[str]] = box
        self.len_x = len(box[0])
        # self.is_win: bool = False
        # self.total_round: int = 0

    def detectCoordinate(self, position: int):
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

    def inputAndReadData(self, position: int, char: str):
        # transform position into coordinate
        x, y = self.detectCoordinate(position)

        # iterate through cell
        for index_y, value_y in enumerate(self.box):
            for index_x, value_x in enumerate(value_y):
                remove_pos = value_x

                # if cell is found
                # replace with the char
                if y == index_x and x == index_y:
                    self.box[x][y] = char
                    remove_pos = char

                # if index x is same with size of x
                # just print new line
                if index_x == (self.len_x - 1):
                    print(remove_pos)
                # otherwise just separate with space
                else:
                    print(remove_pos, end=" ")

    def detectCoordinateIsEmpty(self, position: int) -> bool:
        # transform position into coordinate
        x, y = self.detectCoordinate(position)
        # detect if position is filled or not
        if self.box[x][y] == "-":
            return True

        return False

    def checkingPattern(
        self, total: int, flow: str, pattern: str, x: int, y: int
    ) -> int:
        # if len of pattern equal with total pattern will return
        if total == self.len_x:
            return self.len_x

        # if position x is less than zero or
        # if position x more than equal length of x-box or
        # if position y is less than zero or
        # if position y more than equal length of y-box or
        # if box[y][x] is not equal with current pattern
        # just return zero
        if (
            x < 0
            or x >= self.len_x
            or y < 0
            or y >= len(self.box[x])
            or self.box[y][x] != pattern
        ):
            return 0

        # we're continue searching with specific flow
        # and adding total with one
        # since we're still searching until reach
        # total equal length of box
        match flow:
            # if flow is going to right side
            case "right":
                return self.checkingPattern(total + 1, flow, pattern, x + 1, y)
            # if flow is going to right side
            case "down":
                return self.checkingPattern(total + 1, flow, pattern, x, y + 1)
            # if flow is going to right and down side
            case "right-down":
                return self.checkingPattern(total + 1, flow, pattern, x + 1, y + 1)
            # if flow is going to left and down side
            case "left-down":
                return self.checkingPattern(total + 1, flow, pattern, x - 1, y + 1)

    def patternMatching(self, pattern: str) -> bool:
        # iterate through all position
        for index_y, value_y in enumerate(self.box):
            for index_x, value_x in enumerate(value_y):
                # if we find value with the same pattern
                # execute search function
                if value_y[index_x] == pattern and value_x == pattern:
                    if (
                        self.checkingPattern(0, "right", pattern, index_x, index_y)
                        == self.len_x
                        or self.checkingPattern(0, "down", pattern, index_x, index_y)
                        == self.len_x
                        or self.checkingPattern(
                            0, "right-down", pattern, index_x, index_y
                        )
                        == self.len_x
                        or self.checkingPattern(
                            0, "left-down", pattern, index_x, index_y
                        )
                        == self.len_x
                    ):
                        return True
        return False
