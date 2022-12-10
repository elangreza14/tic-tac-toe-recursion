from math import *
from tictactoe import *


def detect_input_two():
    ttt = TicTacToe(
        [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ]
    )

    while True:
        if ttt.isFinished():
            print(ttt.getFinalResult())
            break

        input_player = input(f"round {ttt.getCurrentRound()}: ")

        if input_player.isdigit():
            num = int(input_player)
            if 0 < num < 10:
                ttt.run(num)
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
