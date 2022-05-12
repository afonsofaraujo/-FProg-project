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

        self.body.move(dx, dy)
        self.PosX = self.PosX + dx
        self.PosY = self.PosY + dy


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
        min_distance = 1000
        for Obstacle in Obstacles:
            distance = sqrt((self.PosX - Obstacle.getX())**2 + (self.PosY - Obstacle.getY())**2)
            if distance < min_distance:
                min_distance = distance
                min_obstacle = Obstacle
        return min_obstacle

    def Stop(self, Obstacles):                   #checks the need to stop and returns 1
                                                #the input is a list
        min_distance = 1000
        for Obstacle in Obstacles:
            distance = sqrt((self.PosX - Obstacle.getX())**2 + (self.PosY - Obstacle.getY())**2)
            if distance < min_distance:
                min_distance = distance
                min_obstacle = Obstacle
        if min_distance < 20:                   #it stoped to grab   
            Grab(Obstacles)
            return 1

    def Grab(self, Obstacle):
        time.sleep(2)
        Obstacle.Undraw()
        del Obstacle
        
            
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