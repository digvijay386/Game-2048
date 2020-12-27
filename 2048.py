#Importing required modules
import pygame
import random

#Initializing pygame modules
pygame.init()

#Initializing font module
pygame.font.init()

#Creating fonts 
myfont = pygame.font.SysFont('Comic Sans MS', 50)
myfont_win=pygame.font.SysFont('Times New Roman', 80)

#Defining RGB values for colours
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
GOLD=( 230, 215, 0)


screen = pygame.display.set_mode((800,600)) #Initialzing a screen for display
pygame.display.set_caption('2048') 
clock = pygame.time.Clock() 

#Lists to store game matrices
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
board_copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#Initializing variables
points = 0
score = 0
continue_after_win = 0
draw_state = 0

try:
    #TODO : "highscore.txt is a file in the current directory containing
    #       the highest score recorded. This is not erased when game is
    #       closed. Open the file and store the value of highest score in
    #       variable called highest_score
except:
    highest_score=0

#To set initial state of game matrix and score.
def initial(): 
    """
    Fill in two random cells of the board with either 2 or 4.
    Reset current score to zero and any other variables you might think
    needs resetting.
    """
    pass
      

#To draw the game matrix, scores and required buttons
def draw():
    global highest_score,points
    
    mouse=pygame.mouse.get_pos()#To get the mouse cursor position    
    click=pygame.mouse.get_pressed()#To get the state of the mouse buttons
    
    #Drawing the game matrix
    for i in range (0,5):
    	pygame.draw.line(screen, BLUE, (200,100*(i+1) ), (600, 100*(i+1)))
    	pygame.draw.line(screen, BLUE, (200+100*i,100 ), (200+100*i,500 ))          

    #Displaying the name of game, 'Score' and 'High Score'
    textsurface = myfont.render('2048', False, WHITE)
    screen.blit(textsurface,(50,50))           

    textsurface = myfont.render('Score', False, GREEN)
    screen.blit(textsurface,(660,50))            

    textsurface = myfont.render('Highest_score', False, RED)
    screen.blit(textsurface,(630,150)) 

    if mouse[0] < 175 and mouse[0] > 50 and mouse[1] < 250 and mouse[1] > 200:
        pygame.draw.rect(screen, GREEN,(50,200,125,50))#Change button colour to green
        if click[0] == 1: #If button is clicked
            reset() # Reset the matrix by calling reset() function            
    else:#Display colour of button as red	
        pygame.draw.rect(screen,RED,(50,200,125,50))   

    #Display 'RESET' on the button
    textsurface = myfont.render('RESET', False, WHITE)
    screen.blit(textsurface,(55,210))
   
    if mouse[0] < 175 and mouse[0] > 50 and mouse[1] < 350 and mouse[1] > 300:
        pygame.draw.rect(screen, GREEN,(50,300,125,50)) #Change button colour to green
        if click[0]:#If button is clicked
            undo() #Undo the prevoius move by calling undo() function
    else:#Display colour of button as blue.	
        pygame.draw.rect(screen,BLUE,(50,300,125,50))   

    #Display 'UNDO' on the button
    textsurface = myfont.render('UNDO', False, WHITE)
    screen.blit(textsurface,(60,310))    

    for i in range (0,4):
        for j in range (0,4):
            if not board[i][j] == 0:
                if board[i][j] < 1000:
                    textsurface = myfont.render(str(board[i][j]), False, WHITE)
                    screen.blit(textsurface,((j*100)+200+35,(i+1)*100+35))
                else:
                    textsurface = myfont.render(str(board[i][j]), False, WHITE)
                    screen.blit(textsurface,((j*100)+200+15,(i+1)*100+35))

    #TODO : Write code to display the score(Consult PyGame documentation for displaying Text)

    #TODO : Write code to display the highest score till date(Consult PyGame documentation for displaying Text)

    #TODO : Write highest score to file(Consult PyGame documentation for displaying Text)
    
    adjacent_horizontal = adjacent_vertical = all_cells = 0

    #TODO : Check if any two adjacent horizontal elements are equal

    #TODO : Check if any two adjacent vertical elements are equal

    #TODO : Check if all cells are filled        

    if adjacent_horizontal == 0 and adjacent_vertical == 0 and all_cells == 0:
        textsurface = myfont.render("Game Over !!! Now GTFO...", False, RED)
        screen.blit(textsurface,(300,50)) 


def undo():
    """
    Restore board by undoing the last move.
    """
    pass


def right():
    """
    Squash rows of board left when right key is pressed.
    
    Guidelines
    ----------
    
    You might have to break up this task into a "squash" and "replace" operation
    The squash operation would accept a list and compute the new list after
    values are squashed in that direction. Once that's computed for every row,
    replace the rows with the new computed ones. Don't forget to add
    a random element to the board once you're done with row-wise squash.
    """
    pass


def left():
    """
    Squash rows of board left when left key is pressed.
    
    Guidelines
    ----------
    
    You might have to break up this task into a "squash" and "replace" operation
    The squash operation would accept a list and compute the new list after
    values are squashed in that direction. Once that's computed for every row,
    replace the rows with the new computed ones. Don't forget to add
    a random element to the board once you're done with row-wise squash.
    """
    pass

def up():
    """
    Squash columns of board up when up key is pressed.
    
    Guidelines
    ----------
    
    You might have to break up this task into a "squash" and "replace" operation
    The squash operation would accept a list and compute the new list after
    values are squashed in that direction. Once that's computed for every column,
    replace the columns with the new computed ones. Don't forget to add
    a random element to the board once you're done with columnwise squash.
    """
    pass

def down():
    """
    Move columns of board down when down key is pressed.
    
    Guidelines
    ----------
    
    You might have to break up this task into a "squash" and "replace" operation
    The squash operation would accept a list and compute the new list after
    values are squashed in that direction. Once that's computed for every column,
    replace the columns with the new computed ones. Don't forget to add
    a random element to the board once you're done with columnwise squash.
    """
    pass


#To add element to game matrix
def add():
    """
    Fills up one empty cell of the board
    
    Guidelines
    ----------
    
    The cell must be filled up randomly with either 2 or 4. Whether you
    should favour 2 or 4 more is upto you. Experiment with both.
    """
    pass


#To reset the game matrix to initial state 
def reset():
    """
    Reset the board and restart the game. 
    """
    pass


def welcome_message():
    """
    Display a welcome message at the start of the game
    """
    global quit, draw_state

    #TODO : Consult PyGame documentation and retrieve mouse position and mouse action state.
    #       Store them in variables 'mouse' and 'click'.
    
    #Fill the screen black
    screen.fill(BLACK)
    
    #Display '2048'
    textsurface=myfont_win.render('2048', False, GOLD)
    screen.blit(textsurface, (300, 200))    

    if mouse[0] < 450 and mouse[0] > 330 and mouse[1] < 450 and mouse[1] > 400:#If mouse hovers over button
        pygame.draw.rect(screen, GREEN,(310,400,130,50))#Change button colour to green 
        if click[0]:#If button is clicked 
           draw_state += 1
           draw() #Draw the game matrix, thereby startng the game
    else:#Display colour of button as blue	
        pygame.draw.rect(screen,BLUE,(310,400,130,50))

    #Display 'PLAY' on the button
    textsurface = myfont.render('PLAY', False, WHITE)
    screen.blit(textsurface,(330,410)) 


def win_message():
    """
    Display a victory message when 2048 is achieved
    """
    global quit, continue_after_win

    #TODO : Consult PyGame documentation and retrieve mouse position and mouse action state.
    #       Store them in variables mouse and click.

    #Fill the screen to black
    screen.fill(BLACK)

    #Display 'You won!' on screen
    #TODO : Display a win message on screen. Get as creative as you want :)    

    if mouse[0] < 375 and mouse[0] > 200 and mouse[1] < 450 and mouse[1] > 400:#If mouse hovers over button
        pygame.draw.rect(screen, GREEN,(200, 400,125,50))#Change button colour to green 
        if click[0]==1:#If button is clicked 
            quit=True #Change quit to true, thereby quitting the game
    else:#Display colour of button as red	
        pygame.draw.rect(screen,RED,(200,400,125,50))   

    #Display 'QUIT' on the button
    textsurface = myfont.render('QUIT', False, WHITE)
    screen.blit(textsurface,(220,410))
 
    if mouse[0] < 650 and mouse[0] > 430 and mouse[1] < 450 and mouse[1] > 400:#If mouse hovers over button
        pygame.draw.rect(screen, GREEN,(410,400,220,50))#Change button colour to green  
        if click[0]==1:#If button is clicked 
           continue_after_win = 1
           draw()#Draw the game matrix, therby continuing the game
    else:#Display colour of button as blue	
        pygame.draw.rect(screen,BLUE,(410,400,220,50))   

    #Display 'CONTINUE' on the button
    textsurface = myfont.render('CONTINUE', False, WHITE)
    screen.blit(textsurface,(430,410)) 

initial() #Calling initial() function, thereby beginning the game
welcome_message() #Dispaying welcome message

quit = False #Initialzing variable  

while not quit: #While game is running
    #global continue_after_win, draw_state    
    screen.fill((50, 50, 50)) #Fill screen to grey


    for event in pygame.event.get():
        #TODO : Look up keyboard event in PyGame, there should be four more
        #       conditionals here corresponding to left, right, up and down key.
        #       
        #       Below is one such event. The quit event.
        if event.type == pygame.QUIT:#If user quits game
            quit = True

    if draw_state == 0:#If game has just begun
        welcome_message()#Display welcome message

    if draw_state > 0:#If game has already begun
        draw()#Draw game matrix

    #If user achieves 2048
    if continue_after_win == 0:         
        for i in range(0,4):
            for j in range(0,4):
                if board[i][j]==2048: #Checking if any element in game matrix is equal to 2048               
                    win_message()#Displaying victory message by calling win_message() function                   

    pygame.display.update() #Update portions of the screen for software displays  

pygame.quit() #Uninitialize all pygame modules
