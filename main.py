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
#from PathplanningRRT import *
from Button_modified import *
from math import *
from a1234 import *
import random
import time

#Global lists
Obstacles = []
Goal = []
Objects = []   
Buttons = []
Chargers = []
bars = []
global Path
Path = []

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
rec1 = Rectangle(Point(WindowWidth-TabSize/2-15,ButtonsVerticalSpacement -5),Point(WindowWidth-TabSize/2 +14,ButtonsVerticalSpacement-6))
rec2 = Rectangle(Point(WindowWidth-TabSize/2-15,ButtonsVerticalSpacement +6),Point(WindowWidth-TabSize/2 +14,ButtonsVerticalSpacement+5))
rec3 = Rectangle(Point(WindowWidth-TabSize/2-15,ButtonsVerticalSpacement+6),Point(WindowWidth-TabSize/2-14,ButtonsVerticalSpacement-6))
rec4 = Rectangle(Point(WindowWidth-TabSize/2+14,ButtonsVerticalSpacement+6),Point(WindowWidth-TabSize/2+13,ButtonsVerticalSpacement-6))
rec5 = Rectangle(Point(WindowWidth-TabSize/2+17,ButtonsVerticalSpacement+5),Point(WindowWidth-TabSize/2+16,ButtonsVerticalSpacement-5))
rec1.setFill('black')
rec2.setFill('black')
rec3.setFill('black')
rec4.setFill('black')
rec5.setFill('black')

def main(): 
    global play2_button
    global play1_button
    global reset_button
    global quit_button
    global run_button
    global reset_button
    
    LeftTab.draw(win)
    RightTab.draw(win)
    play1_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Mode 1", Playmode1)
    play2_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*5), (2/3)*TabSize, ButtonsHeight, "Mode 2", Playmode2)
    #play3_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*6), (2/3)*TabSize, ButtonsHeight, "Mode 3", Playmode3)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement), (2/3)*TabSize, ButtonsHeight, "Reset", Reset)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Run", Run1)
    reset_button.deactivate()
    run_button.deactivate()
    
    Buttons.append(quit_button)
    Buttons.append(reset_button)
    Buttons.append(play1_button)
    Buttons.append(play2_button)
    #Buttons.append(play3_button)
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
            
def Generatefield():
    
    Obstacles.append(Obstacle(random.randint(TabSize+20,780-TabSize), random.randint(TabSize+20,580-TabSize), 0, win))
    Obstacles.append(Obstacle(random.randint(TabSize+20,780-TabSize), random.randint(TabSize+20,580-TabSize), 0, win))
    Obstacles.append(Obstacle(random.randint(TabSize+20,780-TabSize), random.randint(TabSize+20,580-TabSize), 1, win))
    Obstacles.append(Obstacle(random.randint(TabSize+20,780-TabSize), random.randint(TabSize+20,580-TabSize), 2, win))
    Obstacles.append(Obstacle(random.randint(TabSize+20,780-TabSize), random.randint(TabSize+20,580-TabSize), 2, win))   
    
def Playmode2():
    GameMode = 2
    run_button.changehandler(Run2)
    print('GameMode is now ', GameMode)
    init(win)
    play2_button.deactivate()
    play1_button.deactivate()
    reset_button.activate()
            
    Generatefield()   
    
    while True:
        #CheckButtons()
        click = win.checkMouse()
        if click != None:
            a = True
            for i in Obstacles:
                if distance(Point(i.PosX,i.PosY), Point(click.getX(),click.getY())) < 10:
                    a = False
            if IsInside(click.getX(), click.getY()) and a:
                Goal.append(Tree(click.getX(), click.getY(), win))
                print(len(Goal))
                run_button.activate()
            if run_button.clicked(click):
                break
        #CheckButtons()
    run_button.deactivate()
    Run2()

'''def Playmode3():
    GameMode = 3
    run_button.changehandler(Run3)
    print('GameMode is now ', GameMode)
    init(win)
    play2_button.deactivate()
    play1_button.deactivate()
    play3_button.deactivate()
    reset_button.activate()
    
def Run3():
    pass'''

def init(win):
    
    rec1.draw(win)
    rec2.draw(win)
    rec3.draw(win)
    rec4.draw(win)
    rec5.draw(win)
    
    global bar1
    bar1 = Rectangle(Point(WindowWidth-TabSize/2-12,ButtonsVerticalSpacement+4),Point(WindowWidth-TabSize/2-7,ButtonsVerticalSpacement-3))
    bar1.setFill('green3')
    bar1.setWidth(0)
    bar1.draw(win)
    
    global bar2
    bar2 = Rectangle(Point(WindowWidth-TabSize/2-6,ButtonsVerticalSpacement+4),Point(WindowWidth-TabSize/2-1,ButtonsVerticalSpacement-3))
    bar2.setFill('green3')
    bar2.setWidth(0)
    bar2.draw(win)
    
    global bar3
    bar3 = Rectangle(Point(WindowWidth-TabSize/2,ButtonsVerticalSpacement+4),Point(WindowWidth-TabSize/2+5,ButtonsVerticalSpacement-3))
    bar3.setFill('green3')
    bar3.setWidth(0)
    bar3.draw(win)
    
    global bar4
    bar4 = Rectangle(Point(WindowWidth-TabSize/2+6,ButtonsVerticalSpacement+4),Point(WindowWidth-TabSize/2+11,ButtonsVerticalSpacement-3))
    bar4.setFill('green3')
    bar4.setWidth(0)
    bar4.draw(win)
    
    global Dock
    Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)
    Dock.setFill("light grey")
    Dock.draw(win)
    
    bars.append(bar1)
    bars.append(bar2)
    bars.append(bar3)
    bars.append(bar4)
    
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
    myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win, Chargers)
    
def CheckButtons():
    mouse = win.checkMouse()
    if mouse != None:
        for Button in Buttons:
            if Button.clicked(mouse):
                Button.onClick()
                return True

def IsInside(x,y):
    return (TabSize < x < (WindowWidth - TabSize))

def Reset():
    reset_button.deactivate()
    play1_button.activate()
    play2_button.activate()
    run_button.deactivate()
    rec1.undraw()
    rec2.undraw()
    rec3.undraw()
    rec4.undraw()
    rec5.undraw()
    batteryinfo.undraw()
    batterylabel.undraw()
    Dock.undraw()
    myrobot.undraw()
    myrobot.delete()
    batteryinfo.undraw()
    for i in Path:
        i.undraw()
    Path.clear()
    for i in bars:
        i.undraw()
    bars.clear()
    for i in Chargers:
        i.undraw()
        i.delete()
    Chargers.clear()
    for i in Objects:
        i.undraw()
        i.delete()
    Objects.clear()
    for i in Obstacles:
        i.undraw()
        i.delete()
    Obstacles.clear()
    for i in Goal:
        i.undraw()
    Goal.clear()
   
    
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
    print('-----------Run2-------------')
    print(len(Obstacles),'Obstacles')
    print(len(Goal),'Goals')
    
    encontrar_caminho(Obstacles, myrobot.getPos(), Goal[0], myrobot, win, Path)
    
    
    
    
    '''lstPath = []
    
    #scout
    for i in Goal:
        print(myrobot.getPos())
        Path = pathplanning(Obstacles, i, myrobot.getPos())
        print('Path: ',len(Path))   
        for ii in Path:
            c = Point(ii.getX(),ii.getY())
            c.setFill('red')
            c.draw(win)
            time.sleep(0.1)
       # lstPath.append(Path)
    
        
        
        
     
    #move              
    for i in lstPath:                    
        for ii in i:
            while distance(myrobot,ii)>10:
                Clock(ii.getX(),ii.getY())
                time.sleep(0.2)'''
    print('-----------done-------------')
    
    #CheckButtons()
           
    
def Clock(obsX, obsY):       #Harve module after this
    for i in bars:
        i.undraw()
    if myrobot.Batterylevel == 4:
        for i in bars:
            i.setFill('green3')
            i.draw(win)
    elif myrobot.Batterylevel == 3:
        for i in bars:
            i.setFill('yellow')
        bar1.draw(win)
        bar2.draw(win)
        bar3.draw(win)
    elif myrobot.Batterylevel == 2:
        for i in bars:
            i.setFill('dark orange')
        bar1.draw(win)
        bar2.draw(win)
    else:
        for i in bars:
            i.setFill('red')
        bar1.draw(win)
        
    myrobot.Charge()
    batteryinfo.setText(str(myrobot.getBattery()) +' %')
    time.sleep(0.01)
    myrobot.Seek(obsX, obsY)


if __name__ == "__main__":  
    main()