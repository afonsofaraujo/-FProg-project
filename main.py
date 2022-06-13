# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:15 2022

@author: Afonso Araújo
"""

from graphics import *
from Harve import *
from Tree import *
from Charger import *
from Bush import *
from Stone import *
from Grass import *
from PathplanningRRT import *
from Button_modified import *
from math import *
import time

#Global lists
Obstacles = []
Goal = []
Objects = []      
Buttons = []    
Chargers = []

#Variables
#GameMode = 0     #default 0
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
Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)
Dock.setFill("light grey")

def main():
    global GameMode
    GameMode = 0
    def Playmode1():
        GameMode = 1
        print(GameMode)
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
        print(GameMode)
        init(win)
        play2_button.deactivate()
        reset_button.activate()            #not working for mode 2
        CheckButtons()
        
        #plot obstacles
        a = Bush(200, 350, win)
        b = Bush(620, 140, win)
        c = Grass(560, 200, win)
        d = Stone(400, 300, win)
        e = Stone(300, 450, win)
        #later this can be generated with random or chaotic function
        
        Obstacles = [a,b,c,d,e]
        print('1')
        
        while True:
            CheckButtons()
            click = win.checkMouse()
            if click!= None:
                a = True
                print('2')
                for i in Obstacles:
                    if distance(Point(i.getX(),i.getY()), Point(click.getX(),click.getY())) < 10:
                        a = False
                if IsInside(click.getX(), click.getY()) and a:
                    tree = Tree(click.getX(), click.getY(), win)
                    Goal.append(Point(click.getX(),click.getY()))
                    run_button.activate()
                if run_button.clicked(click):
                    break

    def init(win):
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
        batterylabel = Text(Point(WindowWidth - TabSize/2, 80), 'Battery')
        batterylabel.setFace('courier')
        batterylabel.setSize(10)
        batterylabel.draw(win)
        global myrobot
        myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win)
        
    def CheckButtons():
        #print('GameMode is now ',GameMode)
        if GameMode == 1:
            run_button.changehandler(Run1)
            run_button.gethandler()
        elif GameMode == 2:
            run_button.changehandler(Run2)
            run_button.gethandler()
        else:
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
        run_button.deactivate()
        print('3')
        lstPath = []
        
        for i in Goal:
            Path = pathplanning(Obstacles, i, myrobot.getPos())
            for ii in Path:
                c = Circle(ii,5)
                c.setFill('red')
                c.draw(win)
            lstPath.append(Path)   
                                 
        for i in lstPath:                        
            for ii in i:
                while myrobot.getX()!= ii.getX() and myrobot.getY() != ii.getY():             #enquanto ainda não estiver lá
                    Clock(ii.getX(),ii.getY())                                                #anda de node em node

        
    def Clock(obsX, obsY):       #Harve module after this
        batteryinfo.setText(str(myrobot.getBattery()) +' %')
        time.sleep(0.01)
        myrobot.Seek(obsX, obsY)

    LeftTab.draw(win)
    RightTab.draw(win)
    play2_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*5), (2/3)*TabSize, ButtonsHeight, "Mode 2", Playmode2)
    play1_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Mode 1", Playmode1)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement), (2/3)*TabSize, ButtonsHeight, "Reset", Reset)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Run", Run1)
    reset_button.deactivate()
    run_button.deactivate()
    Buttons = [quit_button, reset_button, play1_button, play2_button, run_button]
    
    while True:
        CheckButtons()
        
if __name__ == "__main__":  
    main()