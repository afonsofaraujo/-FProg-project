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
from Button_modified import *
from math import *
import time

Trees = [] #Lista de arvores, lista de objetos da classe TREE
Buttons = []
Chargers = []

#Variables
WindowWidth = 800
WindowHeight = 600
TabSize = 100
ButtonsVerticalSpacement = 50
ButtonsHeight = 30
ObstaclesSize = 5 #radius
  #append Buttons on main
win = GraphWin("GAME", WindowWidth, WindowHeight, autoflush=False)
LeftTab = Rectangle(Point(0,WindowHeight), Point(TabSize,0))
RightTab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)


def main():
    
    def handleClick(pt, win):
        pass
    
    def Playmode1():
        init(win)
        play_button.deactivate()
        CheckButtons()
        while True:
            click1 = win.checkMouse()
            if click1 != None:
                if IsInside(click1.getX(), click1.getY()):
                    Trees.append(Tree(click1.getX(), click1.getY(), win))
                    reset_button.activate()
                    run_button.activate()
                    CheckButtons()
                    break
       
    def init(win):
        Dock.draw(win)
        RightCharger = Charger(WindowWidth - TabSize - 20, 20, win)
        LeftCharger = Charger(TabSize + 20, 20, win)
        Chargers.append(RightCharger)
        Chargers.append(LeftCharger)
        global batteryinfo
        batteryinfo = Text(Point(WindowWidth - TabSize/2, 100), '100 %')
        batteryinfo.draw(win)
        batterylabel = Text(Point(WindowWidth - TabSize/2, 100), 'Battery')
        global myrobot
        myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win)
        
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
        play_button.activate()
        run_button.deactivate()
        Dock.undraw()
        myrobot.undraw()
        myrobot.delete()
        batteryinfo.undraw()
        for Charger in Chargers:
            Charger.undraw()
            Charger.delete()
        Chargers.clear()
        for Tree in Trees:
            Tree.undraw()
            Tree.delete()
        Trees.clear()
        
    def Quit():
        win.close()
        
    def Run():
        
        run_button.deactivate()
        while True:
            CheckButtons()
            Update(myrobot.Sonar(Trees).getX(), myrobot.Sonar(Trees).getY())
            if myrobot.Stop(Trees) == 1:
                myrobot.Grab(myrobot.Sonar(Trees))
                break

#starts the new movement to go to the charger
        while True:
            CheckButtons()
            Update(myrobot.Sonar(Chargers).getX(), myrobot.Sonar(Chargers).getY())
            if myrobot.getX() - myrobot.Sonar(Chargers).getX() < 1 and myrobot.getY() - myrobot.Sonar(Chargers).getY() < 1:
                print('done')
                run_button.deactivate()
                break
        CheckButtons()
        #finish 
                  
                

        
    def Update(obsX, obsY):       #Harve module after this
        
        print('x', obsX,'y', obsY)
        batteryinfo.setText(str(round(myrobot.getBattery())) +' %')
        time.sleep(0.01)
        myrobot.Seek(obsX, obsY)

        
    print("Hello Worldings")
    
    LeftTab.setFill("light grey")
    RightTab.setFill("light grey")
    Dock.setFill("light grey")
    LeftTab.draw(win)
    RightTab.draw(win)
    play_button = Button(win, Point(TabSize/2, 50), (2/3)*TabSize, ButtonsHeight, "Play", Playmode1)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Reset", Reset)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Run", Run)
    reset_button.deactivate()
    run_button.deactivate()
    Buttons = [quit_button, reset_button, play_button, run_button]
    
    

    while True:
        CheckButtons()
    
main()