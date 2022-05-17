# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:15 2022

@author: Afonso Araújo
"""

from graphics import *
from Harve import *
from Tree import *
from Charger import *
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
        print("DEBUG1")
        CheckButtons()
        while True:
            click1 = win.checkMouse()
            if click1 != None:
                                           #opportunity to quit or reset
                print("DEBUG2")
                if IsInside(click1.getX(), click1.getY()):
                    print("DEBUG3")
                    Trees.append(Tree(click1.getX(), click1.getY(), win))
                    reset_button.activate()
                    run_button.activate()
                    break
        while True:
            click2 = win.checkMouse()   
            if click2:
                print("DEBUG4")
                run_button.activate()
                CheckButtons()
                break
                
    def init(win):
        Dock.draw(win)
        RightCharger = Charger(WindowWidth - TabSize - 20, 20, win)
        LeftCharger = Charger(TabSize + 20, 20, win)
        Chargers =[RightCharger, LeftCharger]
        
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
        myrobot.Undraw()
        myrobot.Delete()
        for Charger in Chargers:
            Charger.undraw()
            Charger.Delete()
        Chargers.clear()
        for Tree in Trees:
            Tree.Undraw()
            Tree.Delete()
        Trees.clear()
        
    def Quit():
        win.close()
        
    def Run():
        
        print('entrou no run')
        run_button.deactivate()
        while True:
            CheckButtons()
            Update(myrobot.Sonar(Trees).GetX(), myrobot.Sonar(Trees).GetY())        #the Get method is in caps because it was created by me in each object type class
            if myrobot.Stop(Trees) == 1:
                myrobot.Grab(myrobot.Sonar(Trees))
                break
            print('entrou no loop de update')
#starts the new movement to go to the charger
        while True:
            Update(myrobot.Sonar(Chargers).GetX(), myrobot.Sonar(Chargers).GetY())
            if myrobot.Stop(Chargers) == 1:
                print('done')
                run_button.deactivate()
                break
        CheckButtons()
        #finish 
                  
                

        
    def Update(obsX, obsY):       #Harve module after this
        
        print('update()')    
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