result_state = {
    "ONE": "The Winner is Player One",
    "TWO": "The Winner is Player Two",
    "DRAW": "The Match is Draw",
}


class TicTacToe:
    def __init__(self, box: list[list[str]]):
        self.box: list[list[str]] = box
        self.__len_x = len(box[0])
        self.__total_round = 0
        self.__winner = result_state.get("DRAW")

    def __detect_coordinate(self, position: int) -> tuple[int, int]:
        y = 0
        x = 0
        # iterate position through the size of the box
        for val in range(1, position):
            # if we get the modulo if box length
            # we add x position with one
            # and reset y position back to zero
            if val % self.__len_x == 0:
                x = x + 1
                y = 0
            # else we add new y with one
            else:
                y = y + 1

        # just return coordinate
        return x, y

    def __input_and_read_data(self, position: int, char: str):
        # transform position into coordinate
        x, y = self.__detect_coordinate(position)

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
                if index_x == (self.__len_x - 1):
                    print(remove_pos)
                # otherwise just separate with space
                else:
                    print(remove_pos, end=" ")

    def __detect_coordinate_is_empty(self, position: int) -> bool:
        # transform position into coordinate
        x, y = self.__detect_coordinate(position)
        # detect if position is filled or not
        if self.box[x][y] == "-":
            return True

        # just return false
        return False

    def __checking_pattern(self, total: int, flow: str, pattern: str, x: int, y: int) -> int:
        # if len of pattern equal with total pattern will return
        if total == self.__len_x:
            return self.__len_x

        # if position x is less than zero or
        # if position x more than equal length of x-box or
        # if position y is less than zero or
        # if position y more than equal length of y-box or
        # if box[y][x] is not equal with current pattern
        # just return zero
        if x < 0 or x >= self.__len_x or y < 0 or y >= len(self.box[x]) or self.box[y][x] != pattern:
            return 0

        # we're continue searching with specific flow
        # and adding total with one
        # since we're still searching until reach final total
        match flow:
            # if flow is going to right side
            case "right":
                x = x + 1
            # if flow is going to right side
            case "down":
                y = y + 1
            # if flow is going to right and down side
            case "right-down":
                x = x + 1
                y = y + 1
            # if flow is going to left and down side
            case "left-down":
                x = x - 1
                y = y + 1

        # continue running recursion
        return self.__checking_pattern(total + 1, flow, pattern, x, y)

    def __pattern_matching(self, pattern: str) -> bool:
        # iterate through all position
        for index_y, value_y in enumerate(self.box):
            for index_x, value_x in enumerate(value_y):
                # if we find value with the same pattern
                # execute search function
                if value_y[index_x] == pattern and value_x == pattern:
                    for flow in ["right", "right-down", "down", "left-down"]:
                        if self.__checking_pattern(0, flow, pattern, index_x, index_y) == self.__len_x:
                            return True

        return False

    def is_finished(self) -> bool:
        if self.__winner != result_state.get("DRAW") or self.__total_round == 9:
            return True
        return False

    def get_current_round(self) -> int:
        return self.__total_round + 1

    def get_final_result(self) -> str:
        if self.is_finished():
            return self.__winner
        return "Match Still Running"

    def run(self, num: int):
        if self.__detect_coordinate_is_empty(num):
            if self.__total_round % 2 == 0:
                self.__input_and_read_data(num, "X")
                if self.__pattern_matching("X"):
                    self.__winner = result_state.get("ONE")
            else:
                self.__input_and_read_data(num, "O")
                if self.__pattern_matching("O"):
                    self.__winner = result_state.get("TWO")

            self.__total_round = self.__total_round + 1
        else:
            print(f"cannot use position")
