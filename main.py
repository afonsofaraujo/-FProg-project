# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:15 2022

@author: Afonso Araújo
"""

from graphics import *
from Harve import *
from Tree import *
from Button_modified import *
from math import *
import time

Trees = [] #Lista de arvores, lista de objetos da classe TREE

Buttons = []

#Variables
WindowWidth = 800
WindowHeight = 600
TabSize = 100
ButtonsVerticalSpacement = 100
ButtonsHeight = 20
ObstaclesSize = 5 #radius
  #append Buttons on main

def main():
    
    def Playmode1():
        init(win)
        play_button.deactivate()
        print("DEBUG1")
        click1 = win.checkMouse()
        while click1:
            CheckButtons(win)         #opportunity to quit or reset
            print("DEBUG2")
            if click1 != None:
                if IsInside(click1.getX(), click1.getY()):
                    print("DEBUG3")
                    Trees.append(Tree(click1.getX(), click1.getY(), win))
                    reset_button.activate()
                    break
            print("DEBUG4")
        while True:
            click2 = win.checkMouse()   
            if click2:
                run_button.activate()
                CheckButtons(win)
                
    def init(win):
        Dock.draw(win)
        RightCharger.draw(win)
        LeftCharger.draw(win)
        global myrobot
        myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win)
        
    def CheckButtons(win):
        while True:
            mouse = win.checkMouse()
            if mouse:
                for Button in Buttons:
                    if Button.clicked(mouse):
                        Button.onClick()
                        return True
                break
    
    def IsInside(x,y):
        return (TabSize < x < (WindowWidth - TabSize))
    
    def ClearBoard():
        reset_button.deactivate()
        play_button.activate()
        Dock.undraw()
        for tree in Trees:    
            tree.Delete()
        myrobot.Delete()
    
    def Quit():
        win.close()
        
    def Run():
        CheckButtons(win)
        run_button.deactivate()
        while True:
            CheckButtons(win)
            Update(myrobot.Sonar(Trees).getX(), myrobot.Sonar(Trees).getY())
            myrobot.Sonar(Trees)
            if myrobot.Sonar(Trees) == 1:
                break
        while True:
            Update(myrobot.Gocharge().getX(), myrobot.Gocharge().getY())
            if sqrt((myrobot.getX() - myrobot.Gocharge().getX())**2 + (myrobot.getY() - myrobot.Gocharge().getY())**2):
                print('done')
                break
                  
                

        
    def Update(obsX, obsY):       #Harve module after this
        time.sleep(0.01)
        myrobot.Seek(obsX, obsY)

        
    print("Hello Worldings")
    global win
    win = GraphWin("GAME", WindowWidth, WindowHeight, autoflush=False)
    LeftTab = Rectangle(Point(0,WindowHeight), Point(TabSize,0))
    RightTab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
    Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)
    RightCharger = Circle(Point(WindowWidth - TabSize - 20, 20), 30)
    LeftCharger = Circle(Point(TabSize + 20, 20), 30)
    RightCharger.setFill('yellow')
    LeftCharger.setFill('yellow')
    LeftTab.setFill("light grey")
    RightTab.setFill("light grey")
    Dock.setFill("light grey")
    LeftTab.draw(win)
    RightTab.draw(win)
    play_button = Button(win, Point(TabSize/2, 50), (2/3)*TabSize, ButtonsHeight, "Play", Playmode1)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Reset", ClearBoard)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Run", Run)
    reset_button.deactivate()
    Buttons = [quit_button, reset_button, play_button, run_button]
    

    while True:
        CheckButtons(win)
    
main()