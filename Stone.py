# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:26:59 2022

@author: Afonso Araújo
"""

from graphics import *
class Stone:
    def __init__(self, PosX, PosY, win):
        self.PosX = PosX
        self.PosY = PosY
        self.radius = 15
        self.body = Circle(Point(self.PosX, self.PosY), self.radius)
        self.body.setFill('darkgray')
        self.body.draw(win)
        
    def undraw(self):
        self.body.undraw() 
               
    def delete(self):
        del self
        
    def getX(self):
        return self.PosX
    
    def getY(self):
        return self.PosY
    
    def radius(self):
        return self.radius