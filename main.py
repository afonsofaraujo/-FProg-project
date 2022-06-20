# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:15 2022

@author: Afonso Araújo
"""

from graphics import *
from Harve import *
from Tree import *
from Charger import *
from Obstacle import *
from PathplanningRRT import *
from Button_modified import *
from math import *
from Pathfind import *
import time

#Global lists
Obstacles = []
Goal = []
Objects = []   
Buttons = []    
Chargers = []

#Variables
#global GameMode
GameMode = 0   #default 0
WindowWidth = 800
WindowHeight = 600
TabSize = 100
ButtonsVerticalSpacement = 50
ButtonsHeight = 30
ObstaclesSize = 5               #radius

win = GraphWin("GAME", WindowWidth, WindowHeight, autoflush=False)
LeftTab = Rectangle(Point(0,WindowHeight), Point(TabSize,0))
LeftTab.setFill("light grey")
RightTab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
RightTab.setFill("light grey")

def main(): 
    global play2_button
    global play1_button
    global reset_button
    global quit_button
    global run_button
    global reset_button
    
    LeftTab.draw(win)
    RightTab.draw(win)
    play2_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*5), (2/3)*TabSize, ButtonsHeight, "Mode 2", Playmode2)
    play1_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Mode 1", Playmode1)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement), (2/3)*TabSize, ButtonsHeight, "Reset", Reset)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Run", Run1)
    reset_button.deactivate()
    run_button.deactivate()
    
    Buttons.append(quit_button)
    Buttons.append(reset_button)
    Buttons.append(play1_button)
    Buttons.append(play2_button)
    Buttons.append(run_button)
    
    
    while True:
        CheckButtons()
    
    
    
def Playmode1():
    GameMode = 1
    run_button.changehandler(Run1)
    print('GameMode is now ',GameMode)
    init(win)
    play1_button.deactivate()
    CheckButtons()
    while True:
        click1 = win.checkMouse()
        if click1 != None:
            if IsInside(click1.getX(), click1.getY()):
                Objects.append(Tree(click1.getX(), click1.getY(), win))
                reset_button.activate()
                run_button.activate()
                CheckButtons()
                break
    
def Playmode2():
    GameMode = 2
    run_button.changehandler(Run2)
    print('GameMode is now ', GameMode)
    init(win)
    play2_button.deactivate()
    play1_button.deactivate()
    reset_button.activate()            
    
    
    #later this can be generated with random or chaotic function
    Obstacles.append(Obstacle(200, 350, 0, win))
    Obstacles.append(Obstacle(620, 140, 0, win))
    Obstacles.append(Obstacle(560, 200, 1, win))
    Obstacles.append(Obstacle(400, 300, 2, win))
    Obstacles.append(Obstacle(300, 350, 2, win))
                
    while True:
        click = win.checkMouse()
        if click != None:
            a = True
            for i in Obstacles:
                if distance(Point(i.PosX,i.PosY), Point(click.getX(),click.getY())) < 10:
                    a = False
            if IsInside(click.getX(), click.getY()) and a:
                tree = Tree(click.getX(), click.getY(), win)
                pt = Point(click.getX(),click.getY())
                Goal.append(pt)
                print(len(Goal))
                run_button.activate()
        CheckButtons()
            

def init(win):
    global Dock
    Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)
    Dock.setFill("light grey")
    Dock.draw(win)
    
    RightCharger = Charger(WindowWidth - TabSize - 20, 20, win)
    LeftCharger = Charger(TabSize + 20, 20, win)
    Chargers.append(RightCharger)
    Chargers.append(LeftCharger)
    
    global batteryinfo
    batteryinfo = Text(Point(WindowWidth - TabSize/2, 100), '100 %')
    batteryinfo.setFace('courier')
    batteryinfo.setSize(10)
    batteryinfo.draw(win)
    
    global batterylabel
    batterylabel = Text(Point(WindowWidth - TabSize/2, 80), 'Battery')
    batterylabel.setFace('courier')
    batterylabel.setSize(10)
    batterylabel.draw(win)
    
    global myrobot
    myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win)
    
def CheckButtons():
    mouse = win.checkMouse()
    if mouse != None:
        for Button in Buttons:
            if Button.clicked(mouse):
                Button.onClick()
                Button.deactivate()
                return True

def IsInside(x,y):
    return (TabSize < x < (WindowWidth - TabSize))

def Reset():
    reset_button.deactivate()
    play1_button.activate()
    run_button.deactivate()
    Dock.undraw()
    myrobot.undraw()
    myrobot.delete()
    batteryinfo.undraw()
    for Charger in Chargers:
        Charger.undraw()
        Charger.delete()
    Chargers.clear()
    for Object in Objects:
        Object.undraw()
        Object.delete()
    Objects.clear()
    
def Quit():
    win.close()
    
def Run1():
    run_button.deactivate()
    while True:
        CheckButtons()
        Clock(myrobot.Sonar(Objects).getX(), myrobot.Sonar(Objects).getY())
        if myrobot.Stop(Objects) == 1:
            myrobot.Grab(myrobot.Sonar(Objects))
            break

    #starts the new movement to go to the charger
    while True:
        CheckButtons()
        Clock(myrobot.Sonar(Chargers).getX(), myrobot.Sonar(Chargers).getY())
        if myrobot.getX() - myrobot.Sonar(Chargers).getX() < 1 and myrobot.getY() - myrobot.Sonar(Chargers).getY() < 1:
            print('-----------done-------------')
            run_button.deactivate()
            break
    CheckButtons()

def Run2():
    
    print(len(Obstacles),'Obstacles')
    print(len(Goal),'Goals')
    
    for i in Goal:
        encontrar_caminho(obst, myrobot.getPos(), objetivo)
        
    
    '''run_button.deactivate()
    print('-----------------Run2--------------------')
    lstPath = []
    
    for i in Goal:
        print('Obstacles: ',len(Obstacles))
        print(myrobot.getPos())
        Path = pathplanning(Obstacles, i, myrobot.getPos())
        print('Path: ',len(Path))
        for ii in Path:
            print('drawing path')
            c = Circle(ii,5)
            c.setFill('red')
            c.draw(win)
        lstPath.append(Path)   
                             
    for i in lstPath:                    
        for ii in i:
            while myrobot.getX()!= ii.getX() and myrobot.getY() != ii.getY():             #enquanto ainda não estiver lá
                Clock(ii.getX(),ii.getY())
            
             #anda de node em node
            #condição para ele parar e apanhar arvore
    '''
def Clock(obsX, obsY):       #Harve module after this
    batteryinfo.setText(str(myrobot.getBattery()) +' %')
    time.sleep(0.01)
    myrobot.Seek(obsX, obsY)

        
if __name__ == "__main__":  
    main()