def tic_tac_toe():
    print("\t" "+ + + + + + + + + + + + + + + + + + + + + + + + + ""\t"
      " TIC TAC TOE (X O) ""\t"
      " + + + + + + + + + + + + + + + + + + + + + + + + + ""\n")

    # board
    board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

    # display board
    def display_board():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])


    display_board()
    # check game is still going or not and store the user input

    print("# # # # # # # # # # # # # # # # # # # # # # # # ""\n"
      "\n""NOTE: Player one is X and Player two is O ""\n"
      "\n""# # # # # # # # # # # # # # # # # # # # # # # # ")
    game_going = 1
    while game_going < 10:

        def position():

            if game_going % 2 != 0:
                player = "X"
            else:
                player = "O"

            if(player == "X"):
                pos = input("enter the position from 1-9 for X:")
                pos = int(pos) - 1
                if (pos >= 9):
                    print("pls enter the correct position limit is 9")
                    pos = input("enter the position from 1-9 for X:")
                    pos = int(pos) - 1

            else:
                pos = input("enter the position from 1-9 for O:")
                pos = int(pos) - 1
                if (pos >= 9):
                    print("pls enter the correct position limit is 9")
                    pos = input("enter the position from 1-9 for O:")
                    pos = int(pos) - 1

            # check board position is fill or not
            if(board[pos] == "-"):
                board[pos] = player

            else:
                print("invalid position")
                pos = input("enter the valued position:")
                pos = int(pos) - 1
                board[pos] = player

            display_board()


            # check winner
            if (player == "X"):

                #check columns
                if (board[0] == board[3] == board[6] == "X"):
                    print("player X win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[1] == board[4] == board[7] == "X"):
                    print("player X win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[2] == board[5] == board[8] == "X"):
                    print("player X win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                #check rows
                elif (board[0] == board[1] == board[2] == "X"):
                    print("player X win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[3] == board[4] == board[5] == "X"):
                    print("player X win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[6] == board[7] == board[8] == "X"):
                    print("player X win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                #check diagonal
                elif (board[0] == board[4] == board[8] == "X"):
                    print("player X win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[2] == board[4] == board[6] == "X"):
                    print("player X win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                #check tie
                elif (game_going == 9):
                    print("its a tie!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()


                else:
                    return None

            else:
                if (board[0] == board[3] == board[6] == "O"):
                    print("player O win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[1] == board[4] == board[7] == "O"):
                    print("player O win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[2] == board[5] == board[8] == "O"):
                    print("player O win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                # check rows
                elif (board[0] == board[1] == board[2] == "O"):
                    print("player O win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[3] == board[4] == board[5] == "O"):
                    print("player O win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[6] == board[7] == board[8] == "O"):
                    print("player O win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                # check diagonal
                elif (board[0] == board[4] == board[8] == "O"):
                    print("player O win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                elif (board[2] == board[4] == board[6] == "O"):
                    print("player O win!")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()

                    exit()

                #check tie
                elif (game_going == 9):
                    print("its a tie")
                    print("if you want to play again press y or quit to press n")
                    user_choice = input()
                    if (user_choice == "y"):
                        tic_tac_toe()

                    else:
                        exit()


                else:
                    return None


        position()

        game_going = game_going + 1


tic_tac_toe()
