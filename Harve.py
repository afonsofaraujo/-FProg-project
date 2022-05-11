# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:06:23 2022

@author: Afonso Araújo
"""
from graphics import *
from math import *

class Harve:
    def __init__(self, PosX, PosY, Batery, velocity, win):
        self.PosX = PosX
        self.PosY = PosY
        self.Batery = Batery
        self.Velocity = velocity
        self.Window = win
        self.body = Circle(Point(PosX, PosY),10)
        self.body.setFill("black")
        self.Draw()
        self.xvel = 0
        self.yvel = 0
        
    def Move(self, dx, dy):
        self.Undraw()
        self.body.move(dx, dy)
        self.PosX = self.PosX + dx
        self.PosY = self.PosY + dy
        self.Draw()

    def Seek(self, obsX, obsY):
        deltax = abs(self.PosX - obsX)
        deltay = abs(self.PosY - obsY)
        angle = atan(deltay/deltax)
        theta = radians(angle)
        self.xvel = cos(angle) * self.Velocity
        self.yvel = sin(angle) * self.Velocity
        if (obsX < self.PosX):
            self.xvel = -self.xvel
        if (obsY < self.PosY):
            self.yvel = -self.yvel
        
        self.Move(self.xvel, self.yvel)
        
    def Sonar(self, Obstacles):                 #returns the closest object
        max_distance = 0
        for Obstacle in Obstacles:
            distance = sqrt((self.PosX - Obstacle.getX())**2 + (self.PosY - Obstacle.getY())**2)
            if distance > max_distance:
                max_distance = distance
                max_obstacle = Obstacle
        return max_obstacle
        if max_distance < 20:                   #it stoped to grab   
            Grab(Obstacle)

    def Grab(self, Obstacle):
        time.sleep(2)
        Obstacle.Undraw()
        del Obstacle
        
    def GoCharge(self):                         #decides which charger is the closest
        
        if (abs(self.PosX - TabSize)) < (abs(self.PosX - (WindowWidth - TabSize))):
            rightcharger = Point(WindowWidth - TabSize - 20, 20)
            return rightcharger
        else:
            leftcharger = Point(TabSize + 20, 20)
            return leftcharger
            
    def Draw(self):
        self.body.draw(self.Window) 
            
    def Undraw(self):
        self.body.undraw()
        
    def Delete(self):
        del self
            
    def getX(self):
        return self.PosX
    
    def getY(self):
        return self.PosY