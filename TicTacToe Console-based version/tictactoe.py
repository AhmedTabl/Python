import random

isGame = True
player = 1

print("----------------Welcome to Tic-Tac-Toe!------------\n")
print("      |       |\n"
      "  1   |   2   |  3 "
      "\n______|_______|________\n"
      "      |       |    \n"
      "   4  |   5   |  6\n"
      "______|_______|________\n"
      "      |       |     \n"
      "   7  |   8   |  9 \n      |       |     \n")

inputarray = [[" "," "," "],[" "," "," "],[" "," "," "]]


while isGame:

    mark = 'x'
    if player == 1:
        mark = 'x'
    elif player == 2:
        mark = 'o'

    print("\n\nPlayer" + str(player) + "'s turn\n")


    if player == 1:
        print("Which box do you want to use(1-9):")
        box = int(input(""))

        validBox = False
        while validBox == False:
            if box == 1 and inputarray[0][0] == " ":

                inputarray[0][0] = mark
                validBox = True

            elif box == 2 and inputarray[0][1] == " ":
                inputarray[0][1] = mark
                validBox = True

            elif box == 3 and inputarray[0][2] == " ":
                inputarray[0][2] = mark
                validBox = True

            elif box == 4 and inputarray[1][0] == " ":
                inputarray[1][0] = mark
                validBox = True

            elif box == 5 and inputarray[1][1] == " ":
                inputarray[1][1] = mark
                validBox = True

            elif box == 6 and inputarray[1][2] == " ":

                inputarray[1][2] = mark
                validBox = True

            elif box == 7 and inputarray[2][0] == " ":

                inputarray[2][0] = mark
                validBox = True

            elif box == 8 and inputarray[2][1] == " ":

                inputarray[2][1] = mark
                validBox = True

            elif box == 9 and inputarray[2][2] == " ":

                inputarray[2][2] = mark
                validBox = True

            else:
                print("Invalid box! Try again.")
                validBox = False
                box = int(input(""))

    elif player == 2:

        tempMark = "x"
        isChosen = False  # Determines if one of the for-loops(for the red and green cases) has chosen a square

        # Goes over all the cases with the favor of "o" first(meaning it picks the squares that complete "o" first) then blocks "x" on the second iteration
        for iter in range(2):

            if inputarray[1][1] == " ":

                inputarray[1][1] = mark
                break

            elif inputarray[1][1] != " ":

                #Checks for the "red" case of input (look at the misc onenote)
                for i in range(3):
                    for j in range(2):
                        if (inputarray[i][j] == inputarray[i][j+1]) and (inputarray[i][j] != " ") and (inputarray[i][j] != tempMark) and isChosen == False:
                            if j == 0 and inputarray[i][j+2] == " ":
                                inputarray[i][j+2] = mark
                                isChosen = True
                                break
                            elif j == 1 and inputarray[i][0] == " ":
                                inputarray[i][0] = mark
                                isChosen = True
                                break

                # Checks for the "green" case of input (look at the misc onenote)
                for i in range(2):
                     for j in range(3):
                        if (inputarray[i][j] == inputarray[i+1][j]) and (inputarray[i][j] != " ") and (inputarray[i][j] != tempMark) and isChosen == False:
                            if i == 0 and inputarray[i+2][j] == " ":
                                inputarray[i+2][j] = mark
                                isChosen = True
                                break
                            elif i == 1 and inputarray[0][j] == " ":
                                inputarray[0][j] = mark
                                isChosen = True
                                break

                if isChosen == True:
                    break

                # Checks for "black" case of input (look at the misc onenote)
                if (inputarray[0][0] == inputarray[1][1]) and (inputarray[1][1] != " ") and (inputarray[1][1] != tempMark) and inputarray[2][2] == " ":
                    inputarray[2][2] = mark
                    isChosen = True
                    break

                elif (inputarray[0][2] == inputarray[1][1]) and (inputarray[1][1] != " ") and (inputarray[1][1] != tempMark) and inputarray[2][0] == " ":
                    inputarray[2][0] = mark
                    isChosen = True
                    break
                elif (inputarray[2][0] == inputarray[1][1]) and (inputarray[1][1] != " ") and (inputarray[1][1] != tempMark) and inputarray[0][2] == " ":
                    inputarray[0][2] = mark
                    isChosen = True
                    break
                elif (inputarray[2][2] == inputarray[1][1]) and (inputarray[1][1] != " ") and (inputarray[1][1] != tempMark) and inputarray[0][0] == " ":
                    inputarray[0][0] = mark
                    isChosen = True
                    break

                # Middle-Empty cases within the "black" cases
                elif (inputarray[0][0] == inputarray[0][2]) and (inputarray[0][0] != " ") and (inputarray[0][0] != tempMark) and inputarray[0][1] == " ":
                    inputarray[0][1] = mark
                    isChosen = True
                    break
                elif (inputarray[0][0] == inputarray[2][0]) and (inputarray[0][0] != " ") and (inputarray[0][0] != tempMark) and inputarray[1][0] == " ":
                    inputarray[1][0] = mark
                    isChosen = True
                    break

                elif (inputarray[2][2] == inputarray[0][2]) and (inputarray[2][2] != " ") and (inputarray[2][2] != tempMark) and inputarray[1][2] == " ":
                    inputarray[1][2] = mark
                    isChosen = True
                    break
                elif (inputarray[2][2] == inputarray[2][0]) and (inputarray[2][2] != " ") and (inputarray[2][2] != tempMark) and inputarray[2][1] == " ":
                    inputarray[2][1] = mark
                    isChosen = True
                    break

                elif ((inputarray[0][0] == inputarray[2][2]) or (inputarray[2][0] == inputarray[0][2])) and (inputarray[0][0] != " ") and (inputarray[0][0] != tempMark) and inputarray[1][1] == " ":
                    inputarray[1][1] = mark
                    isChosen = True
                    break

                tempMark = "o"

            # If none of the cases are available, play a random empty square
            if iter == 1 and isChosen == False:

                emptySquares = []  # Stores the coordinates of the empty squares available

                for i in range(3):
                    for j in range(3):
                        if inputarray[i][j] == " ":
                            emptySquares.append((i, j))

                randSquare = random.choice(emptySquares)

                inputarray[randSquare[0]][randSquare[1]] = mark  # Plays the mark at the random empty square coordinates


    # Prints out the updated game stage
    print("      |       |\n"
          "  "+inputarray[0][0]+"   |   "+inputarray[0][1]+"   |  "+inputarray[0][2] +" "
          "\n______|_______|________\n"
          "      |       |    \n"
          "   "+inputarray[1][0]+"  |   "+inputarray[1][1] +"   |  "+ inputarray[1][2]+"\n"
          "______|_______|________\n"
          "      |       |     \n"
          "   "+ inputarray[2][0]+"  |   "+inputarray[2][1]+"   |  "+ inputarray[2][2]+" \n      |       |     \n")

    # Checks for win or draw
    if (inputarray[0][0] == inputarray[0][1] and inputarray[0][0] == inputarray[0][2] and inputarray[0][0] != " ") or (
            inputarray[1][0] == inputarray[1][1] and inputarray[1][0] == inputarray[1][2] and inputarray[1][0] != " ") or (
            inputarray[2][0] == inputarray[2][1] and inputarray[2][0] == inputarray[2][2] and inputarray[2][0] != " ") or (
            inputarray[0][0] == inputarray[1][0] and inputarray[0][0] == inputarray[2][0] and inputarray[0][0] != " ")  or (
            inputarray[0][1] == inputarray[1][1] and inputarray[0][1] == inputarray[2][1] and inputarray[0][1] != " ") or (
            inputarray[0][2] == inputarray[1][2] and inputarray[0][2] == inputarray[2][2] and inputarray[0][2] != " ") or (
            inputarray[0][0] == inputarray[1][1] and inputarray[0][0] == inputarray[2][2] and inputarray[0][0] != " ") or (
            inputarray[0][2] == inputarray[1][1] and inputarray[0][2] == inputarray[2][0] and inputarray[0][2] != " "):
        isGame = False
        print("\n\nPlayer" + str(player) + " wins!")

    else:

        fill = 0 # indicates the number of filled boxes
        for i in inputarray:
            for j in i:
                if (j == "x") or (j == "o"):
                    fill += 1

        if fill == 9:
            isGame = False
            print("\n\nIt's a Draw!")
        else:
            if player == 1:
                player = 2
            elif player == 2:
                player = 1
