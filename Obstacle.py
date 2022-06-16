# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:29:36 2022

@author: Afonso Araújo
"""

from graphics import *

class Obstacle:
    def __init__(self, PosX, PosY, Type, win):
        self.PosX = PosX
        self.PosY = PosY
        self.Type = Type
        if self.Type == 0: #BUSH
            self.radius = 15
            self.body = Oval(Point(self.PosX - 15, self.PosY-10), Point(self.PosX + 15, self.PosY+ 10))
            self.body.setFill('darkgreen')
            self.body.draw(win)
        elif self.Type == 1: #GRASS
            self.radius = 10
            self.body = Circle(Point(self.PosX, self.PosY), self.radius)
            self.body.setFill('lightgreen')
            self.body.draw(win)
        elif self.Type == 2: #STONE
            self.radius = 15
            self.body = Circle(Point(self.PosX, self.PosY), self.radius)
            self.body.setFill('darkgray')
            self.body.draw(win)
        
    def undraw(self):
        self.body.undraw() 
               
    def delete(self):
        del self
    
    def radius(self):
        return self.radius