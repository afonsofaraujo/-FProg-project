###########################################################################################
#   2º Semestre do 1º ano do curso de Engenharia Mecânica - Instituto Superior Técnico    #
#   Unidade Curricular do Projeto - Fundamentos da Programação                            #
#   Nome do Projeto: Robô da Fruta                                                        #
#   Autores: Afonso Araújo (102685) e Lucas Feijó (103968)                                #
#   Grupo: G45                                                                            #
#   Data: 25.06.2022                                                                      #
#   Módulo: Harve                                                                         #
###########################################################################################

from math import sin, cos, atan, sqrt
from graphics import *

class Harve:
    '''robot class'''
    def __init__(self, posX, posY, battery, velocity, win, Chargers):
        self.Chargers = Chargers
        self.PosX = posX
        self.PosY = posY
        self.Pos = Point(posX, posY)
        self.Battery = battery
        self.Batterylevel = 4
        self.Velocity = velocity
        self.Window = win
        self.body = Circle(Point(posX, posY), 10)
        self.body.setFill('black')
        self.body.draw(win)
        self.light = Circle(Point(posX, posY-5), 3)
        self.light.setFill('green')
        self.light.draw(win)
        self.xvel = 0
        self.yvel = 0

    def batterylight(self):
        '''updates the color of the light according to battery percentage'''
        if 75 <= self.Battery <= 100:
            self.light.setFill('green3')
            self.Batterylevel = 4
        elif 50 <= self.Battery < 75:
            self.light.setFill('yellow')
            self.Batterylevel = 3
        elif 25 <= self.Battery < 50:
            self.light.setFill('dark orange')
            self.Batterylevel = 2
        elif self.Battery < 25:
            self.light.setFill('red')
            self.Batterylevel = 1

    def Move(self, dx, dy):
        '''robot moves its position dx and dy given in the input'''
        self.body.move(dx, dy)
        self.light.move(dx, dy)
        self.PosX = self.PosX + dx
        self.PosY = self.PosY + dy
        self.Pos = Point(self.PosX, self.PosY)
        self.Battery = self.Battery - 0.05
        self.batterylight()

    def Seek(self, x, y):
        '''makes the robot move in a straight line from its position to x and y given in the input'''
        deltax = abs(self.PosX - x)
        deltay = abs(self.PosY - y)

        angle = atan(deltay/deltax)
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
        min_object = Point(0, 0)
        for i in Objects:
            distance = sqrt((self.PosX - i.getX())**2 + (self.PosY - i.getY())**2)
            if distance < min_distance:
                min_distance = distance
                min_object = i
        return min_object

    def Stop(self, Goal):
        '''checks the need to stop and returns 1 if so'''
        min_distance = 9999
        min_goal = Point(0, 0)
        for i in Goal:
            distance = sqrt((self.PosX - i.getX())**2 + (self.PosY - i.getY())**2)
            if distance < min_distance:
                min_distance = distance
                min_goal = i
        if min_distance < 20:
            return 1
        else:
            return 0

    def Grab(self, Object):
        '''robot pauses to collect the input object and deletes it '''
        time.sleep(1)
        Object.undraw()
        Object.delete()

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
        self.light.draw(win)

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
        return Point(self.PosX, self.PosY)

    def getBattery(self):
        '''returns battery of the robot'''
        if self.Battery > 100:
            self.Battery = 100
        return round(self.Battery)
