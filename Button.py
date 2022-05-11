# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:06:07 2022

@author: Afonso Araújo
"""
from graphics import *

#ARRAY de BUttons
#for i in button, if clicked

class Button():
    """ Creates a Button object with methods activate(), deactivate(),
        and clicked(pt) """

    def __init__(self, win, center, width, height, label, handler):
        """ Create button object which consists of a Rectangle centered at 'center'
            with a Text object with text 'label' """
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmin, self.ymin = x-w, y-h
        self.xmax, self.ymax = x+w, y+h

        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(pt1, pt2)

        self.label = Text(center,label)
        self.label.setTextColor('lightgrey')

        self.rect.draw(win)
        self.label.draw(win)
        self.activate()
        
        self.handler = handler

    def activate(self):
        """ sets to active / available to be clicked """
        self.label.setTextColor('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """ sets to inactive / unavailable to be clicked """
        self.label.setTextColor('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        
    def Clicked(self, mouse):
        """ if button is active this will determine if there was a click
            (pt) within the button """       
        return (self.active and self.xmin <= mouse.getX() <= self.xmax and self.ymin <= mouse.getY() <= self.ymax)

    def getLabel(self):
        """ returns the label text """
        return self.label.getText()
    
    
    def OnClick(self):
        self.handler()