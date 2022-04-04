# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:42:43 2022

@author: Afonso Araújo


"""
from graphics import*
def main():
    win = GraphWin("MENU",500,500)
    
    a = Rectangle(Point(200,200), Point(300,300))
    txtjogo = Text(a.getCenter(),"Jogar")
    
    txtjogo.draw(win)
    a.draw(win)
    
    win.getMouse()
    win.close()
    
main()
