# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:15 2022

@author: Afonso Araújo
"""

from graphics import *
from Robot import *
from Tree import *
from Button import *

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
    LeftTab.setFill("light grey")
    RightTab.setFill("light grey")
    LeftTab.draw(win)
    RightTab.draw(win)
    play_button = Button(win, Point(TabSize/2, 50), (2/3)*TabSize, ButtonsHeight, "Play")
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Reset")
    
    while (1):
        mouse = win.getMouse()
        if play_button.clicked(mouse):
            NumObstacles = int(input("Quantos obstáculos? ")) #getText later
            click = win.getMouse() 
            for i in range(NumObstacles):    
                if TabSize < click.getX() < WindowWidth - TabSize: #condition to be inside game zone
                    obstacle = Circle(Point(click.getX(),click.getY()), ObstaclesSize)  #class for obstacles later
                    obstacle.setFill("green")
                    obstacle.draw(win)
                    
        win.close()

  
    
    
    
    
    
   # init()
    #update():
       # time.sleep(1)

def init():
    #Criar janela
    #Iniciar myroot na posiçao inicial
    myrobot = Robot(0, 0, 100)
    


def update():
    draw()
    return 0
    

    
def draw():
    #draw shit
    return 0
       

       
main()