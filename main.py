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

def main():
    print("Hello Worldings")
    menu = GraphWin("MENU",800,600)
    play_button = Button(menu,Point(50,50), 20, 100,"Jogar")
        
    while (1):
        mouse = menu.getMouse()
        if (play_button.clicked(mouse)):
            
            menu.close()
    

    
    
    
    
    
    
   # init()
    #update():
       # time.sleep(1)

main()   


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