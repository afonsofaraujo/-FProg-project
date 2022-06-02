# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:21:54 2022

@author: Afonso Araújo
"""
from graphics import *
class Bush:
    def __init__(self, PosX, PosY, win):
        self.PosX = PosX
        self.PosY = PosY
        self.body = Oval(Point(self.PosX - 15, self.PosY-10), Point(self.PosX + 15, self.PosY+ 10))
        self.body.setFill('darkgreen')
        self.body.draw(win)
        
    def undraw(self):
        self.body.undraw() 
               
    def delete(self):
        del self
        
    def getX(self):
        return self.PosX
    
    def getY(self):
        return self.PosY
