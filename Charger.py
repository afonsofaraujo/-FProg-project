# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:13:20 2022

@author: Afonso Araújo
"""

from graphics import *
class  Charger:
    def __init__(self, PosX, PosY, win):
        self.PosX = PosX
        self.PosY = PosY
        self.body = Rectangle(Point(PosX-20, PosY+20),Point(PosX+20, PosY-20))
        self.body.setFill('yellow')
        self.body.draw(win)
        
    def Undraw(self):
        self.body.undraw()
               
    def Delete(self):
        del self
        
    def GetX(self):
        return self.PosX
    
    def GetY(self):
        return self.PosY