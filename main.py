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

def main():
    print("Hello Worldings")
    win = GraphWin("GAME", WindowWidth, WindowHeight)
    LeftTab = Rectangle(Point(0,WindowHeight), Point(TabSize,0))
    RightTab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
    Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)
    LeftTab.setFill("light grey")
    RightTab.setFill("light grey")
    Dock.setFill("light grey")
    LeftTab.draw(win)
    RightTab.draw(win)
    play_button = Button(win, Point(TabSize/2, 50), (2/3)*TabSize, ButtonsHeight, "Play")
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Reset")
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Quit")
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Run")
    reset_button.deactivate()
    
    def init(win):
        Dock.draw(win)
        global myrobot
        myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win)
        
    def event(reset_button, quit_button, play_button, win):
        click = win.checkMouse()
        if click:
            if play_button.clicked(click):
                init(win)
                play_button.deactivate()
                playmode1(win)
            elif reset_button.clicked(click):
                ClearBoard()
            elif quit_button.clicked(click):
                quit_button.deactivate()
                win.close()
        else:
            return 0
        
    def IsInside(x,y):
        return (TabSize < x < (WindowWidth - TabSize))
    
    def ClearBoard():
        reset_button.deactivate()
        play_button.activate()
        Dock.undraw()
        obs1.Delete()
        myrobot.Delete()
        
    def Update():
        time.sleep(0.01)
        myrobot.Seek(obs1.getX(), obs1.getY())
        print(abs(myrobot.getX()-obs1.getX()),"     ",abs(myrobot.getY()-obs1.getY()))
        
    def playmode1(win):
        while True:
            event(reset_button, quit_button, play_button, win)                         #opportunity to quit or reset
            click1 = win.checkMouse()
            if click1:
                event(reset_button, quit_button, play_button, win)
                if IsInside(click1.getX(), click1.getY()):
                    global obs1
                    obs1 = Tree(click1.getX(),click1.getY(),win)
                    print(obs1.getX(),obs1.getY())
                    reset_button.activate()
                    break
        while True:
            click2 = win.checkMouse()   
            if click2:
                event(reset_button, quit_button, play_button, win)
                if run_button.clicked(click2):
                    event(reset_button, quit_button, play_button, win)
                    run_button.deactivate()
                    while (abs(myrobot.getX()-obs1.getX()) > 20 or abs(myrobot.getY()-obs1.getY()) > 20):
                            Update()
                            event(reset_button, quit_button, play_button, win)
                    print("done")
                    break
    while True:
            event(reset_button, quit_button, play_button, win)
    
main()