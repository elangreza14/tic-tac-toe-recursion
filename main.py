from math import *
from tictactoe import *


def detect_input_two():
    round = 0

    ttt = TicTacToe(
        [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ]
    )

    while True:
        if round == 9:
            print(f"finish")
            break

        input_player = input(f"round {round+1}: ")

        if input_player.isdigit():
            num = int(input_player)
            if 0 < num < 10:
                if ttt.detectCoordinateIsEmpty(num):
                    if round % 2 == 0:
                        ttt.inputAndReadData(num, "X")
                        if ttt.patternMatching("X"):
                            print("player 1 win")
                            break
                    else:
                        ttt.inputAndReadData(num, "O")
                        if ttt.patternMatching("O"):
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
    detect_input_two()


if __name__ == "__main__":
    main()
