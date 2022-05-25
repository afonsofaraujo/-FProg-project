# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:06:23 2022

@author: Afonso Araújo
"""
from graphics import *
from math import *
from Tree import *
from Bush import *
from Stone import *
from Grass import *
from Charger import *

class Harve:
    def __init__(self, PosX, PosY, Battery, velocity, win):
        self.PosX = PosX
        self.PosY = PosY
        self.Battery = Battery
        self.Velocity = velocity
        self.Window = win
        self.body = Circle(Point(PosX, PosY),10)
        self.body.setFill("black")
        self.body.draw(win)
        self.xvel = 0
        self.yvel = 0
        
    def Move(self, dx, dy):

        self.body.move(dx, dy)
        self.PosX = self.PosX + dx              #updated position
        self.PosY = self.PosY + dy
        self.Battery = self.Battery - 0.1
        print(self.PosX,self.PosY)

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
        
    def Sonar(self, Obstacles):           #returns the closest object
                                                        
        min_distance = 9999
        min_obstacle = Point(0,0)
        
        for i in Obstacles:
            distance = sqrt((self.PosX - i.getX())**2 + (self.PosY - i.getY())**2)
            if distance < min_distance:
                min_distance = distance
                min_obstacle = i
        return min_obstacle

    def Stop(self, Obstacles):                   #checks the need to stop and returns 1
                                                #the input is a list
        min_distance = 9999
        min_obstacle = Point(0,0)
        for i in Obstacles:
            distance = sqrt((self.PosX - i.getX())**2 + (self.PosY - i.getY())**2)
            
            if distance < min_distance:
                min_distance = distance
                min_obstacle = i
        if min_distance < 20:                   #it stoped to grab   
            return 1
        else:
            return 0

    def Grab(self, Obstacle):                     #input is an object
        
        time.sleep(1)
        Obstacle.undraw()
        del Obstacle
            
    def undraw(self):
        self.body.undraw()
        
    def delete(self):
        del self
            
    def getX(self):
        return self.PosX
    
    def getY(self):
        return self.PosY
    
    def getBattery(self):
        return self.Battery