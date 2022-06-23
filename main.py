# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:15 2022

@author: Afonso Araújo
"""

from random import randint
import time
from tkinter import filedialog as fd

from graphics import *
from Harve import *
from Tree import *
from Charger import *
from Obstacle import *
from Button_modified import *
from math import *
from Findpath import *


# Global Lists
Obstacles = []
Goal = []
Objects = []
Buttons = []
Chargers = []
bars = []
global Path
Path = []
global win2
win2 = Point(0,0)
global win3
win3 = Point(0,0)

# Global Variables
GameMode = 0  # 0 mean no gamemode
WindowWidth = 800
WindowHeight = 600
TabSize = 100
ButtonsVerticalSpacement = 50
ButtonsHeight = 30
ObstaclesSize = 5  # Radius

# Global Objects
win = GraphWin("GAME", WindowWidth, WindowHeight, autoflush=False)
LeftTab = Rectangle(Point(0, WindowHeight), Point(TabSize, 0))
LeftTab.setFill("light grey")
RightTab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
RightTab.setFill("light grey")

rec1 = Rectangle(Point(WindowWidth-TabSize/2-15, ButtonsVerticalSpacement-5), Point(WindowWidth-TabSize/2+14, ButtonsVerticalSpacement-6))
rec2 = Rectangle(Point(WindowWidth-TabSize/2-15, ButtonsVerticalSpacement+6), Point(WindowWidth-TabSize/2+14, ButtonsVerticalSpacement+5))
rec3 = Rectangle(Point(WindowWidth-TabSize/2-15, ButtonsVerticalSpacement+6), Point(WindowWidth-TabSize/2-14, ButtonsVerticalSpacement-6))
rec4 = Rectangle(Point(WindowWidth-TabSize/2+14, ButtonsVerticalSpacement+6), Point(WindowWidth-TabSize/2+13, ButtonsVerticalSpacement-6))
rec5 = Rectangle(Point(WindowWidth-TabSize/2+17, ButtonsVerticalSpacement+5), Point(WindowWidth-TabSize/2+16, ButtonsVerticalSpacement-5))
rec1.setFill('black')
rec2.setFill('black')
rec3.setFill('black')
rec4.setFill('black')
rec5.setFill('black')


def main():
    global play1_button
    global play2_button
    global play3_button
    global reset_button
    global quit_button
    global run_button
    global reset_button
    
    LeftTab.draw(win)
    RightTab.draw(win)
    play1_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Mode 1", Playmode1)
    play2_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*5), (2/3)*TabSize, ButtonsHeight, "Mode 2", Playmode2)
    play3_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*6), (2/3)*TabSize, ButtonsHeight, "Mode 3", Playmode3)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement), (2/3)*TabSize, ButtonsHeight, "Reset", Reset)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Run", Run1)
    reset_button.deactivate()
    run_button.deactivate()

    Buttons.append(quit_button)
    Buttons.append(reset_button)
    Buttons.append(play1_button)
    Buttons.append(play2_button)
    Buttons.append(play3_button)
    Buttons.append(run_button)

    while True:
        CheckButtons(win)


def Playmode1():
    GameMode = 1
    run_button.changehandler(Run1)
    print('GameMode is now ', GameMode)
    init(win)
    play1_button.deactivate()
    reset_button.deactivate()
    CheckButtons(win)
    infolabel1 = Text(Point(WindowWidth/2, WindowHeight/2-ButtonsVerticalSpacement*0.5), "Click to place ")
    infolabel1.setFace('courier')
    infolabel1.setSize(10)
    infolabel1.draw(win)
    infolabel2 = Text(Point(WindowWidth/2, WindowHeight/2+ButtonsVerticalSpacement*0.5), "a Tree and hit Run")
    infolabel2.setFace('courier')
    infolabel2.setSize(10)
    infolabel2.draw(win)
    while True:
        click1 = win.checkMouse()
        if click1 != None:
            if IsInside(click1.getX(), click1.getY()):
                Objects.append(Tree(click1.getX(), click1.getY(), win))
                infolabel1.undraw()
                infolabel2.undraw()
                run_button.activate()
                CheckButtons(win)
                break


def Run1():
    run_button.deactivate()
    reset_button.deactivate()
    while True:
        CheckButtons(win)
        Clock(myrobot.Sonar(Objects).getX(), myrobot.Sonar(Objects).getY())
        if myrobot.Stop(Objects) == 1:
            myrobot.Grab(myrobot.Sonar(Objects))
            break

    while True:
        CheckButtons(win)
        Clock(myrobot.Sonar(Chargers).getX(), myrobot.Sonar(Chargers).getY())
        if myrobot.getX() - myrobot.Sonar(Chargers).getX() < 1 and myrobot.getY() - myrobot.Sonar(Chargers).getY() < 1:
            print('-----------done-------------')
            reset_button.activate()
            break
    infolabel3 = Text(Point(WindowWidth/2, WindowHeight/2), "Click to Reset")
    infolabel3.setFace('courier')
    infolabel3.setSize(10)
    infolabel3.draw(win)
    clicktoreset = win.getMouse()
    infolabel3.undraw()
    Reset()
    CheckButtons(win)


def Generatefield():
    Obstacles.append(Obstacle(randint(TabSize+20, 780-TabSize), randint(TabSize+20, 580-TabSize), 0, win))
    Obstacles.append(Obstacle(randint(TabSize+20, 780-TabSize), randint(TabSize+20, 580-TabSize), 0, win))
    Obstacles.append(Obstacle(randint(TabSize+20, 780-TabSize), randint(TabSize+20, 580-TabSize), 1, win))
    Obstacles.append(Obstacle(randint(TabSize+20, 780-TabSize), randint(TabSize+20, 580-TabSize), 2, win))
    Obstacles.append(Obstacle(randint(TabSize+20, 780-TabSize), randint(TabSize+20, 580-TabSize), 2, win))   
    

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
        # CheckButtons()
        click = win.checkMouse()
        if click != None:
            a = True
            for i in Obstacles:
                if distance(Point(i.PosX,i.PosY), Point(click.getX(), click.getY())) < 20:
                    a = False
            if IsInside(click.getX(), click.getY()) and a:
                Goal.append(Tree(click.getX(), click.getY(), win))
                print(len(Goal))
                run_button.activate()
            if run_button.clicked(click):
                break
        # CheckButtons()
    run_button.deactivate()
    encontrar_caminho(Obstacles, myrobot.getPos(), Goal[0], win, Path)
    Run2()


def Run2():
    print('-----------Run2-------------')
    print(len(Obstacles), 'Obstacles')
    print(len(Goal), 'Goals')
    print(len(Path), 'Points')
    # Lucas
    for point in Path:
        point.draw(win)


    for i in Path:
        while distance(i, myrobot.Pos) > 2:
            update(30)
            Clock(i.getX(), i.getY())
        Path.remove(i)

    print('-----------done-------------')
    clicktoreset = win.getMouse()
    Reset()


def Playmode3():
    GameMode = 3
    print('GameMode is now ', GameMode)
    init(win)
    play2_button.deactivate()
    play1_button.deactivate()
    play3_button.deactivate()
    reset_button.activate()
    win2 = GraphWin("Choose", WindowWidth/2, WindowHeight/2, autoflush=False)
    button_file = Button(win2, Point(WindowWidth/4, WindowHeight*(1/6)), 2*TabSize, 2*ButtonsHeight, "Read from a file", Run3file)
    button_random = Button(win2, Point(WindowWidth/4, WindowHeight*(2/6)), 2*TabSize, 2*ButtonsHeight, "Random map", Run3random)
    Buttons.append(button_file)
    Buttons.append(button_random)
    while win2 != 0:
        CheckButtons(win2)


def Filereader():
    Lines = []
    filename = fd.askopenfilename()
    f = open(filename, "r")
    for i in f:
        Lines.append(i)
    print(len(Lines))
    print(Lines[1])
    width, height = Lines[1].split(" ")
    for i in range(3, len(Lines)):
        Type, PosX, PosY = Lines[i].split(" ")
        Obstacles.append(Obstacle(float(PosX)*int(width), float(PosY)*int(height), int(Type), win))
    f.close()
    return int(width), int(height)


def Run3file():
    # win2.close()
    win2 = 0
    print('Run3file')
    width, height = Filereader()


    xratio = 100/width
    yratio = 100/height
    print(xratio)
    print(yratio)
    init2(width, height)


    clicktoclose = win.getMouse()
    if clicktoclose != None:
        win3.close()

def Run3random():
    #win2.close()
    win2 = 0
    print('Run3random')
    GameMode = 3
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
    pass

def init2(width,height): #transformar coisas redondas
    win3 = GraphWin("Mode 3", width, height, autoflush=False)
    
    rec1_2 = Rectangle(Point(95,95),Point(97,96))
    rec2_2 = Rectangle(Point(95,93),Point(97,94))
    rec3_2 = Rectangle(Point(91,91),Point(97,92))
    rec4_2 = Rectangle(Point(90,95),Point(91,98))
    rec5_2 = Rectangle(Point(80,80),Point(85,82))
    
    rec1_2.draw(win3)
    rec2_2.draw(win3)
    rec3_2.draw(win3)
    rec4_2.draw(win3)
    rec5_2.draw(win3)
    
    global bar1
    bar1 = Rectangle(Point(3,3),Point(4,4))
    bar1.setFill('green3')
    bar1.setWidth(0)
    bar1.draw(win3)
    
    global bar2
    bar2 = Rectangle(Point(5,5),Point(6,10))
    bar2.setFill('green3')
    bar2.setWidth(0)
    bar2.draw(win3)
    
    global bar3
    bar3 = Rectangle(Point(15,15),Point(16,20))
    bar3.setFill('green3')
    bar3.setWidth(0)
    bar3.draw(win3)
    
    global bar4
    bar4 = Rectangle(Point(2,20),Point(3,22))
    bar4.setFill('green3')
    bar4.setWidth(0)
    bar4.draw(win3)
    
    global Dock
    #Dock = Oval()
    Dock = Circle(Point(50,50), 5)
    Dock.setFill("light grey")
    Dock.draw(win3)
    bars.append(bar1)
    bars.append(bar2)
    bars.append(bar3)
    bars.append(bar4)
    
    RightCharger = Charger(3.25, 95, win3, mx,my)
    LeftCharger = Charger(96.75,95, win3, mx,my)
    Chargers.append(RightCharger)
    Chargers.append(LeftCharger)
    
    global batteryinfo
    batteryinfo = Text(Point(80,80), '100 %')
    batteryinfo.setFace('courier')
    batteryinfo.setSize(10)
    batteryinfo.draw(win3)
    
    global batterylabel
    batterylabel = Text(Point(18, 80), 'Battery')
    batterylabel.setFace('courier')
    batterylabel.setSize(10)
    batterylabel.draw(win3)
    
    global myrobot
    myrobot = Harve(50,0, 100, 1, win3, Chargers)
    
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
    
    RightCharger = Charger(WindowWidth - TabSize - 20, 20, win, 1, 1)
    LeftCharger = Charger(TabSize + 20, 20, win, 1, 1)
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
    
def CheckButtons(win):
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
    '''
    if type(win2) != "Point":
        win2.close()
    if type(win2) != "Point":
        win3.close()'''
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

def gotoPoint(obsX, obsY):
    print(" ")
    
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