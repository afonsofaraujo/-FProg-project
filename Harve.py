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
        '''robot moves its position dx and dy given in the input'''
        self.body.move(dx, dy)
        self.PosX = self.PosX + dx              #update position
        self.PosY = self.PosY + dy
        self.Battery = self.Battery - 0.1

    def Seek(self, x, y):
        '''makes the robot move in a straight line from its position to x and y given in the input'''
        deltax = abs(self.PosX - x)
        deltay = abs(self.PosY - y)
        angle = atan(deltay/deltax)
        theta = radians(angle)
        self.xvel = cos(angle) * self.Velocity
        self.yvel = sin(angle) * self.Velocity
        if (x < self.PosX):
            self.xvel = -self.xvel
        if (y < self.PosY):
            self.yvel = -self.yvel
            
        self.Move(self.xvel, self.yvel)
        
    def Sonar(self, Objects):         
        '''returns the closest object'''
        min_distance = 9999
        min_object = Point(0,0)
        for i in Objects:
            distance = sqrt((self.PosX - i.getX())**2 + (self.PosY - i.getY())**2)
            if distance < min_distance:
                min_distance = distance
                min_object = i
        return min_object

    def Stop(self, Objects):
        '''checks the need to stop and returns 1 if so'''
        min_distance = 9999
        min_object = Point(0,0)
        for i in Objects:
            distance = sqrt((self.PosX - i.getX())**2 + (self.PosY - i.getY())**2)
            if distance < min_distance:
                min_distance = distance
                min_object = i
        if min_distance < 20:
            return 1
        else:
            return 0

    def Grab(self, Object):
        '''robot pauses to collect the input object and deletes it '''
        time.sleep(1)
        Object.undraw()
        del Object
            
    def undraw(self):
        '''undraw robot'''
        self.body.undraw()
        
    def delete(self):
        '''deletes robot'''
        del self
            
    def getX(self):
        '''returns PosX of the robot'''
        return self.PosX
    
    def getY(self):
        '''returns PosY of the robot'''
        return self.PosY
    
    def getBattery(self):
        '''returns battery of the robot'''
        return round(self.Battery)