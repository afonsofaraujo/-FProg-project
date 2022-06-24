# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:28:13 2022

@author: Afonso Araújo
"""

from graphics import *


class Tree:
    def __init__(self, posX, posY, win):
        self.PosX = posX
        self.PosY = posY
        self.trunk = Rectangle(Point(posX-2, posY-5), Point(posX+2, posY+5))
        self.trunk.setFill('brown')
        self.leaves = Circle(Point(posX, posY-8), 5)
        self.leaves.setFill('green')
        self.trunk.draw(win)
        self.leaves.draw(win)

    def undraw(self):
        self.trunk.undraw()
        self.leaves.undraw()

    def delete(self):
        del self

    def getX(self):
        return self.PosX

    def getY(self):
        return self.PosY
