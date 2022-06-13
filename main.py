# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:15 2022

@author: Afonso Araújo
"""

from graphics import *
from Harve import *
from Tree import *
from Charger import *
from Bush import *
from Stone import *
from Grass import *
from PathplanningRRT import *
from Button_modified import *
from math import *
import time

#Global lists
Objects = []      
Buttons = []    
Chargers = []
Avoid = []
Avoid_tuple = [] 

#Variables


GameMode = 0     #default 0
WindowWidth = 800
WindowHeight = 600
TabSize = 100
ButtonsVerticalSpacement = 50
ButtonsHeight = 30
ObstaclesSize = 5               #radius

win = GraphWin("GAME", WindowWidth, WindowHeight, autoflush=False)
LeftTab = Rectangle(Point(0,WindowHeight), Point(TabSize,0))
LeftTab.setFill("light grey")
RightTab = Rectangle(Point(WindowWidth - TabSize, WindowHeight), Point(WindowWidth, 0))
RightTab.setFill("light grey")
Dock = Circle(Point(WindowWidth/2,WindowHeight), 50)
Dock.setFill("light grey")



def main():

    def Playmode1():
        init(win)
        play1_button.deactivate()
        GameMode = 1 
        CheckButtons()
        while True:
            click1 = win.checkMouse()
            if click1 != None:
                if IsInside(click1.getX(), click1.getY()):
                    Objects.append(Tree(click1.getX(), click1.getY(), win))
                    reset_button.activate()
                    run_button.activate()
                    CheckButtons()
                    break
    
    def Playmode2():
        init(win)
        play2_button.deactivate()
        GameMode = 2 
        CheckButtons()
        
        #plot objects
        a = Bush(200, 350, win)
        b = Bush(620, 140, win)
        c = Grass(560, 200, win)
        d = Stone(400, 300, win)
        e = Stone(300, 450, win)
        # later this can be generated with random or chaotic function
        
        Avoid = [a,b,c,d,e]
        
        #for i in Group:
           # Avoid.append(i.getX)
           # Avoid.append(i.getY)
            
        #Avoid_tuple = [x for x in zip(*[iter(Avoid)]*2)]
        #print(Avoid_tuple)
        
        
        run_button.activate()
        
        while run_button.state():
            click = win.checkMouse()
            CheckButtons()
            if click != None:
                if IsInside(click.getX(),click.getY()):
                    Objects.append(Tree(click.getX(), click.getY(), win))
                    if len(Objects)>2:
                        reset_button.activate()
                        run_button.activate()
                        CheckButtons()
                        break    #forçar a sair ao terceiro objeto colocado       
        
        
      
    
    def init(win):
        Dock.draw(win)
        RightCharger = Charger(WindowWidth - TabSize - 20, 20, win)
        LeftCharger = Charger(TabSize + 20, 20, win)
        Chargers.append(RightCharger)
        Chargers.append(LeftCharger)
        global batteryinfo
        batteryinfo = Text(Point(WindowWidth - TabSize/2, 100), '100 %')
        batteryinfo.setFace('courier')
        batteryinfo.setSize(10)
        batteryinfo.draw(win)
        batterylabel = Text(Point(WindowWidth - TabSize/2, 80), 'Battery')
        batterylabel.setFace('courier')
        batterylabel.setSize(10)
        batterylabel.draw(win)
        global myrobot
        myrobot = Harve(WindowWidth/2, WindowHeight, 100, 1, win)
        
    def CheckButtons():
        mouse = win.checkMouse()
        if mouse != None:
            for Button in Buttons:
                if Button.clicked(mouse):
                    Button.onClick()
                    return True
        if GameMode == 1:
            run_button.changehandler(Run1())
        elif GameMode == 2:
            run_button.changehandler(Run2())
        else:
            pass
            
    
    def IsInside(x,y):
        return (TabSize < x < (WindowWidth - TabSize))
    
    def Reset():
        reset_button.deactivate()
        play1_button.activate()
        run_button.deactivate()
        Dock.undraw()
        myrobot.undraw()
        myrobot.delete()
        batteryinfo.undraw()
        for Charger in Chargers:
            Charger.undraw()
            Charger.delete()
        Chargers.clear()
        for Object in Objects:
            Object.undraw()
            Object.delete()
        Objects.clear()
        
    def Quit():
        win.close()
        
    def Run1():
        run_button.deactivate()
        while True:
            CheckButtons()
            Clock(myrobot.Sonar(Objects).getX(), myrobot.Sonar(Objects).getY())
            if myrobot.Stop(Objects) == 1:
                myrobot.Grab(myrobot.Sonar(Objects))
                break

        #starts the new movement to go to the charger
        while True:
            CheckButtons()
            Clock(myrobot.Sonar(Chargers).getX(), myrobot.Sonar(Chargers).getY())
            if myrobot.getX() - myrobot.Sonar(Chargers).getX() < 1 and myrobot.getY() - myrobot.Sonar(Chargers).getY() < 1:
                print('-----------done-------------')
                run_button.deactivate()
                break
        CheckButtons()
        #finish 
    def Run2():
        #aqui é que vai dar buraco
        
        #Objects tem coisas
        #Avoid_tuple tem coisas
        
        
        Nodes = []
        
        pathplaning()   #returns a list of nodes (tuples) to use on Seek()
                                #ele volta à base logo a posição inicial é a posição final
        for i in Nodes:
            while myrobot.getX()!= i.tuple[0] and myrobot.getY() != i.tuple[1]:             #enquanto ainda não estiver lá
                Clock(i.tuple[0],i.tuple[1])                                                #anda de node em node
















        pass
        
    def Clock(obsX, obsY):       #Harve module after this
        batteryinfo.setText(str(myrobot.getBattery()) +' %')
        time.sleep(0.01)
        myrobot.Seek(obsX, obsY)

    LeftTab.draw(win)
    RightTab.draw(win)
    play2_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*5), (2/3)*TabSize, ButtonsHeight, "Mode 2", Playmode2)
    play1_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*4), (2/3)*TabSize, ButtonsHeight, "Mode 1", Playmode1)
    reset_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement), (2/3)*TabSize, ButtonsHeight, "Reset", Reset)
    quit_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*2), (2/3)*TabSize, ButtonsHeight, "Quit", Quit)
    run_button = Button(win, Point(TabSize/2, ButtonsVerticalSpacement*3), (2/3)*TabSize, ButtonsHeight, "Run", Run1)
    reset_button.deactivate()
    run_button.deactivate()
    Buttons = [quit_button, reset_button, play1_button, play2_button, run_button]
    
    while True:
        CheckButtons()
        
if __name__ == "__main__":  
    main()