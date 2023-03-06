#File Created By Daniel Azevedo
#libraries
#suspense, time between sentences
from time import sleep
#sorta random numbers, robots not true random
from random import randint

import pygame as pg

import os 

gamefolder = os.path.dirname(__file__)
print(gamefolder)

# game setting
WIDTH = 900
HEIGHT = 500
FPS = 30

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# starts pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ROCK, PAPER, Scissors")
clock= pg.time.Clock()
#all images
rock_image = pg.image.load(os.path.join(gamefolder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
paper_image = pg.image.load(os.path.join(gamefolder, 'money.jpg')).convert()
paper_image_rect = paper_image.get_rect()
scissor_image = pg.image.load(os.path.join(gamefolder, 'scissors.jpg')).convert()
scissor_image_rect = scissor_image.get_rect()
choose_image = pg.image.load(os.path.join(gamefolder, 'CHOOSE.jpg')).convert()
choose_image_rect = choose_image.get_rect()
rockc_image = pg.image.load(os.path.join(gamefolder, 'ROCKC.jpg')).convert()
rockc_image_rect = rockc_image.get_rect()
paperc_image = pg.image.load(os.path.join(gamefolder, 'PAPERc.jpg')).convert()
paperc_image_rect = paperc_image.get_rect()
sicc_image = pg.image.load(os.path.join(gamefolder, 'SICC.jpg')).convert()
sicc_image_rect = rockc_image.get_rect()
tier_image = pg.image.load(os.path.join(gamefolder, 'Tier.jpg')).convert()
tier_image_rect = tier_image.get_rect()
tiep_image = pg.image.load(os.path.join(gamefolder, 'Tiep.jpg')).convert()
tiep_image_rect = tiep_image.get_rect()
ties_image = pg.image.load(os.path.join(gamefolder, 'Ties.jpg')).convert()
ties_image_rect = ties_image.get_rect()
loser_image = pg.image.load(os.path.join(gamefolder, 'Loser.jpg')).convert()
loser_image_rect = loser_image.get_rect()
Losep_image = pg.image.load(os.path.join(gamefolder, 'Losep.jpg')).convert()
Losep_image_rect = Losep_image.get_rect()
Loses_image = pg.image.load(os.path.join(gamefolder, 'Loses.jpg')).convert()
Loses_image_rect = Loses_image.get_rect()
winr_image = pg.image.load(os.path.join(gamefolder, 'Winr.jpg')).convert()
winr_image_rect = winr_image.get_rect()
winp_image = pg.image.load(os.path.join(gamefolder, 'Winp.jpg')).convert()
winp_image_rect = winp_image.get_rect()
wins_image = pg.image.load(os.path.join(gamefolder, 'Wins.jpg')).convert()
wins_image_rect = wins_image.get_rect()
defeat_image = pg.image.load(os.path.join(gamefolder, 'Defeat.jpg')).convert()
defeat_image_rect = defeat_image.get_rect()
Victory_image = pg.image.load(os.path.join(gamefolder, 'Victory.jpg')).convert()
Victory_image_rect = Victory_image.get_rect()
Tie_image = pg.image.load(os.path.join(gamefolder, 'tie.jpg')).convert()
Tie_image_rect = Tie_image.get_rect()
Bo_image = pg.image.load(os.path.join(gamefolder, 'BON.jpg')).convert()
Bo_image_rect = Bo_image.get_rect()
SU_image = pg.image.load(os.path.join(gamefolder, 'SU.jpg')).convert()
SU_image_rect = SU_image.get_rect()
NG_image = pg.image.load(os.path.join(gamefolder, 'NG.jpg')).convert()
NG_image_rect = NG_image.get_rect()
Con_image = pg.image.load(os.path.join(gamefolder, 'conti.jpg')).convert()
Con_image_rect = Con_image.get_rect()
#stuff for later stages of code
First = True
Secondr = False
Secondp = False
Seconds = False
Thirdr = False
Thirdp = False
Thirds = False
Tier = False
Tiep = False
Ties = False
Loser = False
Losep = False
Loses = False
Winr = False
Winp = False
Wins = False
Victory = False
Defeat = False
Tie = False
# computer and user choices
choices = ["rock", "paper", "scissors"]
#comp choice
def comp_choice():
    #Returns random value between 0 and 2
    return choices[randint(0,2)]
cpu = comp_choice()


running = True
#draw/ image display
 #starting locations
Con_image_rect.x = 600
Con_image_rect.y = 300
rock_image_rect.x = 330
paper_image_rect.x = 600
scissor_image_rect.x
choose_image_rect.x = 300
choose_image_rect.y = 300
rockc_image_rect.x = 150
rockc_image_rect.y = 10
paperc_image_rect.x = 240
paperc_image_rect.y = 50
sicc_image_rect.x = 240
sicc_image_rect.y = 50
Bo_image_rect.x = 250
SU_image_rect.x = 650
winp_image_rect.x = 150
tiep_image_rect.x = 150
tiep_image_rect.y = 70
wins_image_rect.x = 100
wins_image_rect.y = 20
ties_image_rect.x = 250
ties_image_rect.y = 150
Loses_image_rect.x = 100
Loses_image_rect.y = 50
defeat_image_rect.x = 100
defeat_image_rect.y = 75
tier_image_rect.y = 200
tier_image_rect.x = 100
#starting images
screen.fill(BLACK)
screen.blit(rock_image, rock_image_rect)
screen.blit(scissor_image, scissor_image_rect)
screen.blit(paper_image, paper_image_rect)
screen.blit(choose_image, choose_image_rect)
clock.tick(FPS)
pg.display.flip()
#first click
fc = True
while running == True:
   while fc and running == True:
    #images for when it resets
    screen.fill(BLACK)
    screen.blit(rock_image, rock_image_rect)
    screen.blit(scissor_image, scissor_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(choose_image, choose_image_rect)
    pg.display.flip()
    for event in pg.event.get():
        #quits
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.MOUSEBUTTONUP:
            pg.mouse.get_pos
            mouse_coords = pg.mouse.get_pos()
            print(mouse_coords)
            #coords given
            print(rock_image_rect.collidepoint(mouse_coords))
            
            #if i hit the rock, tells me that it is in fact the rock
            if rock_image_rect.collidepoint(mouse_coords) == True:
                    print("THATS THE ROCK")
                    userchoice = "rock"
                    #for second image layer, get rid of first
                    First = False
                    Secondr = True
                    #for figuring out which click this is
                    fc = False
                    sc = True
                   
            if paper_image_rect.collidepoint(mouse_coords) == True:
                    print("MONEY, Paper of tommorrow")
                    userchoice = "paper"
                    First = False
                    Secondp = True
                    fc = False
                    sc = True
                    sleep(1)

            if scissor_image_rect.collidepoint(mouse_coords) == True:
                    print("SCISSOR TIME")
                    userchoice = "scissors"
                    First = False
                    Seconds = True
                    fc = False
                    sc = True
                    sleep(1)
   while running and sc == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.MOUSEBUTTONUP:
            #new comp choice everytime
            cpu = comp_choice()
            
            sleep(1)
            #Image showing match chosen
            if userchoice == cpu and userchoice == "rock":
                        
             Tier = True
             print("WE HAVE A TIE")
             #now onto the third click
             tc = True
             sc = False
            elif cpu == "paper" and userchoice == "rock":
                        
             Loser = True
             print("I win")
             tc = True
             sc = False
            elif cpu == "scissors" and userchoice == "rock":
                        
             Winr = True
             print("U WIN")
             tc = True
             sc = False
            elif userchoice == cpu and userchoice == "paper":
                        
             Tiep = True
             print("WE HAVE A TIE")
             tc = True
             sc = False
            elif cpu == "scissors" and userchoice == "paper":
                        
             Losep = True
             print("I win")
             tc = True
             sc = False
            elif cpu == "rock" and userchoice == "paper":
                        
             Winp = True
             print("U WIN")
             tc = True
             sc = False 
            elif userchoice == cpu and userchoice == "scissors":
             Ties = True
             print("WE HAVE A TIE")
             tc = True
             sc = False
            elif cpu == "rock" and userchoice == "scissors":
                        
             Loses = True
             print("I win")
             tc = True
             sc = False
            elif cpu == "paper" and userchoice == "scissors":
                        
             Wins = True
             print("U WIN")
             tc = True
             sc = False
    #displays second images
    if First == False and Secondr == True:
        print("HERE")
        screen.fill(BLACK)
        screen.blit(rockc_image, rockc_image_rect)
        screen.blit(Con_image, Con_image_rect)
        sleep(1)
        # no longer showing the second images
        Secondr = False    
    if First == False and Secondp == True:
        screen.fill(BLACK)
        screen.blit(paperc_image, paperc_image_rect)
        screen.blit(Con_image, Con_image_rect)
        Secondp = False
    if First == False and Seconds == True:
        screen.fill(BLACK)
        screen.blit(sicc_image, sicc_image_rect)
        screen.blit(Con_image, Con_image_rect)
        Seconds = False
    pg.display.update()
   while running and tc == True:
    for event in pg.event.get():
         if event.type == pg.QUIT:
            running = False  
    # displays the images for the match  
    if Tier == True:
        #finding result of match
        Tie = True
        screen.fill(BLACK)
        screen.blit(tier_image, tier_image_rect)
        #reset
        Tier = False
        #onto fourth click
        tc = False
        fr = True
        print("1")
       
    if Loser == True:
        Defeat = True
        screen.fill(BLACK)
        screen.blit(loser_image, loser_image_rect)
        print("2")
        Loser = False
        tc = False
        fr = True
        
    if Winr == True:
        Victory = True
        screen.fill(BLACK)
        screen.blit(winr_image, winr_image_rect)
        print("3")
        Winr = False
        tc = False
        fr = True
        
    if Tiep == True:
        Tie = True
        screen.fill(BLACK)
        screen.blit(tiep_image, tiep_image_rect)
        tc = False
        fr = True
        Tiep = False
        
        print("uefhuehfuhf")
    if Losep == True:
        Defeat = True
        screen.fill(BLACK)
        screen.blit(Losep_image, Losep_image_rect)
        tc = False
        fr = True
        Losep = False
        
        print("iwjdiwndnwd")
    if Winp == True:
        Victory = True
        screen.fill(BLACK)
        screen.blit(winp_image, winp_image_rect)
        tc = False
        fr = True
        Winp = False
        
        print("wkdnwdn")
    if Ties == True:
        Tie = True
        screen.fill(BLACK)
        screen.blit(ties_image, ties_image_rect)
        tc = False
        fr = True
        Ties = False
        
        print("niwndiwnd")
    if Loses == True:
        Defeat = True
        screen.fill(BLACK)
        screen.blit(Loses_image, Loses_image_rect)
        tc = False
        fr = True
        Loses = False
        
        print("wjnduwnduw")
    if Wins == True:
        Victory = True
        screen.fill(BLACK)
        screen.blit(wins_image, wins_image_rect)
        tc = False
        fr = True
        Wins = False
        
        print("niwdniwdniwdn")
    pg.display.update()
   while running and fr == True:
    for event in pg.event.get():
        print("YO Im here")
    if event.type == pg.QUIT:
        running = False 
    #shows end of match images
    if Victory == True:
        sleep(4)
        screen.fill(BLACK)
        screen.blit(Victory_image, Victory_image_rect)
        # onto the next click
        ng = True
        fr = False
        # reset
        Victory = False
    if Defeat == True:
        sleep(4)
        screen.fill(BLACK)
        screen.blit(defeat_image, defeat_image_rect) 
        ng = True
        fr = False
        Defeat = False
    if Tie == True:
        sleep(4)
        screen.fill(BLACK)
        screen.blit(Tie_image, Tie_image_rect)
        ng = True
        fr = False
        Tie = False
    else:
        print("Why")
    pg.display.update()
   while running and ng == True:
      #restart images
      sleep(4)
      screen.fill(BLACK)
      screen.blit(Bo_image,Bo_image_rect)
      screen.blit(SU_image, SU_image_rect)
      screen.blit(NG_image, NG_image_rect)
      pg.display.flip()    
      for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
           mouse_coords = pg.mouse.get_pos()
           print(mouse_coords)
           #ends game
           if SU_image_rect.collidepoint(mouse_coords) == True:
              running = False
            #restarts
           if NG_image_rect.collidepoint(mouse_coords) == True:
              fc = True
              ng = False  
pg.quit()