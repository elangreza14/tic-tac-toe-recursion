from tictactoe import TicTacToe


def detect_input_two():
    ttt = TicTacToe(
        [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ]
    )

    while True:
        if ttt.is_finished():
            print(ttt.get_final_result())
            break

        input_player = input(f"round {ttt.get_current_round()}: ")

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
