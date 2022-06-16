# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 20:29:46 2022

@author: Afonso Araújo
"""

from graphics import *
from math import *
import time


def distance(a, b):
    '''returns the distance between points a and b'''
    return abs(sqrt((a.getX()-b.getX())**2 + (a.getY()-b.getY())**2))
    
class virtualnode:  #posI é o ponto inicial, angulo em radianos, alvo é um ponto, lista de obstáculos
    '''creates a virtual Point around the robot based on a position and angle''' 
    def __init__(self, posi, ang, goal):
        
        self.radius = 10 #vai variar para ver o que acontece
        self.nodepos = Point(posi.getX + radius*cos(ang),posi.getY + radius*sin(ang)) 
        self.ang = ang
        self.goal = goal
        self.d = distance(nodepos,alvo)
        
    def getX(self):
        return nodePos.getX()
        
    def getY(self):
        return nodePos.getY()
        
    def getd(self):
        return self.d

  
def pathplanning(Obstacles, goal, startPos): #lista de obstaculos
    '''returns a list of several points that make the path for the robot from its startPos to goal'''
    #loop
    #currentPos é onde está a posição do robot a ser avaliada
    #startPos é onde ele começa que é invariável
    #no final do loop a currentPos tem de ser atualizada para passarmos a avaliar a proxima posição
    #a condição do while serve para parar o loop se estiver proximo do goal
    localpath = []
    currentPos = startPos
    while distance(currentPos, goal)<20:
        
        a = virtualnode(currentPos,0, goal)
        b = virtualnode(currentPos,math.pi/4, goal)
        c = virtualnode(currentPos,math.pi/2, goal)
        d = virtualnode(currentPos,3*math.pi/4, goal)
        e = virtualnode(currentPos,math.pi, goal)
        f = virtualnode(currentPos,-3*math.pi/4, goal)
        g = virtualnode(currentPos,-math.pi/2, goal) 
        h = virtualnode(currentPos,-math.pi/4, goal)
        
        Nodes = [a,b,c,d,e,f,g,h]
        
        #select nodes
        for i in Nodes:
            if i.getd() > distance(currentPos, goal):
                Nodes.remove(i)
        for i in Nodes:     
            for ii in Obstacles:
                if distance(Point(ii.getX(),ii.getY()),Point(i.getX(),i.getY())) < 2:    #raio da sensibilidade de cada node
                    Nodes.remove(i)
        selectednode = Nodes.index(1)  #default
        mind = 9999
        for i in Nodes:
            if i.getd() < mind:
                selectednode = Nodes.index(i)
                mind = i.getd
            elif i.getd() == mind:
                selectednode = Nodes.index(1)     #em caso de empate
        
        currentPos = Point(selectednode.getX(),selectednode.getY())
        localpath.append(currentPos)
    return localpath
