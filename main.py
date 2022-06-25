###########################################################################################
#   2º Semestre do 1º ano do curso de Engenharia Mecânica - Instituto Superior Técnico    #
#   Unidade Curricular do Projeto - Fundamentos da Programação                            #
#   Nome do Projeto: Robô da Fruta                                                        #
#   Autores: Afonso Araújo (102685) e Lucas Feijó (103968)                                #
#   Grupo: G45                                                                            #
#   Data: 25.06.2022                                                                      #
#   Módulo: main                                                                          #
###########################################################################################

from random import randint
import time
from tkinter import filedialog as fd
from graphics import *
from Harve import *
from Tree import *
from Charger import *
from Obstacle import *
from Button import *
from math import *
from Findpath import *

# Global Lists
Obstacles = []                 # Current Obstacles         
Goal = []                      # Current Goals
Buttons = []                   # Available Buttons
Chargers = []                  # Available Chargers
bars = []                      # Rectangles that make the battery bars
Path = []                      # Findpath() appends Points
Lines = []                     # Filereader() append strings from file

# Global Variables
GameMode = 0                   # Determines what mode is being played. varies in [0;4]  (0 means no Gamemode) 
WindowWidth = 800              # Width of win
WindowHeight = 600             # Height of win
TabSize = 100                  # Size of the lateral tabs
ButtonsVerticalSpacement = 50  # Vertical distance between buttons
ButtonsHeight = 30             # Button's height
ObstaclesNumber = 5            # Number of obstacles to generate
MaxObstacleDistance = 20       # Minimum distance between 2 obstacles

## Global Objects ##
win = GraphWin("GAME", WindowWidth, WindowHeight, autoflush=False)   # main window

#Tabs
LeftTab = Rectangle(Point(0, WindowHeight), Point(TabSize, 0))
RightTab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))

#Labels
infolabel1 = Text(Point(WindowWidth/2, WindowHeight/2-ButtonsVerticalSpacement*0.5), "Click to place ")
infolabel2 = Text(Point(WindowWidth/2, WindowHeight/2+ButtonsVerticalSpacement*0.5), "a Tree and hit Run")
infolabel3 = Text(Point(WindowWidth/2, WindowHeight/2), "Click to Reset")
infolabel4 = Text(Point(WindowWidth-TabSize/2, ButtonsVerticalSpacement*3), "Obstacles:")
infolabel5 = Text(Point(WindowWidth-TabSize/2, ButtonsVerticalSpacement*3.5), "0")
infolabel6 = Text(Point(WindowWidth-TabSize/2, ButtonsVerticalSpacement*4), "Trees:")
infolabel7 = Text(Point(WindowWidth-TabSize/2, ButtonsVerticalSpacement*4.5), "0")

#Enhancement
LeftTab.setFill("light grey")
RightTab.setFill("light grey")
infolabel1.setFace('courier')
infolabel2.setFace('courier')
infolabel3.setFace('courier')
infolabel4.setFace('courier')
infolabel5.setFace('courier')
infolabel6.setFace('courier')
infolabel7.setFace('courier')
infolabel1.setSize(10)
infolabel2.setSize(10)
infolabel3.setSize(10)
infolabel4.setSize(10)
infolabel5.setSize(10)
infolabel6.setSize(10)
infolabel7.setSize(10)

def main():
    '''main program'''
    
    #Global Buttons
    global play1_button
    global play2_button
    global play3_button
    global play4_button
    global reset_button
    global quit_button
    global run_button
    global reset_button
    
    LeftTab.draw(win)
    RightTab.draw(win)
    
    #Create Buttons
    play1_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Mode 1", Playmode1)
    play2_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*5), (2/3)*TabSize, ButtonsHeight, "Mode 2", Playmode2)
    play3_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*6), (2/3)*TabSize, ButtonsHeight, "Mode 3", Playmode3)
    play4_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*7), (2/3)*TabSize, ButtonsHeight, "Mode 4", Playmode4)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement), (2/3)*TabSize, ButtonsHeight, "Reset", Reset)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Run", Run1)
    reset_button.deactivate()
    run_button.deactivate()
    
    #Append Buttons
    Buttons.append(quit_button)
    Buttons.append(reset_button)
    Buttons.append(play1_button)
    Buttons.append(play2_button)
    Buttons.append(play3_button)
    Buttons.append(play4_button)
    Buttons.append(run_button)

    while True:
        CheckButtons(win)
        
def Quit():
    '''closes win'''
    win.close()
        
def CheckButtons(win):
    '''checks if there was a click on a given window and executes the button's function if clicked inside'''
    mouse = win.checkMouse()
    if mouse != None:
        for Button in Buttons:
            if Button.clicked(mouse):
                Button.onClick()
                Button.deactivate()
                return True        

def IsInside(x,y):
    '''returns True if (x,y) is inside''' 
    return (TabSize < x < (WindowWidth - TabSize))

def Generatefield(win):
    '''generates obstacles in random positions and appends them in Obstacles list'''
    Obstacles.append(Obstacle(randint(TabSize+20, 780-TabSize), randint(TabSize+20, 580-TabSize), randint(0, 2), win))
    while len(Obstacles) < ObstaclesNumber:
      valid = True
      NewObstacle = Obstacle(randint(TabSize+20, 780-TabSize), randint(TabSize+20, 580-TabSize), randint(0, 2), win)
      for Obstaclei in Obstacles:
          ObstacleDistance = sqrt( ((NewObstacle.PosX-Obstaclei.PosX)**2) + ((NewObstacle.PosY-Obstaclei.PosY)**2) )
          if ObstacleDistance < (NewObstacle.radius + Obstaclei.radius + MaxObstacleDistance):
              valid = False
              break;
      if valid:
          Obstacles.append(NewObstacle)

def Filereader():
    '''opens a file dialog and returns width, height and filename'''
    filename = fd.askopenfilename()           # Open file dialog
    f = open(filename, "r")                   # Open file
    for i in f:
        Lines.append(i)                       # Appends strings to list
    width, height = Lines[1].split(" ")      
    f.close()                                 # Close file
    return int(width), int(height), filename

def Playmode1():
    '''initializes Mode 1'''
    GameMode = 1
    run_button.changehandler(Run1)
    init(WindowWidth, WindowHeight, win, 1)
    play1_button.deactivate()
    play2_button.deactivate()
    play3_button.deactivate()
    play4_button.deactivate()
    reset_button.deactivate()
    infolabel1.draw(win)
    infolabel2.draw(win)
    infolabel4.draw(win)
    infolabel5.draw(win)
    infolabel6.draw(win)
    infolabel7.draw(win)
    while True:
        click1 = win.checkMouse()
        if click1 != None:
            if IsInside(click1.getX(), click1.getY()):
                Goal.append(Tree(click1.getX(), click1.getY(), win))     # Append Tree to Goal list
                infolabel7.setText(len(Goal))
                infolabel1.undraw()
                infolabel2.undraw()
                run_button.activate()
                CheckButtons(win)
                break

def Run1():
    '''Runs Mode 1'''
    run_button.deactivate()
    reset_button.deactivate()
    while True:
        CheckButtons(win)
        Clock(myrobot.Sonar(Goal).getX(), myrobot.Sonar(Goal).getY(),myrobot,win)
        if myrobot.Stop(Goal) == 1:
            myrobot.Grab(myrobot.Sonar(Goal))
            Goal.remove(myrobot.Sonar(Goal))                             # Remove closest Tree from Goal
            infolabel7.setText(len(Goal))                                # Updates label
            break
    while True:
        CheckButtons(win)
        Clock(myrobot.Sonar(Chargers).getX(), myrobot.Sonar(Chargers).getY(), myrobot, win)
        if myrobot.getX() - myrobot.Sonar(Chargers).getX() < 1 and myrobot.getY() - myrobot.Sonar(Chargers).getY() < 1:
            reset_button.activate()
            break
    infolabel3.draw(win)
    clicktoreset = win.getMouse()                                        # Click to reset
    infolabel3.undraw()
    Reset()

def Playmode2():
    '''initializes Mode 2'''
    GameMode = 2
    run_button.changehandler(Run2)
    init(WindowWidth, WindowHeight, win, 1)
    play1_button.deactivate()
    play2_button.deactivate()
    play3_button.deactivate()
    play4_button.deactivate()

    infolabel4.draw(win)
    infolabel5.draw(win)
    infolabel6.draw(win)
    infolabel7.draw(win)
    Generatefield(win)
    infolabel5.setText(len(Obstacles))
    while True:
        click = win.checkMouse()
        if click != None:
            a = True
            for i in Obstacles:
                if distance(Point(i.PosX,i.PosY), Point(click.getX(), click.getY())) < 20:  # Doesn't let place Tree if it is too close to an Object
                    a = False
            if IsInside(click.getX(), click.getY()) and a:
                Goal.append(Tree(click.getX(), click.getY(), win))    # Append Tree to Goal list
                infolabel7.setText(str(len(Goal)))                    # Updates label
                run_button.activate()
            if run_button.clicked(click):
                break
    Run2()

def Run2():
    '''Runs Mode 2'''
    run_button.deactivate()
    Findpath(Obstacles, myrobot.getPos(), Goal[0], win, Path)
    for point in Path:
        while distance(point, myrobot.Pos) > 1:
            CheckButtons(win)
            update(200)
            Clock(point.getX(), point.getY(),myrobot,win)
            if myrobot.Stop(Goal) == 1:
                myrobot.Grab(myrobot.Sonar(Goal))
                Goal.remove(myrobot.Sonar(Goal))                      # Remove closest Tree from Goal
                infolabel7.setText(len(Goal))                         # Updates label
                break       
    while len(Goal) > 0:
        if myrobot.Battery >25:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Goal), win, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    CheckButtons(win)
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot,win)
                    if myrobot.Stop(Goal) == 1:
                        myrobot.Grab(myrobot.Sonar(Goal))
                        Goal.remove(myrobot.Sonar(Goal))              # Remove closest Tree from Goal
                        infolabel7.setText(len(Goal))                 # Updates label
                        break
        else:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Chargers), win, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot,win)
                    if myrobot.Battery >=100:
                        break
    infolabel3.draw(win)
    clicktoreset = win.getMouse()                                     # Click to reset
    infolabel3.undraw()
    Reset()

def Playmode3():
    '''initializes Mode 3 - Choose'''
    GameMode = 3
    play1_button.deactivate()
    play2_button.deactivate()
    play3_button.deactivate()
    play4_button.deactivate()
    global win2
    win2 = GraphWin("Choose", WindowWidth/2, WindowHeight/2, autoflush=False)
    button_file = Button(win2, Point(WindowWidth/4, WindowHeight*(1/6)), 2*TabSize, 2*ButtonsHeight, "Read from a file", Playmode3file)
    button_random = Button(win2, Point(WindowWidth/4, WindowHeight*(2/6)), 2*TabSize, 2*ButtonsHeight, "Random map", Playmode3random)
    Buttons.append(button_file)
    Buttons.append(button_random)
    while True:
        CheckButtons(win2)

def Playmode3file():
    '''initializes Mode 3 - Read from a file selection'''
    win2.close()
    Buttons.clear()
    width, height, filename = Filereader()
    global win3
    win3 = GraphWin("Mode 3", width, height, autoflush=False)
    init(width, height, win3, 3)
    Lines = []
    f = open(filename, "r")                                                # Open file
    for i in f:
        Lines.append(i)                                                    # Apppend strings to Lines
    f.close()                                                              # Close file
    for i in range(3, len(Lines)):                                         # Read values
        Type, PosX, PosY = Lines[i].split(" ")
        Obstacles.append(Obstacle(TabSize + (float(PosX)/100)*(width-2*TabSize), (float(PosY)/100)*height, int(Type), win3))
        infolabel8.setText(len(Obstacles))                                 # Update label
  
    while True:
        click = win3.checkMouse()
        if click != None:
            a = True
            for i in Obstacles:
                if distance(Point(i.PosX,i.PosY), Point(click.getX(), click.getY())) < 20:
                    a = False
            if TabSize<click.getX()<width-TabSize and a:
                Goal.append(Tree(click.getX(), click.getY(), win3))
                infolabel9.setText(len(Goal))                              # Update label
                run_button_3.activate()
            if run_button_3.clicked(click):
                break
    Run3file(width,height)

def Run3file(width,height):
    '''Runs Mode 3 - Read from a file selection'''
    run_button_3.deactivate()
    Findpath(Obstacles, myrobot.getPos(), Goal[0], win3, Path)
    for point in Path:                                                     #
        while distance(point, myrobot.Pos) > 1:
            update(200)
            Clock(point.getX(), point.getY(),myrobot,win3)
            if myrobot.Stop(Goal) == 1:
                myrobot.Grab(myrobot.Sonar(Goal))
                Goal.remove(myrobot.Sonar(Goal))                           # Remove closest Tree from Goal
                infolabel9.setText(len(Goal))                              # Update label
                break
    while len(Goal) > 0:
        if myrobot.Battery >25:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Goal), win3, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot,win3)
                    if myrobot.Stop(Goal) == 1:
                        myrobot.Grab(myrobot.Sonar(Goal))
                        Goal.remove(myrobot.Sonar(Goal))                   # Remove closest Tree from Goal
                        infolabel9.setText(len(Goal))                      # Update label
                        break
        else:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Chargers), win3, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot,win3)
                    if myrobot.Battery >=100:
                        break
    infolabel10 = Text(Point(width/2, height/2), "Click to Reset")
    infolabel10.setFace('courier')
    infolabel10.setSize(10)
    infolabel10.draw(win3)
    clicktoclose = win3.getMouse()                                         # Click to reset
    infolabel10.undraw()
    win3.close()
    win.close()
    
def Playmode3random():
    '''initializes Mode 3 - Random map selection'''
    win2.close()
    global win4
    win4 = GraphWin("Mode 3", WindowWidth, WindowHeight, autoflush=False)
    init(WindowWidth, WindowHeight, win4, 2)
    Generatefield(win4)
    infolabel5.setText(len(Obstacles))                                     # Update label
    while True:
        click = win4.checkMouse()
        if click != None:
            a = True
            for i in Obstacles:
                if distance(Point(i.PosX,i.PosY), Point(click.getX(), click.getY())) < 20:
                    a = False
            if TabSize<click.getX()<WindowWidth-TabSize and a:
                Goal.append(Tree(click.getX(), click.getY(), win4))
                infolabel7.setText(len(Goal))                              # Update label
                run_button_2.activate()
            if run_button_2.clicked(click):
                break
    Run3random()
    
def Run3random():
    '''Runs 3 - Random map selection'''
    run_button_2.deactivate()
    Findpath(Obstacles, myrobot.getPos(), Goal[0], win4, Path)
    for point in Path:
        while distance(point, myrobot.Pos) > 1:
            update(200)
            Clock(point.getX(), point.getY(),myrobot,win4)
            if myrobot.Stop(Goal) == 1:
                myrobot.Grab(myrobot.Sonar(Goal))
                Goal.remove(myrobot.Sonar(Goal))                           # Remove closest Tree from Goal
                infolabel7.setText(len(Goal))                              # Update label
                break
    while len(Goal) > 0:
        if myrobot.Battery >25:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Goal), win4, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot, win4)
                    if myrobot.Stop(Goal) == 1:
                        myrobot.Grab(myrobot.Sonar(Goal))
                        Goal.remove(myrobot.Sonar(Goal))                   # Remove closest Tree from Goal
                        infolabel7.setText(len(Goal))                      # Update label
                        break
        else:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Chargers), win4, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot, win4)
                    if myrobot.Battery >=100:
                        break
    infolabel3.draw(win4)
    clicktoclose = win4.getMouse()                                         # Click to reset
    infolabel3.undraw()
    win4.close()
    win.close()
    
def Playmode4():
    '''initializes Mode 4 - Choose'''
    GameMode = 4
    play1_button.deactivate()
    play2_button.deactivate()
    play3_button.deactivate()
    play4_button.deactivate()
    global win5
    win5 = GraphWin("Choose", WindowWidth/2, WindowHeight/2, autoflush=False)
    button_file = Button(win5, Point(WindowWidth/4, WindowHeight*(1/6)), 2*TabSize, 2*ButtonsHeight, "Read from a file", Playmode4file)
    button_random = Button(win5, Point(WindowWidth/4, WindowHeight*(2/6)), 2*TabSize, 2*ButtonsHeight, "Random map", Playmode4random)
    Buttons.append(button_file)
    Buttons.append(button_random)
    while win5 != 0:
        CheckButtons(win5)

def Playmode4file():
    '''initializes Mode 4 - Read from a file selection'''
    win5.close()
    Buttons.clear()
    width=WindowWidth
    height=WindowHeight
    filename = fd.askopenfilename()
    global win7
    win7 = GraphWin("Mode 4", width, height, autoflush=False)
    init(WindowWidth, WindowHeight, win7, 2)
    f = open(filename, "r")                                 # Open a file 
    for i in f:
        Lines.append(i)                                     # Append strings to Lines list
    f.close()                                               # Close file
    for i in range(1, len(Lines)):
        PosX, PosY = Lines[i].split(" ")
        Goal.append(Tree(float(PosX)/100*width, float(PosY)/100*height, win7))
        infolabel7.setText(len(Goal))                       # Update label
    Generatefield(win7)
    infolabel5.setText(len(Obstacles))                      # Update label
    run_button_2.activate()
    while True:
        click = win7.checkMouse()
        if click != None:
            if run_button_2.clicked(click):
                run_button_2.deactivate()
                break
    Run4file()

def Run4file():
    '''Runs Mode 4 - Read from a file selection'''
    run_button_2.deactivate()
    Findpath(Obstacles, myrobot.getPos(), Goal[0], win7, Path)
    for point in Path:
        while distance(point, myrobot.Pos) > 1:
            update(200)
            Clock(point.getX(), point.getY(),myrobot,win7)
            if myrobot.Stop(Goal) == 1:
                myrobot.Grab(myrobot.Sonar(Goal))
                Goal.remove(myrobot.Sonar(Goal))                   # Remove closest Tree from Goal
                infolabel7.setText(len(Goal))                      # Update label
                break
    while len(Goal) > 0:
        if myrobot.Battery >25:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Goal), win7, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot, win7)
                    if myrobot.Stop(Goal) == 1:
                        myrobot.Grab(myrobot.Sonar(Goal))
                        Goal.remove(myrobot.Sonar(Goal))           # Remove closest Tree from Goal
                        infolabel7.setText(len(Goal))              # Update label
                        break
        else:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Chargers), win7, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot, win7)
                    if myrobot.Battery >=100:
                        break
    infolabel3.draw(win7)
    clicktoclose = win7.getMouse()                                 # Click to reset
    infolabel3.undraw()
    win7.close()
    win.close()
    
def Playmode4random():
    '''initializes Mode 4 - Random map selection'''
    win5.close()
    global win6
    win6 = GraphWin("Mode 4", WindowWidth, WindowHeight, autoflush=False)
    init(WindowWidth, WindowHeight, win6, 2)
    Generatefield(win6)
    infolabel5.setText(len(Obstacles))                             # Update label
    while True:
        click = win6.checkMouse()
        if click != None:
            a = True
            for i in Obstacles:
                if distance(Point(i.PosX,i.PosY), Point(click.getX(), click.getY())) < 20:
                    a = False
            if TabSize<click.getX()<WindowWidth-TabSize and a:
                Goal.append(Tree(click.getX(), click.getY(), win6))
                infolabel7.setText(len(Goal))                       # Update label
                run_button_2.activate()
            if run_button_2.clicked(click):
                break
    Run4random()
    
def Run4random():
    '''Runs Mode 4 - Random map selection'''
    run_button_2.deactivate()
    Findpath(Obstacles, myrobot.getPos(), Goal[0], win6, Path)
    for point in Path:
        while distance(point, myrobot.Pos) > 1:
            update(200)
            Clock(point.getX(), point.getY(),myrobot,win6)
            if myrobot.Stop(Goal) == 1:
                myrobot.Grab(myrobot.Sonar(Goal))
                Goal.remove(myrobot.Sonar(Goal))                    # Remove closest Tree from Goal
                infolabel7.setText(len(Goal))                       # Update label
                break
    while len(Goal) > 0:
        if myrobot.Battery >25:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Goal), win6, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot, win6)
                    if myrobot.Stop(Goal) == 1:
                        myrobot.Grab(myrobot.Sonar(Goal))
                        Goal.remove(myrobot.Sonar(Goal))            # Remove closest Tree from Goal
                        infolabel7.setText(len(Goal))               # Update label
                        break
        else:
            Path.clear()
            Findpath(Obstacles, myrobot.getPos(), myrobot.Sonar(Chargers), win6, Path)
            for point in Path:
                while distance(point, myrobot.Pos) > 1:
                    update(200)
                    Clock(point.getX(), point.getY(), myrobot, win6)
                    if myrobot.Battery >=100:
                        break
    infolabel3.draw(win6)
    clicktoclose = win6.getMouse()                                  # Click to reset
    infolabel3.undraw()
    win6.close()
    win.close()
   
def init(WindowWidth, WindowHeight, win, Type):
    '''initializes win according to Width, Height and Type''' 
    if Type==2:
        lefttab = Rectangle(Point(0, WindowHeight), Point(TabSize, 0))
        righttab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
        lefttab.setFill("light grey")
        righttab.setFill("light grey")
        lefttab.draw(win)
        righttab.draw(win)
        infolabel4.draw(win)
        infolabel5.draw(win)
        infolabel6.draw(win)
        infolabel7.draw(win)
        global run_button_2
        run_button_2 = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Run", Run3random)
        run_button_2.deactivate()
    elif Type==3:
        lefttab = Rectangle(Point(0, WindowHeight), Point(TabSize, 0))
        righttab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
        lefttab.setFill("light grey")
        righttab.setFill("light grey")
        lefttab.draw(win)
        righttab.draw(win)
        infolabel11 = Text(Point(WindowWidth-TabSize/2, ButtonsVerticalSpacement*3), "Obstacles:")
        global infolabel8
        infolabel8 = Text(Point(WindowWidth-TabSize/2, ButtonsVerticalSpacement*3.5), "0")
        infolabel12 = Text(Point(WindowWidth-TabSize/2, ButtonsVerticalSpacement*4), "Trees:")
        global infolabel9
        infolabel9 = Text(Point(WindowWidth-TabSize/2, ButtonsVerticalSpacement*4.5), "0")
        infolabel11.setFace('courier')        #Enhancement
        infolabel8.setFace('courier')
        infolabel12.setFace('courier')
        infolabel9.setFace('courier')
        infolabel11.setSize(10)
        infolabel8.setSize(10)
        infolabel12.setSize(10)
        infolabel9.setSize(10)
        infolabel11.draw(win)                 #Draw
        infolabel8.draw(win)
        infolabel12.draw(win)
        infolabel9.draw(win)
        global run_button_3
        run_button_3 = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Run", Run3random)
        run_button_3.deactivate()
    
    #Battery figure
    global rec1
    global rec2
    global rec3
    global rec4
    global rec5
    global bar1
    global bar2
    global bar3
    global bar4
    global Dock
    global batteryinfo
    global batterylabel
    rec1 = Rectangle(Point(WindowWidth-TabSize/2-15, ButtonsVerticalSpacement-5), Point(WindowWidth-TabSize/2+14, ButtonsVerticalSpacement-6))
    rec2 = Rectangle(Point(WindowWidth-TabSize/2-15, ButtonsVerticalSpacement+6), Point(WindowWidth-TabSize/2+14, ButtonsVerticalSpacement+5))
    rec3 = Rectangle(Point(WindowWidth-TabSize/2-15, ButtonsVerticalSpacement+6), Point(WindowWidth-TabSize/2-14, ButtonsVerticalSpacement-6))
    rec4 = Rectangle(Point(WindowWidth-TabSize/2+14, ButtonsVerticalSpacement+6), Point(WindowWidth-TabSize/2+13, ButtonsVerticalSpacement-6))
    rec5 = Rectangle(Point(WindowWidth-TabSize/2+17, ButtonsVerticalSpacement+5), Point(WindowWidth-TabSize/2+16, ButtonsVerticalSpacement-5))
    bar1 = Rectangle(Point(WindowWidth-TabSize/2-12,ButtonsVerticalSpacement+4),Point(WindowWidth-TabSize/2-7,ButtonsVerticalSpacement-3))
    bar2 = Rectangle(Point(WindowWidth-TabSize/2-6,ButtonsVerticalSpacement+4),Point(WindowWidth-TabSize/2-1,ButtonsVerticalSpacement-3))
    bar3 = Rectangle(Point(WindowWidth-TabSize/2,ButtonsVerticalSpacement+4),Point(WindowWidth-TabSize/2+5,ButtonsVerticalSpacement-3))
    bar4 = Rectangle(Point(WindowWidth-TabSize/2+6,ButtonsVerticalSpacement+4),Point(WindowWidth-TabSize/2+11,ButtonsVerticalSpacement-3))
    bars.append(bar1)                           # Append to bars list
    bars.append(bar2)
    bars.append(bar3)
    bars.append(bar4)
    Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)
    batteryinfo = Text(Point(WindowWidth - TabSize/2, 100), '100 %')
    batterylabel = Text(Point(WindowWidth - TabSize/2, 80), 'Battery')
    rec1.setFill('black')               #Enhancement
    rec2.setFill('black')
    rec3.setFill('black')
    rec4.setFill('black')
    rec5.setFill('black')
    bar1.setFill('green3')
    bar2.setFill('green3')
    bar3.setFill('green3')
    bar4.setFill('green3')
    bar1.setWidth(0)
    bar2.setWidth(0)
    bar3.setWidth(0)
    bar4.setWidth(0)
    Dock.setFill("light grey")
    batteryinfo.setFace('courier')
    batterylabel.setFace('courier')
    batteryinfo.setSize(10)
    batterylabel.setSize(10)
    rec1.draw(win)                       #Draw
    rec2.draw(win)
    rec3.draw(win)
    rec4.draw(win)
    rec5.draw(win)
    bar1.draw(win)
    bar2.draw(win)
    bar3.draw(win)
    bar4.draw(win)
    Dock.draw(win)
    batteryinfo.draw(win)
    batterylabel.draw(win)
    
    #Chargers
    RightCharger = Charger(WindowWidth - TabSize - 20, 20, win)
    LeftCharger = Charger(TabSize + 20, 20, win)
    Chargers.append(RightCharger)        # Append to Chargers list
    Chargers.append(LeftCharger)
    
    #Create robot object
    global myrobot
    myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win, Chargers)
 
def Reset():
    '''Resets win and clears Global Lists'''
    play1_button.activate()              # Activate modes buttons
    play2_button.activate()
    play3_button.activate()
    play4_button.activate()
    reset_button.deactivate()            # Deactivate "Reset" button
    run_button.deactivate()              # Deactivate "Run" button
    rec1.undraw()                        # Undraw
    rec2.undraw()
    rec3.undraw()
    rec4.undraw()
    rec5.undraw()
    batteryinfo.undraw()
    batterylabel.undraw()
    infolabel4.undraw()
    infolabel5.undraw()
    infolabel6.undraw()
    infolabel7.undraw()
    Dock.undraw()
    myrobot.undraw()
    myrobot.delete()                     # Deletes robot
    for i in Path:
        i.undraw()
    for i in bars:
        i.undraw()
    for i in Chargers:
        i.undraw()
        i.delete()
    for i in Obstacles:
        i.undraw()
        i.delete()
    for i in Goal:
        i.undraw()
        i.delete()
    bars.clear()                         # Clears lists                  
    Goal.clear()
    Lines.clear()
    Path.clear()
    Chargers.clear()
    Obstacles.clear()

def Clock(obsX, obsY, myrobot, win):
    '''Makes movement and updates battery bars in a given Window'''
    for i in bars:
        i.undraw()                       # Undraws all bars
    if myrobot.Batterylevel == 4:        # Draw 4 bars
        for i in bars:
            i.setFill('green3')          # Green color
            i.draw(win)
    elif myrobot.Batterylevel == 3:      # Draw 3 bars
        for i in bars:
            i.setFill('yellow')          # Yellow color
        bar1.draw(win)
        bar2.draw(win)
        bar3.draw(win)
    elif myrobot.Batterylevel == 2:      # Draw 2 bars
        for i in bars:
            i.setFill('dark orange')     # Orange color
        bar1.draw(win)
        bar2.draw(win)
    else:                                # Draw 1 bar
        for i in bars:
            i.setFill('red')             # Red color
        bar1.draw(win)
    myrobot.Charge()
    batteryinfo.setText(str(myrobot.getBattery()) +' %')         # Update label
    time.sleep(0.01)
    myrobot.Seek(obsX, obsY)

if __name__ == "__main__":  
    main()