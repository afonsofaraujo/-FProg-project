# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:15 2022

@author: Afonso Araújo
"""

from graphics import *
from Robot import *
from Tree import *
from Button import *
import time

trees = [] #Lista de arvores, lista de objetos da classe TREE

#Variables
WindowWidth = 800
WindowHeight = 600
TabSize = 100
ButtonsVerticalSpacement = 100
ButtonsHeight = 20
ObstaclesSize = 5 #radius
  #append Buttons on main

def main():
    
    def Playmode1(win):
        while True:
            CheckButtons(win)                      #opportunity to quit or reset
            click1 = win.checkMouse()
            if click1:
                CheckButtons(win)
                if IsInside(click1.getX(), click1.getY()):
                    global obs1
                    obs1 = Tree(click1.getX(),click1.getY(),win)
                    Obstacles.append(obs1)
                    print(obs1.getX(),obs1.getY())
                    reset_button.activate()
                    break
        while True:
            click2 = win.checkMouse()   
            if click2:
                CheckButtons(win)
                if run_button.clicked(click2):
                    CheckButtons(win)
                    run_button.deactivate()
                    while (abs(myrobot.getX()-obs1.getX()) > 20 or abs(myrobot.getY()-obs1.getY()) > 20):
                            Update()
                            if reset_button.clicked(click):   #cancel the animation
                                ClearBoard()
                                break
                            
                    print("done")
                    break
                
    def init(win):
        Dock.draw(win)
        global myrobot
        myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win)
        
    def CheckButtons(win):
        mouse = win.checkMouse()
        for Button in Buttons:
            if Button.Clicked(mouse):
                Button.onClick()
                return true
    #If CheckButtons(win) não corre o update
            
            
    def IsInside(x,y):
        return (TabSize < x < (WindowWidth - TabSize))
    
    def ClearBoard():
        reset_button.deactivate()
        play_button.activate()
        Dock.undraw()
        obs1.Delete()
        myrobot.Delete()
    
    def Quit():
        win.close()
        
        
    def Update():
        time.sleep(0.01)
        myrobot.Seek(obs1.getX(), obs1.getY())
        print(abs(myrobot.getX()-obs1.getX()),"     ",abs(myrobot.getY()-obs1.getY()))
        

    print("Hello Worldings")
    win = GraphWin("GAME", WindowWidth, WindowHeight, autoflush=False)
    LeftTab = Rectangle(Point(0,WindowHeight), Point(TabSize,0))
    RightTab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
    Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)
    LeftTab.setFill("light grey")
    RightTab.setFill("light grey")
    Dock.setFill("light grey")
    LeftTab.draw(win)
    RightTab.draw(win)
    play_button = Button(win, Point(TabSize/2, 50), (2/3)*TabSize, ButtonsHeight, "Play", Playmode1)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Reset", ClearBoard)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Run", )
    reset_button.deactivate()
    global Buttons
    Buttons = [quit_button, reset_button, play_button]
    global Obstacles
    Obstacles = []
    

    while True:
            CheckButtons(win)
    
main()