import pygame
import random
import asyncio


async def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("TicTacToeAI")
    icon = pygame.image.load("tictactoeicon.png")
    pygame.display.set_icon(icon)

    backgroundImg = pygame.image.load("Tic-tac-toe.png")
    backgroundX = 100
    backgroundY = 0

    Xmark = pygame.image.load("mark-x.png")
    Xmark = pygame.transform.scale(Xmark, (120, 120))
    XmarkX = 140
    XmarkY = 60

    Omark = pygame.image.load("Omark.png")
    Omark = pygame.transform.scale(Omark, (120, 120))
    OmarkX = 340
    OmarkY = 60

    box_Img = pygame.image.load("buttonImg.png")
    box_Img = pygame.transform.scale(box_Img, (140, 140))

    class Button:
        def __init__(self, x, y, image):
            self.rect = image.get_rect()
            self.rect.center = (x, y)
            self.image = image
            self.mark = None

    buttons = [
        Button(200, 100, box_Img),
        Button(400, 100, box_Img),
        Button(600, 100, box_Img),
        Button(200, 300, box_Img),
        Button(400, 300, box_Img),
        Button(600, 300, box_Img),
        Button(200, 500, box_Img),
        Button(400, 500, box_Img),
        Button(600, 500, box_Img)
    ]

    current_mark = Xmark
    board = [["" for _ in range(3)] for _ in range(3)]

    def background():
        screen.blit(backgroundImg, (backgroundX, backgroundY))

    def check_win(mark):
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] == mark:
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == mark:
                return True
        if board[0][0] == board[1][1] == board[2][2] == mark:
            return True
        if board[0][2] == board[1][1] == board[2][0] == mark:
            return True
        return False

    def check_draw():
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    return False
        return True

    def ai_player_move():
        mark = Omark  # Assuming the AI player is "O"
        temp_mark = Xmark
        is_chosen = False

        # Goes over all the cases with the favor of "O" first (completing "O")
        # then blocks "X" on the second iteration
        for iteration in range(2):

            if board[1][1] == "":
                buttons[4].mark = mark
                board[1][1] = "O"
                is_chosen = True
                break

            elif board[1][1] != "":
                # Checks for the "red" case
                for i in range(3):
                    for j in range(2):
                        if (
                                board[i][j] == board[i][j + 1]
                                and board[i][j] != ""
                                and board[i][j] != temp_mark
                                and not is_chosen
                        ):
                            if j == 0 and board[i][j + 2] == "":
                                buttons[i * 3 + 2].mark = mark
                                board[i][j + 2] = "O"
                                is_chosen = True
                                break
                            elif j == 1 and board[i][0] == "":
                                buttons[i * 3].mark = mark
                                board[i][0] = "O"
                                is_chosen = True
                                break

                # Checks for the "green" case
                for i in range(2):
                    for j in range(3):
                        if (
                                board[i][j] == board[i + 1][j]
                                and board[i][j] != ""
                                and board[i][j] != temp_mark
                                and not is_chosen
                        ):
                            if i == 0 and board[i + 2][j] == "":
                                buttons[(i + 2) * 3 + j].mark = mark
                                board[i + 2][j] = "O"
                                is_chosen = True
                                break
                            elif i == 1 and board[0][j] == "":
                                buttons[j].mark = mark
                                board[0][j] = "O"
                                is_chosen = True
                                break

                if is_chosen:
                    break

                # Checks for the "black" case
                if (
                        board[0][0] == board[1][1]
                        and board[1][1] != ""
                        and board[1][1] != temp_mark
                        and board[2][2] == ""
                ):
                    buttons[8].mark = mark
                    board[2][2] = "O"
                    is_chosen = True
                    break
                elif (
                        board[0][2] == board[1][1]
                        and board[1][1] != ""
                        and board[1][1] != temp_mark
                        and board[2][0] == ""
                ):
                    buttons[6].mark = mark
                    board[2][0] = "O"
                    is_chosen = True
                    break
                elif (
                        board[2][0] == board[1][1]
                        and board[1][1] != ""
                        and board[1][1] != temp_mark
                        and board[0][2] == ""
                ):
                    buttons[2].mark = mark
                    board[0][2] = "O"
                    is_chosen = True
                    break
                elif (
                        board[2][2] == board[1][1]
                        and board[1][1] != ""
                        and board[1][1] != temp_mark
                        and board[0][0] == ""
                ):
                    buttons[0].mark = mark
                    board[0][0] = "O"
                    is_chosen = True
                    break

                # Additional conditions
                elif (
                        board[0][0] == board[0][2]
                        and board[0][0] != ""
                        and board[0][0] != temp_mark
                        and board[0][1] == ""
                ):
                    buttons[1].mark = mark
                    board[0][1] = "O"
                    is_chosen = True
                    break
                elif (
                        board[0][0] == board[2][0]
                        and board[0][0] != ""
                        and board[0][0] != temp_mark
                        and board[1][0] == ""
                ):
                    buttons[3].mark = mark
                    board[1][0] = "O"
                    is_chosen = True
                    break
                elif (
                        board[2][2] == board[0][2]
                        and board[2][2] != ""
                        and board[2][2] != temp_mark
                        and board[1][2] == ""
                ):
                    buttons[7].mark = mark
                    board[1][2] = "O"
                    is_chosen = True
                    break
                elif (
                        board[2][2] == board[2][0]
                        and board[2][2] != ""
                        and board[2][2] != temp_mark
                        and board[2][1] == ""
                ):
                    buttons[7].mark = mark
                    board[2][1] = "O"
                    is_chosen = True
                    break
                elif (
                        (board[0][0] == board[2][2] or board[2][0] == board[0][2])
                        and board[0][0] != ""
                        and board[0][0] != temp_mark
                        and board[1][1] == ""
                ):
                    buttons[4].mark = mark
                    board[1][1] = "O"
                    is_chosen = True
                    break

        # If no specific conditions are met, choose a random available button
        if not is_chosen:
            available_buttons = [button for button in buttons if not button.mark]
            if available_buttons:
                chosen_button = random.choice(available_buttons)
                chosen_button.mark = mark
                index = buttons.index(chosen_button)
                row = index // 3
                col = index % 3
                board[row][col] = "O"

    def reset_game():
        # Reset the board and button marks
        for button in buttons:
            button.mark = None
        for i in range(3):
            for j in range(3):
                board[i][j] = ""

    running = True

    while running:
        screen.fill((204, 225, 242))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(event.pos) and not button.mark:
                        button.mark = Xmark
                        index = buttons.index(button)
                        row = index // 3
                        col = index % 3
                        board[row][col] = "X"
                        ai_player_move()

        background()

        for button in buttons:
            screen.blit(button.image, button.rect)
            if button.mark:
                mark_x = button.rect.centerx - button.mark.get_width() // 2
                mark_y = button.rect.centery - button.mark.get_height() // 2
                screen.blit(button.mark, (mark_x, mark_y))

        pygame.display.update()

        await asyncio.sleep(0)
        # Check for game over conditions
        if check_win("X"):
            print("Player X wins!")
            pygame.time.delay(1000)
            reset_game()
        elif check_win("O"):
            print("Player O wins!")
            pygame.time.delay(1000)
            reset_game()
        elif check_draw():
            print("It's a draw!")
            pygame.time.delay(1000)
            reset_game()

    pygame.quit()

asyncio.run(main())
