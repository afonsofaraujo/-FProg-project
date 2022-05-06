# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:06:23 2022

@author: Afonso Araújo
"""
from graphics import *
class Harve:
    def __init__(self, PosX, PosY, Batery, win):
        self.PosX = PosX
        self.PosY = PosY
        self.Batery = Batery
        self.body = Circle(Point(PosX, PosY),10)
        self.Draw(win)
    
    def Move(self,newX, newY):
        self.PosX = newX
        self.PosY = newY
        
    def Draw(self, win):
            self.body.draw(win) 
            
    def Undraw(self):
            self.body.undraw() 
    
    def getX(self):
        return self.PosX
    
    def getY(self):
        return self.PosY
    