# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:50:38 2022

@author: Afonso Araújo
"""

import math
import time

from graphics import *
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
            if distance(ii, s) < 30:
                a = 1
        if a == 1:
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

    X = (goal.getX() - Pinicial.getX())/Dinicial
    Y = (goal.getY() - Pinicial.getY())/Dinicial

    # REGIÃO 1
    if 0<=X<=1 and -0.5<=Y<=1:
        
        if Y==1:
            lst3 = [2*math.pi, 9*math.pi/4, 5*math.pi/2, 11*math.pi/4, 3*math.pi, 13*math.pi/4, 3*math.pi/2, 7*math.pi/4]
        else:
            lst3 = [2*math.pi, 9*math.pi/4, 5*math.pi/2, 11*math.pi/4, 3*math.pi, 5*math.pi/4, 3*math.pi/2, 7*math.pi/4]
            
    # REGIÃO 2
    if -(math.sqrt(3)/2)<=X<=(math.sqrt(3)/2) and -1<=Y<=-0.5:
        
        if X==(math.sqrt(3)/2):
            lst3 = [2*math.pi, 9*math.pi/4, 5*math.pi/2, 3*math.pi/4, math.pi, 5*math.pi/4, 3*math.pi/2, 7*math.pi/4]
        else:
            lst3 = [2*math.pi, 9*math.pi/4, math.pi/2, 3*math.pi/4, math.pi, 5*math.pi/4, 3*math.pi/2, 7*math.pi/4]

    
    # REGIÃO 3
    if -1<=X<=0 and -0.5<=Y<=1:
    
        if Y==1:
            lst3 = [2*math.pi, 9*math.pi/4, 5*math.pi/2, 11*math.pi/4, 3*math.pi, 13*math.pi/4, 7*math.pi/2, 7*math.pi/4]
        else:
            lst3 = [0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi, 5*math.pi/4, 3*math.pi/2, 7*math.pi/4]

    lst4 = []

    for i in range(len(lst1)):
        if lst1[i] < Dinicial:
            lst2.append(lst1[i])
            lst4.append(lst3[i])
   
    T = 0.001
    deltas = 0

    for ii in range(len(lst2)):
        deltas += ((Dinicial-lst2[ii]))*lst4[ii]
        T += Dinicial-lst2[ii]

    varang = (deltas/T)

    if varang < 0:
        varang += 2*math.pi

    if 2*math.pi < varang:
        varang -= 2 * math.pi

    # CASO O ROBO ESTEJA EM ROTA DE COLISÃO
    for i in Obstacles:
        if distance(Pinicial, i) < 36:
            print("CUIDADO")
            if (i.getX()-Pinicial.getX()) == 0:
                angulo0 = math.pi/2
            else:
                ang0 = (math.atan((i.getY()-Pinicial.getY())/(i.getX()-Pinicial.getX())))
            if ang0 < 0:
                ang0 += 2*math.pi
            ang1 = ang0 + (math.pi / 2)
            ang2 = ang0 - (math.pi / 2)

            if ang2 < 0:
                ang2 += 2*math.pi
            
            if abs(ang1-(deltas/T)) < abs(ang2-(deltas/T)):
                varang = ang1
            else:
                varang = ang2

    #-------------------------------------------------------------------------------------------------------

    if varang < 0:
        varang += 2*math.pi

    if 2*math.pi < varang:
        varang -= 2*math.pi

    return varang


def encontrar_caminho(Obstacles, Pinicial, goal, win, Path):
    if distance(Pinicial, goal)>20:
        ang = calcular_angulo(Obstacles, Pinicial, goal)
        Pinicial.move(20*math.cos(ang), 20*math.sin(ang))

        # time.sleep(0.1)
        pt = Point(Pinicial.getX(), Pinicial.getY())
        # Path.append(Point(Pinicial.getX(), Pinicial.getY()))
        Path.append(pt)

        encontrar_caminho(Obstacles, Pinicial, goal, win, Path)

    else:
        Pinicial.move((goal.getX()-Pinicial.getX()), (goal.getY()-Pinicial.getY()))
        Path.append(Point(Pinicial.getX(), Pinicial.getY()))
        # robot.Move((goal.getX()-Pinicial.getX()), (goal.getY()-Pinicial.getY()))
        print("feito")
