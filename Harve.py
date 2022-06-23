# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:06:23 2022

@author: Afonso Araújo
"""

from graphics import *

from math import *

class Harve:
    def __init__(self, PosX, PosY, Battery, velocity, win, Chargers):
        self.Chargers = Chargers
        self.PosX = PosX
        self.PosY = PosY
        self.Pos = Point(self.PosX,self.PosY)
        self.Battery = Battery
        self.Batterylevel = 4
        self.Velocity = velocity
        self.Window = win
        self.body = Circle(Point(PosX, PosY),10)
        self.body.setFill('black')
        self.body.draw(win)
        self.light = Circle(Point(PosX, PosY-5),3)
        self.light.setFill('green')
        self.light.draw(win)
        self.xvel = 0
        self.yvel = 0
    
    def batterylight(self):
        '''updates the color of the light according to battery percentage'''
        if 75<=self.Battery<=100:
            self.light.setFill('green3')
            self.Batterylevel = 4
        elif 50<=self.Battery<75:
            self.light.setFill('yellow')
            self.Batterylevel = 3
        elif 25<=self.Battery<50:
            self.light.setFill('dark orange')
            self.Batterylevel = 2
        elif self.Battery<25:
            self.light.setFill('red')
            self.Batterylevel = 1
   
    def Move(self, dx, dy):
        '''robot moves its position dx and dy given in the input'''
        self.body.move(dx, dy)
        self.light.move(dx,dy)
        self.PosX = self.PosX + dx              #update position
        self.PosY = self.PosY + dy
        self.Pos = Point(self.PosX,self.PosY)
        self.Battery = self.Battery - 0.1
        self.batterylight()
        
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
        
    def Goto(self, x, y):
        self.Velocity = 5
        while sqrt(abs((x-self.PosX**2)+(y-self.PosY**2))) > 2:
            self.Window.getMouse()
            self.Seek(x , y)
            time.sleep(0.5)        
        
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
        
    def Charge(self):
        '''charges the battery if the robot is inside charging zone'''
        for i in self.Chargers:
            if i.PosX -20 < self.PosX < i.PosX+20 and i.PosY -20 < self.PosY < i.PosY+20:
                if self.Battery <100:
                    self.Battery += 10
                if self. Battery >= 100:
                    self.battery = 100
                    break
                
    def undraw(self):
        '''undraw robot'''
        self.body.undraw()
        self.light.undraw()
        
    def draw(self, win):
        self.body.draw(win)
        self.light.undraw()
        
    def delete(self):
        '''deletes robot'''
        del self
            
    def getX(self):
        '''returns PosX of the robot'''
        return self.PosX
    
    def getY(self):
        '''returns PosY of the robot'''
        return self.PosY
    
    def getPos(self):
        '''returns Point where the robot is'''
        return Point(self.PosX,self.PosY)
    
    def getBattery(self):
        '''returns battery of the robot'''
        if self.Battery > 100:
            self.Battery = 100
        return round(self.Battery)