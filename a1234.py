# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:50:38 2022

@author: Afonso Araújo
"""

from graphics import *
import math
import time
from Harve import *

def distance(a, b):
    return math.sqrt((a.getX()-b.getX())**2+(a.getY()-b.getY())**2)
    
def sensor(ang, D, center, Obstacles):
    
    # angulo diz para qual direção o sensor anda
    # a D diz quantos passos o sensor da na direção dita pelo angulo
    # o centro diz da onde o sensor sai
    # lista de obstáculos
    
    s = Point(center.getX(), center.getY())
    a = 0
    
    for i in range(int(D/5)):
        for ii in Obstacles:
            if distance(ii, s)<30:
                a = 1
        if a==1:
            break
        s.move(5*math.cos(ang), 5*math.sin(ang)) 
    return s


def calcular_angulo(Obstacles, Pinicial, goal):

    Dinicial = (distance(goal, Pinicial))
    
    S1 = distance((sensor(0, Dinicial, Pinicial, Obstacles)), goal)
    S2 = distance((sensor(math.pi/4, Dinicial, Pinicial, Obstacles)), goal)
    S3 = distance((sensor(math.pi/2, Dinicial, Pinicial, Obstacles)), goal)
    S4 = distance((sensor(3*math.pi/4, Dinicial, Pinicial, Obstacles)), goal)
    S5 = distance((sensor(math.pi, Dinicial, Pinicial, Obstacles)), goal)
    S6 = distance((sensor(-3*math.pi/4, Dinicial, Pinicial, Obstacles)), goal)
    S7 = distance((sensor(-math.pi/2, Dinicial, Pinicial, Obstacles)), goal)
    S8 = distance((sensor(-math.pi/4, Dinicial, Pinicial, Obstacles)), goal)
    
    lst1 = [S1, S2, S3, S4, S5, S6, S7, S8]
    lst2 = []
    
    lst3 = [0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi, 5*math.pi/4, 3*math.pi/2, 7*math.pi/4]
    lst4 = []
    
    for i in range (len(lst1)):
        if (lst1[i])<Dinicial:
            lst2.append(lst1[i])
            lst4.append(lst3[i])
            
    T = 0
    deltas = 0
    
    for ii in range (len(lst2)):
        deltas += ((lst2[ii])-Dinicial)*lst4[ii]
        T += lst2[ii]-Dinicial
        
    varang = (deltas/T)
    
    # CASO O ROBO ESTEJA EM ROTA DE COLISÃO
    for i in Obstacles:
        if distance(Pinicial, i) < 36:
            print("CUIDADO")
            ang0 = math.atan((i.getY()-Pinicial.getY())/(i.getX()-Pinicial.getX()))
            if ang0<0:
                ang0 += 2*math.pi
            ang1 = ang0 + (math.pi/2)
            ang2 = ang0 - (math.pi/2)
            
            if ang2<0:
                ang2 += 2*math.pi
            
            if abs(ang1-(deltas/T))<abs(ang2-(deltas/T)):
                varang = ang1
            else:
                varang = ang2
            
    #-------------------------------------------------------------------------------------------------------
                    
    return varang

def encontrar_caminho(Obstacles, Pinicial, goal, robot, win, Path):
    if distance(Pinicial, goal)>10:
        ang = calcular_angulo(Obstacles, Pinicial, goal)
        Pinicial.move(10*math.cos(ang), 10*math.sin(ang))
        robot.Move(10*math.cos(ang), 10*math.sin(ang))
             
        print(distance(Pinicial, goal))
        pt = Point(Pinicial.getX(), Pinicial.getY())
        pt.draw(win)
        Path.append(pt)
                
        encontrar_caminho(Obstacles, Pinicial, goal, robot, win, Path)
        
    else:
        Pinicial.move((goal.getX()-Pinicial.getX()), (goal.getY()-Pinicial.getY()))
        robot.Move((goal.getX()-Pinicial.getX()), (goal.getY()-Pinicial.getY()))
        print("feito")
        
