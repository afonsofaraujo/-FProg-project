# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:28:13 2022

@author: Afonso Araújo
"""
from graphics import *
class Tree:
    def __init__(self, PosX, PosY, win):
        self.PosX = PosX
        self.PosY = PosY
        self.trunk = Rectangle(Point(PosX-2, PosY-5),Point(PosX+2, PosY+5))
        self.trunk.setFill('brown')
        self.leaves = Circle(Point(PosX, PosY-8),5)
        self.leaves.setFill('green')
        self.trunk.draw(win)
        self.leaves.draw(win)
        
    def Undraw(self):
        self.trunk.undraw() 
        self.leaves.undraw()
               
    def Delete(self):
        del self
        
    def GetX(self):
        return self.PosX
    
    def GetY(self):
        return self.PosY