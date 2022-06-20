# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:31:54 2022

@author: Afonso Araújo
"""
from graphics import *
import math
import Harve

def distancia(variavelA, variavelB):
    euyciuwenc = (math.sqrt((variavelA.getX()-variavelB.getX())**2+(variavelA.getY()-variavelB.getY())**2))
    return (euyciuwenc)
    
def sensor(angulo, D, centro, listaobstaculos):
    
    # angulo diz para qual direção o sensor anda
    # a D diz quantos passos o sensor da na direção dita pelo angulo
    # o centro diz da onde o sensor sai
    # lista de obstáculos
    
    s = Point(centro.getX(), centro.getY())
    a = 0
    
    for i2 in range(int(D/5)):
        for obs in listaobstaculos:
            if distancia(obs, s)<20:
                a = 1
            if a==1:
                break
            
        s.move(5*math.cos(angulo), 5*math.sin(angulo))
        
    return s


def calcular_angulo(obst, Pinicial, objetivo):

    Dinicial = (distancia(objetivo, Pinicial))
    
    S1 = distancia((sensor(0, Dinicial, Pinicial, obst)), objetivo)
    S2 = distancia((sensor(math.pi/4, Dinicial, Pinicial, obst)), objetivo)
    S3 = distancia((sensor(math.pi/2, Dinicial, Pinicial, obst)), objetivo)
    S4 = distancia((sensor(3*math.pi/4, Dinicial, Pinicial, obst)), objetivo)
    S5 = distancia((sensor(math.pi, Dinicial, Pinicial, obst)), objetivo)
    S6 = distancia((sensor(-3*math.pi/4, Dinicial, Pinicial, obst)), objetivo)
    S7 = distancia((sensor(-math.pi/2, Dinicial, Pinicial, obst)), objetivo)
    S8 = distancia((sensor(-math.pi/4, Dinicial, Pinicial, obst)), objetivo)
    
    lista1 = [S1, S2, S3, S4, S5, S6, S7, S8]
    lista2 = []
    
    lista3 = [0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi, 5*math.pi/4, 3*math.pi/2, 7*math.pi/4]
    lista4 = []
    
    for i in range (len(lista1)):
        if (lista1[i])<Dinicial:
            lista2.append(lista1[i])
            lista4.append(lista3[i])
            
    T = 0
    deltas = 0
    
    for s2 in range (len(lista2)):
        deltas += ((lista2[s2])-Dinicial)*lista4[s2]
        T += lista2[s2]-Dinicial
    
    varang = (deltas/T)
    
    # CASO O ROBO ESTEJA EM ROTA DE COLISÃO
    for o in obst:
        if distancia(Pinicial, o) < 46:
            print("CUIDADO")
            angulo0 = (math.atan((o.getY()-Pinicial.getY())/(o.getX()-Pinicial.getX())))
            if angulo0<0:
                angulo0 += 2*math.pi
            angulo1 = angulo0 + (math.pi/2)
            angulo2 = angulo0 - (math.pi/2)
            
            if angulo2<0:
                angulo2 += 2*math.pi
                
            if angulo1>2*math.pi:
                angulo1 -= 2*math.pi
            
            if abs(angulo1-(deltas/T))<abs(angulo2-(deltas/T)):
                varang = angulo1
            else:
                varang = angulo2
            
    
    #-------------------------------------------------------------------------------------------------------
                    
    
    return (varang)

def encontrar_caminho(obst, Pinicial, objetivo,robot):
    if 10<distancia(Pinicial, objetivo):
        ang = calcular_angulo(obst, Pinicial, objetivo)
        Pinicial.move(10*math.cos(ang), 10*math.sin(ang))
        robot.Clock
        
        print(distancia(Pinicial, objetivo))
        
        encontrar_caminho(obst, Pinicial, objetivo)
        
    else:
        Pinicial.move((objetivo.getX()-Pinicial.getX()), (objetivo.getY()-Pinicial.getY()))
    
        print("feito")
