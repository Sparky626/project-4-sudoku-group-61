import pygame, sys, time
from pygame.locals import QUIT
from sudoku_generator import SudokuGenerator, cell, Board, generate_sudoku


pygame.init()
clock = pygame.time.Clock()
width, height = 788,  740
backgroundColor = 255,0,0
color = 255,255,255
color_light = 0,0,0
color_dark = 100,100,100
screen = pygame.display.set_mode((width, height))
backgroundImage = pygame.image.load("pic.jpg")
easybutton = pygame.image.load("easy_button.png")
easybutton = pygame.transform.scale(easybutton, [200,37])
mediumbutton = pygame.image.load("normal_button.png")
mediumbutton = pygame.transform.scale(mediumbutton, [200,37])
hardbutton = pygame.image.load("hard_button.png")
hardbutton = pygame.transform.scale(hardbutton, [200,37])
resetbutton = pygame.image.load("reset.png")
restartbutton = pygame.image.load("restart.png")
exitbutton = pygame.image.load("exit.png")
resetbutton = pygame.transform.scale(resetbutton, [200,80])
restartbutton = pygame.transform.scale(restartbutton, [200,80])
exitbutton = pygame.transform.scale(exitbutton, [200,70])
backgroundImageRect = backgroundImage.get_rect()
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('quit' , True , color)
done = False
current_screen = 0
generated = False
clicked = True
difficulty = ""
user_text = '0'
begin = False
setup = True
empty_board = []

while done == False:
    pygame.event.get()
    pygame.display.flip()
    mouse = pygame.mouse.get_pos()
    screen.blit(backgroundImage,backgroundImageRect)
    screen.blit(easybutton, [80,450])
    screen.blit(mediumbutton, [300,450])
    screen.blit(hardbutton, [520,450])
    pygame.display.set_caption('Sudoku')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Welcome to Sudoku', True, color_light)
    textRect = [252, 60]
    screen.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render('Select Game Mode:', True, color_light)
    textRect = [160, 370]
    screen.blit(text, textRect)
    
    
    
    while setup == True:
        pygame.event.get()
        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        screen.blit(backgroundImage,backgroundImageRect)
        screen.blit(easybutton, [80,450])
        screen.blit(mediumbutton, [300,450])
        screen.blit(hardbutton, [520,450])
        pygame.display.set_caption('Sudoku')
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Welcome to Sudoku', True, color_light)
        textRect = [252, 60]
        screen.blit(text, textRect)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('Select Game Mode:', True, color_light)
        textRect = [160, 370]
        screen.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and current_screen == 0:
                mouse = pygame.mouse.get_pos()
                if 80 + 200 > mouse[0] > 80 and 37 + 450 > mouse[1] > 450:
                    current_screen = 1
                    empty_board = generate_sudoku(9, 30)
                    current_board = empty_board
                    difficulty = "easy"
                elif 300 + 200 > mouse[0] > 80 and 37 + 450 > mouse[1] > 450:
                    current_screen = 1
                    empty_board = generate_sudoku(9, 40)
                    current_board = empty_board
                    difficulty = "medium"
                elif 520 + 200 > mouse[0] > 80 and 37 + 450 > mouse[1] > 450:
                    current_screen = 1
                    empty_board = generate_sudoku(9, 50)
                    current_board = empty_board
                    difficulty = "hard"
                setup = False
            elif event.type == pygame.QUIT:
                done = True
    
    while begin == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    done = True
                    sys.exit()
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                    print(user_text)
            elif event.type == pygame.MOUSEBUTTONDOWN and current_screen == 1:
                mouse = pygame.mouse.get_pos()
                if 80 + 200 > mouse[0] > 80 and 80 + 605 > mouse[1] > 605:
                    done = True
                    sys.exit()
                elif 290 + 200 > mouse[0] > 290 and 80 + 595 > mouse[1] > 595:
                    current_board = empty_board
                    print(empty_board)
                    print(current_board)
                    begin = False
                elif 495 + 200 > mouse[0] > 495 and 80 + 600 > mouse[1] > 600:
                    if difficulty == "easy":
                        removed = 30
                    if difficulty == "medium":
                        removed = 40
                    if difficulty == "hard":
                        removed = 50
                    empty_board = generate_sudoku(9, removed)
                    current_board = empty_board
                    begin = False
                elif 120 + 538 > mouse[0] > 120 and 50 + 538 > mouse[1] > 50:
                    x = int((mouse[0]//(538/9))-1)
                    y = int(mouse[1]//(538/9))
                    rectleft = 120+(60 * (y-1))
                    recttop = 50+(60 * (x-1))
                    rectheight = 60
                    rectwidth = 60
                    if user_text == "":
                        user_text = "0"
                    print(x)
                    print(y)
                    current_board[y-1][x-1] = int(user_text)
                    begin = False
            elif event.type == pygame.QUIT:
                done = True
        
    
    if current_screen == 1:  
        screen.blit(backgroundImage,backgroundImageRect)
        board = Board(9 , 9 , screen, difficulty)    
        board.draw(current_board)
        screen.blit(exitbutton, [80, 605])
        screen.blit(resetbutton, [290, 595])
        screen.blit(restartbutton, [495, 600])
        begin = True
    elif current_screen == 2:
        screen.blit(backgroundImage,backgroundImageRect)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('Game Over!', True, color_light)
        textRect = [160, 370]
        screen.blit(text, textRect)
        screen.blit(resetbutton, [290, 595])
    elif current_screen == 3:
        screen.blit(backgroundImage,backgroundImageRect)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('You Won!', True, color_light)
        textRect = [160, 370]
        screen.blit(text, textRect)
        screen.blit(restartbutton, [290, 600])

    clock.tick(60)
	
def main():
    win = pygame.display.set_mode((788,740))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    play = True
    start = time.time()
    strikes = 0
    while play:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Good")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()
    
  

if __name__=="__main__":
    main()
  