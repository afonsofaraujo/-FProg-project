# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:32:25 2022

@author: Afonso Araújo
"""

'''fazer algoritmo com base no RRT que a função path planning devolva um alista de tuples com os nodes escolhidos
   o input são uma lista de Avoid_tuple ( não sei se vale a pena por em tuple )(é que eles assim têm uma ordem imutável
   que faz sentido porque são um conjunto de pequenos passos) e os Obstacles. O untitled5 é um RRT do IMT mas é uma beca marado'''

from graphics import *
from Harve import *
from Tree import *
from Charger import *
from Bush import *
from Stone import *
from Grass import *
from Button_modified import *
from math import *
import time



def distancia(a, b):
    d = sqrt((a.getX()-b.getX())**2 + (a.getY()-b.getY())**2)
    return(d)

class virtualnode:  #posI é o ponto inicial, angulo em radianos, alvo é um ponto, lista de obstáculos
    def __init__(self, posi, ang, alvo, obstaculo):
        
        self.posi = posi
        self.ang = ang
        self.alvo = alvo
        self.obstaculo = obstaculo
        
        
        a = 0
        p = 15
        
        while True:
            (self.posi).move(10*math.cos(ang), 10*math.sin(ang))
            p -= 1
            
            for obst in obstaculo:
                if distancia(obst, self.posi)<(5 + obst.radius()):
                    a = 1
            if a==1 or p==0:
                return posi
                break
            
        self.d = distancia(posi,alvo)
        
    def getd(self):
        return self.d
    
    def getang(self):
        return self.ang
          
    def atualizarposi(self, newposi):
        self.posi = Point(newposi.getX(),newyposi.getY())
        
        
        
        
        
        
def pathplanning(Avoid, alvo, pontodesaida): #lista de obstaculos
    #loop

        a = virtualnode(pontodesaida,0 , Avoid)
        b = virtualnode(pontodesaida,math.pi/4  , Avoid)
        c = virtualnode(pontodesaida,math.pi/2 , Avoid)
        d = virtualnode(pontodesaida,3*math.pi/4 , Avoid)
        e = virtualnode(pontodesaida,math.pi , Avoid)
        f = virtualnode(pontodesaida,-3*math.pi/4 , Avoid)
        g = virtualnode(pontodesaida,-math.pi/2 , Avoid)
        h = virtualnode(pontodesaida,-math.pi/4, Avoid)
        
        angulo = 0
        valnodes = []
        D = distancia(pontodesaida, alvo)
        lst=[a,b,c,d,e,f,g,h]
        
        T = 0
        for i in lst:
            deltad = D-i.getd()
            if deltad > 0:
                valnodes.append(i)
                T+=deltad
        for i in valnodes:
            angulo += i.ang()*(D-i.getd())/T
        return angulo
    
        lstfinal
        pontodesaida = 
    
    
    
    
    
    
        return lstfinal
    def 
  
    pass