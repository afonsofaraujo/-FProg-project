# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:29:36 2022

@author: Afonso Araújo
"""

from graphics import *


class Obstacle:
    def __init__(self, posX, posY, Type, win):
        self.PosX = posX
        self.PosY = posY
        self.Type = Type
        if self.Type == 0:  # BUSH
            self.radius = 15
            self.body = Oval(Point(posX-15, posY-10), Point(posX+15, posY+10))
            self.body.setFill('darkgreen')
            self.body.draw(win)
        elif self.Type == 1:  # GRASS
            self.radius = 10
            self.body = Circle(Point(posX, posY), self.radius)
            self.body.setFill('lightgreen')
            self.body.draw(win)
        elif self.Type == 2:  # STONE
            self.radius = 15
            self.body = Circle(Point(posX, posY), self.radius)
            self.body.setFill('darkgray')
            self.body.draw(win)

    def undraw(self):
        self.body.undraw()

    def delete(self):
        del self

    def radius(self):
        return self.radius

    def getX(self):
        return self.PosX

    def getY(self):
        return self.PosY
