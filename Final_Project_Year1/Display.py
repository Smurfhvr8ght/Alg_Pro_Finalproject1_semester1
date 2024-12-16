import pygame
import pygame.freetype
from Classes import Sudoku
from Database import Data
from number_asset import num_array_list

pygame.init()

#icon
icon = pygame.image.load(r'Final_Project_Year1/Asset/grid.png')

#initialize screen
screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Sudoku')
pygame.display.set_icon(icon)
fps = pygame.time.Clock()

#background data
sudoku_data = Sudoku()
highscore = Data()
def generate_sudoku():
    sudoku_data.clear_lock()
    sudoku_data.make_sudoku_copy()
    sudoku_data.empty_random()

#Cache area
area = ['title','score','game','win']
cur_area = area[0]

#music
music_path = r'Final_Project_Year1/Asset/game_music.mp3'
pygame.mixer.music.load(music_path)
pygame.mixer_music.play(-1)

#shared asset
    #back button
base_back_button = pygame.image.load(r'Final_Project_Year1/Asset/back_button.png')
back = pygame.transform.scale(base_back_button, (200,100))
back_coordinate = (screen_width-200,screen_height-100)
back_col = back.get_rect()
back_col.topleft = back_coordinate

#Title asset
titlefont =pygame.font.Font(None, 170)
title = titlefont.render("Sudoku", True, (0, 0, 0))
#load title button (and the collision)
    #Start
start_ui = pygame.image.load(r'Final_Project_Year1/Asset/Title/start_button.png')
start_col = start_ui.get_rect()
start_col.topleft = (-10,((screen_height / 2)-50))
    #Score
score_ui = pygame.image.load(r'Final_Project_Year1/Asset/Title/score_button.png')
score_col = score_ui.get_rect()
score_col.topleft = (((screen_width / 2) - 250),((screen_height / 2)-50))
    #Quit
quit_ui = pygame.image.load(r'Final_Project_Year1/Asset/Title/quit_button.png')
quit_col = quit_ui.get_rect()
quit_col.topleft = (((screen_width / 2) + 250),((screen_height / 2)-50))

#Game asset
game_title = titlefont.render("Solve the Sudoku", True, (0, 0, 0))
    #number asset
num_font = pygame.font.Font(None, 50)
    #Text box
text_content = ""
text_box_font = pygame.font.Font(None,50)
input_box = pygame.Rect(screen_width - 500, (screen_height / 2) - 50, 200, 60)
textbox_active = False
    #text label
textbox_label = text_box_font.render('format: x-axis,y-axis,answer', True, (0,0,0))
    #input button
base_inp_button = pygame.image.load(r'Final_Project_Year1/Asset/game/input_button.png')
input_button = pygame.transform.scale(base_inp_button, (200,100))
input_coordinate = (screen_width - 600, (screen_height / 2) + 25)
input_col = input_button.get_rect()
input_col.topleft = input_coordinate
    #delete button
base_del_button = pygame.image.load(r'Final_Project_Year1/Asset/game/del_button.png')
del_button = pygame.transform.scale(base_del_button, (200,100))
del_coordinate = (screen_width - 350, (screen_height / 2) + 25)
del_col = del_button.get_rect()
del_col.topleft = del_coordinate
    #grid data
line_color = (0,0,225)
block_size = 60
number_path = num_array_list()

#Score asset
score_title = titlefont.render("Leaderboard", True, (0, 0, 0))
score_font = pygame.font.Font(None, 70)
username_column = score_font.render('Username', True , (0,0,0))
score_column = score_font.render('Score (in second)', True , (0,0,0))

#Win asset
win_title = titlefont.render('You Win', True, (0,0,0))
    #Name text box
name = ""
name_box = pygame.Rect((screen_width/2) - 170, (screen_height / 2), 300, 60)
name_active = False
    #name textbox label
name_label = num_font.render('Insert name:', True, (0,0,0))
    #add button
base_add_button = pygame.image.load(r'Final_Project_Year1/Asset/win/add_button.png')
add = pygame.transform.scale(base_add_button, (200,100))
add_coordinate = ((screen_width/2) - 130, (screen_height / 2) + 60)
add_col = add.get_rect()
add_col.topleft = add_coordinate

#The LOOP
run = True
while run:
    mouse_position = pygame.mouse.get_pos()
    #filling the screen with asset
    screen.fill((225,225,225))
    #Title Screen
    if cur_area == area[0]:
        #loading img
        screen.blit(title,(((screen_width / 2) - 250), ((screen_height / 2) - 200)))
        screen.blit(start_ui,(-10,((screen_height / 2)-50)))
        screen.blit(score_ui,(((screen_width / 2) - 250),((screen_height / 2)-50)))
        screen.blit(quit_ui,(((screen_width / 2) + 250),((screen_height / 2)-50)))
        #interaction
        if start_col.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]:
                cur_area = area[2]
                generate_sudoku()
                sudoku_data.timed()
        elif score_col.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]:
                cur_area = area[1]
        elif quit_col.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]:
                run = False
    #Scoreboard
    elif cur_area == area[1]:
        screen.blit(score_title,(((screen_width / 2) - 350), 0))
        screen.blit(back,back_coordinate)
        #write column
        screen.blit(username_column,(350,150))
        screen.blit(score_column,(750,150))
        #write top 5
        for i in range(5):
            try:
                name = highscore.get_top5()[i]['Username']
                #shorten name if its too long
                if len(name) > 13:
                    name = name[0:13]
                score = highscore.get_top5()[i]['Score']
                #displaying the result
                score_name = score_font.render(str(name), True , (0,0,0))
                score_score = score_font.render(str(score), True , (0,0,0))
                screen.blit(score_name,(350,i*80+250))
                screen.blit(score_score,(750,i*80+250))
            except:
                break
    #The Game
    elif cur_area == area[2]:
        screen.blit(game_title,(((screen_width / 2) - 500), 0))
        screen.blit(back,back_coordinate)
        #draw grid
            #draw some line
        pygame.draw.line(screen,line_color,(384,150),(384,705),2)
        pygame.draw.line(screen,line_color,(570,150),(570,705),2)
        pygame.draw.line(screen,line_color,(200,334),(754,334),2)
        pygame.draw.line(screen,line_color,(200,520),(754,520),2)
            #draw the box
        for y in range(9):
            for x in range(9):
                grid_img = pygame.Rect((x*(block_size+2))+200, (y*(block_size+2))+150, block_size, block_size)
                if sudoku_data.lock(x,y):
                    #if its changeable
                    pygame.draw.rect(screen, (128,128,128), grid_img) #draw a gray? square
                else:
                    #if its locked
                    pygame.draw.rect(screen, (250,0,0), grid_img) #draw a red? square
        #put number_img
        for y in range(9):
            for x in range(9):
                if sudoku_data.grid[y][x] != 0:
                    the_img_path = number_path[sudoku_data.grid[y][x]]
                    num_img = pygame.image.load(the_img_path)
                    img_num = pygame.transform.scale(num_img,(60,60))
                    screen.blit(img_num,((x*(block_size+2))+200,(y*(block_size+2))+150))
        if len(text_content) > 7:
            text_content = text_content[:-1]
        #Draw textbox
        if textbox_active:
            pygame.draw.rect(screen, (100,100,100), input_box)
        else:
            pygame.draw.rect(screen, (125,125,125), input_box)
        text_box_display = text_box_font.render(text_content, True, (0,0,0))
        screen.blit(text_box_display,(screen_width - 500, (screen_height / 2) - 40))
        #draw textbox label
        screen.blit(textbox_label,(screen_width - 600, (screen_height / 2) - 80))
        #draw functional button
        screen.blit(input_button,input_coordinate)
        screen.blit(del_button,del_coordinate)
        #Win effect
        if sudoku_data.correct():
            sudoku_data.timed()
            cur_area = area[3]
    #Win screen
    elif cur_area == area[3]:
        #Draw congratz
        screen.blit(win_title,(((screen_width / 2) - 250), 0))
        #Display time taken
        time_taken = sudoku_data.get_time()
        time_text = f'In {str(time_taken)} Seconds'
        time_display = num_font.render(time_text, True, (0,0,0))
        screen.blit(time_display,(screen_width/2 - 200, 100))
        #nickname textbox
        if name_active:
            pygame.draw.rect(screen, (100,100,100), name_box)
        else:
            pygame.draw.rect(screen, (125,125,125), name_box)
        #text in box
        text_box_display = text_box_font.render(name, True, (0,0,0))
        screen.blit(text_box_display,((screen_width/2) - 170, (screen_height / 2) + 10))
        #prevent text going over the box
        if len(name) > 11:
            name = name[:-1]
        #add textbox label
        screen.blit(name_label,((screen_width/2) - 170, (screen_height / 2) - 30))
        #draw add button
        screen.blit(add, add_coordinate)
    #Event Handler
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
        #back button (to title screen)
        elif back_col.collidepoint(mouse_position):
            if cur_area != area[3]:
                if pygame.mouse.get_pressed()[0]:
                    if cur_area == 'game':
                        text_content = ""
                        textbox_active = False
                        sudoku_data.clear_time()
                    cur_area = area[0]
        #game area textbox handling
        if cur_area == 'game':
            if event.type == pygame.MOUSEBUTTONDOWN:
                #active/deactivate inputbox
                if input_box.collidepoint(mouse_position):
                    textbox_active = not textbox_active
                else:
                    textbox_active = False
                #input answer
                if input_col.collidepoint(mouse_position):
                    temp = text_content.split(',')
                    try:
                        x_coordinate = int(temp[0])
                        y_coordinate = int(temp[1])
                        answer = int(temp[2])
                        if answer in [1,2,3,4,5,6,7,8,9]:
                            sudoku_data.insert(x_coordinate,y_coordinate,answer)
                    except:
                        None
                    text_content = ""
                #delete answer
                if del_col.collidepoint(mouse_position):
                    temp = text_content.split(',')
                    try:
                        x_coordinate = int(temp[0])
                        y_coordinate = int(temp[1])
                        sudoku_data.delete(x_coordinate,y_coordinate)
                    except:
                        None
                    text_content = ""
            #editing text
            if event.type == pygame.KEYDOWN:
                if textbox_active:
                    if event.key == pygame.K_BACKSPACE:
                        text_content = text_content[:-1] #delete text
                    else:
                        text_content += event.unicode #input text
        if cur_area == area[3]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #active/deactivate inputbox
                if name_box.collidepoint(mouse_position):
                    name_active = not name_active
                else:
                    name_active = False
                #add result
                if add_col.collidepoint(mouse_position):
                    nickname = name
                    try:
                        if name != "":
                            highscore.update(nickname,time_taken)
                            sudoku_data.clear_time()
                            cur_area = area[1]
                    except:
                        None
                    name = ""
            #editing text
            if event.type == pygame.KEYDOWN:
                if name_active:
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1] #delete text
                    else:
                        name += event.unicode #input text
    #update screen
    pygame.display.update()
    #limit fps
    fps.tick(30)

pygame.mixer_music.stop()
pygame.quit()
