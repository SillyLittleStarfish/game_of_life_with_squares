import pygame, sys
import time
from simulation import Simulation
from typewriter import Typewriter

pygame.init()
#Define Window
game_state = "welcome"
black = (0,0,0)
grey = (29,29,29)
window_width = 750
window_height = 750
cell_size = 25
FPS = 8


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(window_width, window_width, cell_size)

introduction_pages = True
game_of_life = False

instructions = Typewriter( """ 
WHAT IS THE GAME OF LIFE? 
The Game of Life is a simulation invented by 
mathematician John Conway in which very simple 
rules cause complex patterns to emerge.
Each cell in a square grid can either be alive 
or dead. 
Don't worry, they're not really.
In order to survive to the next generation, an 
alive cell must have 2 or 3 neighbouring alive 
cells.
Each alive cell with 1 or 0 neighbours will die
from isolation (oh no!).
Each dead cell adjacent to exactly 3 neighbours
is a birth cell and will become alive in the 
next generation. 
All births and deaths occur simultaneously within
each generation.
    
HOW TO PLAY:
""")


welcome = Typewriter("""
Welcome to Conway's Game of Life
Press i for instructions, any other key to start.
""")

before_you_start = Typewriter("""
Select a speed: 
[1] slow.
[2] normal speed?
[3] A little bit faster.

Then press N to continue.
""")




while introduction_pages == True: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if game_state == "welcome":
                if event.key == pygame.K_i: 
                    game_state= "introduction"
                else:
                    game_state = "simulation"
            elif game_state == "introduction": 
                game_state = "simulation"
            elif game_state == "simulation": 
                if event.key == pygame.K_1: 
                    FPS = 2
                elif event.key == pygame.K_2: 
                    FPS = 8
                elif event.key == pygame.K_3:
                    FPS = 12

                if event.key == pygame.K_n:
                    introduction_pages = False
                    game_of_life = True
    window.fill(black)            
    
    if game_state == "welcome": 
        welcome.update()
        welcome.draw(window,(50,50))
    elif game_state =="introduction": 
        instructions.update()
        instructions.draw(window,(50,50))
    elif game_state == "simulation":
        before_you_start.update()
        before_you_start.draw(window,(50,50))
    
    pygame.display.flip()
    clock.tick(60)



#System Running

while game_of_life == True: 
#introduction page 
  # check events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // cell_size
            column = pos[0] // cell_size
            simulation.edit_cells(row, column)

       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life is running")
                     
    #update 
    simulation.update()

    #draw
    window.fill(grey)
    simulation.draw(window)
        

    pygame.display.update()
    clock.tick(FPS)  


    

    



    

    
    
