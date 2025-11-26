# This Is The Main Module Of The "SIX SHIPS" Game Program
# And It Contains The Basic Structure Of The Code


#Import Modules

import pygame
import sys

#RGB Colors
WHITE        = (255,255,255)
BLUE         = (2,137,255)
LIGHT_BLUE   = (170,209,242)
GREEN        = (14,200,3)
LIGHT_GREEN  =(175,242,171)
BLACK        = (0,0,0)

WINDOW_SIZE  = (506,506)

GAME_TITLE   = 'Six_Ships'

TIlE_SIZE    = 90
HAlf_TILE    = TIlE_SIZE//2

CORDS        = [5,106,207,308,409]

CORNERS      = [(0,0),(0,4),(4,0),(4,4)]
START_ROW    = [(0,1),(0,2),(0,3)]
END_ROW      = [(4,1),(4,2),(4,3)]
START_COLUMN = [(1,0),(2,0),(3,0)]
END_COLUMN   = [(1,4),(2,4),(3,4)]

# Here Are The Objects We Need At The Main Code

import pygame
import numpy as np
from CONSTANTS import *
sq_list = [[pygame.Rect(CORDS[i],CORDS[j],TIlE_SIZE,TIlE_SIZE) for i in range(5)] for j in range(5)]


blues=[0,0,0,0]
greens=[0,0,0,0]


def a(Game_board):
    blue_lock1 = (Game_board[0][1]==Game_board[4][2]==Game_board[4][3]=='b' and Game_board[1][1]==Game_board[2][1]=='g')
    blue_lock2 = (Game_board[0][2]==Game_board[4][3]==Game_board[4][1]=='b' and Game_board[1][2]==Game_board[2][2]=='g')
    blue_lock3 = (Game_board[0][3]==Game_board[4][1]==Game_board[4][2]=='b' and Game_board[1][3]==Game_board[2][3]=='g')
    blue_lock4 = (Game_board[1][1]==Game_board[4][2]==Game_board[4][3]=='b' and Game_board[2][1]==Game_board[3][1]=='g')
    blue_lock5 = (Game_board[1][2]==Game_board[4][3]==Game_board[4][1]=='b' and Game_board[2][2]==Game_board[3][2]=='g')
    blue_lock6 = (Game_board[1][3]==Game_board[4][1]==Game_board[4][2]=='b' and Game_board[2][3]==Game_board[3][3]=='g')
    blue_lock = blue_lock1 or blue_lock2 or blue_lock3 or blue_lock4 or blue_lock5 or blue_lock6

    if blue_lock:
        return 1
    
    green_lock1 = (Game_board[1][0]==Game_board[2][4]==Game_board[3][4]=='g' and Game_board[1][1]==Game_board[1][2]=='b')
    green_lock2 = (Game_board[2][0]==Game_board[3][4]==Game_board[1][4]=='g' and Game_board[2][1]==Game_board[2][2]=='b')
    green_lock3 = (Game_board[3][0]==Game_board[1][4]==Game_board[2][4]=='g' and Game_board[3][1]==Game_board[3][2]=='b')
    green_lock4 = (Game_board[1][1]==Game_board[2][4]==Game_board[3][4]=='g' and Game_board[1][2]==Game_board[1][3]=='b')
    green_lock5 = (Game_board[2][1]==Game_board[3][4]==Game_board[1][4]=='g' and Game_board[2][2]==Game_board[2][3]=='b')
    green_lock6 = (Game_board[3][1]==Game_board[1][4]==Game_board[2][4]=='g' and Game_board[3][2]==Game_board[3][3]=='b')
    green_lock = green_lock1 or green_lock2 or green_lock3 or green_lock4 or green_lock5 or green_lock6


    if green_lock:
        return 2
    
    return 3



#To Initialize The Game
pygame.init()
Six_Ships = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(GAME_TITLE)

# Here Are The Functions We Defined And Used In The Program
def show():
    Six_Ships.fill(BLACK)
    for row in range(len(sq_list)):
        for col in range(len(sq_list[0])):
            # print(row,col)
            # if (row,col) in corners:
            #     pygame.draw.rect(Six_Ships, black, sq_list[row][col])
            if (row,col) in END_ROW:
                pygame.draw.rect(Six_Ships, LIGHT_BLUE, sq_list[row][col])
            elif (row,col) in END_COLUMN:
                pygame.draw.rect(Six_Ships, LIGHT_GREEN, sq_list[row][col])
            elif (row,col) not in CORNERS:
                pygame.draw.rect(Six_Ships, WHITE, sq_list[row][col])
    for (row,col) in START_ROW:
        blue_triangle(row,col)
    for (row,col) in START_COLUMN:
        green_triangle(row,col)



def first_player(key):
    if key.lower()=='b':
        return True
    if key.lower()=='g':
        return False



def blue_triangle(row,col):
    pygame.draw.polygon(Six_Ships,BLUE,((CORDS[col]+15,CORDS[row]+15),(CORDS[col]+TIlE_SIZE-15,CORDS[row]+15),(CORDS[col]+HAlf_TILE,CORDS[row]+TIlE_SIZE-15)))



def green_triangle(row,col):
    pygame.draw.polygon(Six_Ships,GREEN,((CORDS[col]+15,CORDS[row]+15),(CORDS[col]+15,CORDS[row]+TIlE_SIZE-15),(CORDS[col]+TIlE_SIZE-15,CORDS[row]+HAlf_TILE)))



def check_state(blues, greens):
    sum_blues=blues[1]+blues[2]+blues[3]
    sum_greens=greens[1]+greens[3]+greens[3]
    if sum_blues==16 and sum_greens<16:
        print('sum_blues',sum_blues,'sum_greens',sum_greens)
        return 'b'
    elif sum_greens==16 and sum_blues<16:
        return 'g'
    return "Continue"



def check_move(turn, gb, row, col):
    if turn:
        if gb[row+1][col]=='g':
            if row<3:
                if gb[row+2][col]=='g':
                    return 0
                else:
                    return 2
        else:
            return 1
    else:
        if gb[row][col+1]=='b':
            if col<3:
                if gb[row][col+2]=='b':
                    return 0
                else:
                    return 2
        else:
            return 1



# Here We Determin Wheter The First Player is "Green" o "Blue" by Entering "g" or "b" in The TERMINAL!
FP = '-'
while FP.lower() not in ['b','g']:
    FP = input("Who Plays First?:\nBlue---> Press 'b'\n Green--->Press 'g':\n")
turn = first_player(FP) #variable 'turn':    if True, then Blue moves       if False, then Green moves
allow = True
edame=True
show()


# These Are The States That The player Who Has To Play, Has No Move To Take!
green_lock1=False
green_lock2=False
green_lock3=False
green_lock4=False
green_lock5=False
green_lock=False

blue_lock=False
blue_lock1=False
blue_lock2=False
blue_lock3=False
blue_lock4=False
blue_lock5=False

# Game Board Shows If Every Square-Cell is Empty, Green Or Blue
# Game Board Will Change With Mouse Clicks On Blue Ships and Green Ships
Game_board =[[ 0 ,'b','b','b', 0 ],
             ['g', 0 , 0 , 0 , 0 ],
             ['g', 0 , 0 , 0 , 0 ],
             ['g', 0 , 0 , 0 , 0 ],
             [ 0 , 0 , 0 , 0 , 0 ]]

#The Main Loop Of The Game
while True:

    # if The State Of Game Is Not Over It Should Continue:
    if allow and edame:

        for event in pygame.event.get():

            # Close The Game If Click On The Game's Window's Close Buttom
            if event.type == pygame.QUIT: #quit pygame
                pygame.quit() 
                sys.exit()
            
            # What Happens If You Click On Any Square-Cells Displaying On Game Window
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # This is "BLUE"'s Turn To Move Forward
                if turn:
                    for col in range(1,4):
                        row = int(blues[col])
                        if row!=4 and sq_list[row][col].collidepoint(pos): # (Blue Ships At The Lowest Row Are At Their Destination,
                                                                           #  So The Can't Move Any Further)
                            
                            cm=check_move(turn,Game_board,row,col) # This Line Check If There Is:   One or Two or No Green Ships In The Way.
                                                                   # Then It Decides How Long
                                                                   #          The Step Should Be:    2  or  0  or 1  (0 means No Move Forward) 

                            # Now If The Blue Ship Is Able To Move, So It Does So!
                            if cm!=0:
                                blues[col]+=cm
                                Game_board[row+cm][col], Game_board[row][col] = Game_board[row][col], Game_board[row+cm][col]
                                pygame.draw.rect(Six_Ships, WHITE, sq_list[row][col])
                                blue_triangle(row+cm,col)
                                turn = not turn

                #This Is "GREEN"'s Turn To Move Forward
                else:
                    for row in range(1,4):
                        col = int(greens[row])
                        if col!=4 and sq_list[row][col].collidepoint(pos): # (Green Ships At The Right-End Column Are At Their Destination,
                                                                           #  So The Can't Move Any Further)
                            
                            cm=check_move(turn,Game_board,row,col) # This Line Check If There Is:   One or Two or No Green Ships In The Way.
                                                                   # Then It Decides How Long
                                                                   #          The Step Should Be:    2  or  0  or 1  (0 means No Move Forward)

                            # Now If The Blue Ship Is Able To Move, So It Does So!
                            if cm!=0:
                                greens[row]+=cm
                                Game_board[row][col+cm], Game_board[row][col] = Game_board[row][col], Game_board[row][col+cm]
                                pygame.draw.rect(Six_Ships, WHITE, sq_list[row][col])
                                green_triangle(row,col+cm)
                                turn = not turn



                # Now There's A Situation Which in One Fleet Of Ships Has The Turn To Move,
                # But There Is No Possible Move For Them: For Example When Two Of The Ships Are Arrived At The End,
                #And The 3rd Ships Is Blocked By Two Ships Of Enemy IN His Way:
                                                                                #      . . .
                                                                                #    G B B 0 .
                                                                                #    . . . . G
                                                                                #    . . . . G
                                                                                #      . . B 
                if   a(Game_board) == 1:
                    turn = False
                elif a(Game_board) == 2:
                    turn = True
                else:
                    continue

        pygame.display.update()

        #Do We Have A Winner?
        b = (blues[1]==4 and blues[1]==blues[2] and blues[2]==blues[3])
        g = (greens[1]==4 and greens[1]==greens[2] and greens[2]==greens[3])

        if b and not g:
            print("Playar Blue is the winner!")
            edame = False

        elif g and not b:
            print("Playar Green is the winner!")
            edame = False

        # If We Have Had A Winner, The Game Is Over!
        if not edame:
            allow = False
 
 
            #can player "turn" move?
    else:
        pygame.quit() 
        sys.exit()