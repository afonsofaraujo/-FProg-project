###########################################################################################
#   2º Semestre do 1º ano do curso de Engenharia Mecânica - Instituto Superior Técnico    #
#   Unidade Curricular do Projeto - Fundamentos da Programação                            #
#   Nome do Projeto: Robô da Fruta                                                        #
#   Autores: Afonso Araújo (102685) e Lucas Feijó (103968)                                #
#   Grupo: G45                                                                            #
#   Data: 25.06.2022                                                                      #
#   Módulo: Button                                                                        #
###########################################################################################

from graphics import *

class Button():
    """ Creates a Button object"""

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
        self.rect.setFill("dim gray")

        self.label = Text(center,label)
        self.label.setTextColor('lightgrey')
        self.label.setFace('courier')

        self.rect.draw(win)
        self.label.draw(win)
        self.activate()
        
        self.handler = handler

    def activate(self):
        """ sets to active / available to be clicked """
        #self.label.setTextColor('black')
        self.label.setTextColor('black')
        self.rect.setWidth(4)
        self.active = True

    def deactivate(self):
        """ sets to inactive / unavailable to be clicked """
        self.label.setTextColor('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        
    def clicked(self, mouse):
        """ if button is active this will determine if there was a click
            (pt) within the button """       
        return (self.active and 
                self.xmin <= mouse.getX() <= self.xmax and
                self.ymin <= mouse.getY() <= self.ymax)

    def getLabel(self):
        """ returns the label text """
        return self.label.getText()
    
    def changehandler(self, newhandler):
        '''change the handler function of a button'''
        self.handler = newhandler
        
    def gethandler(self):
        '''prints the current handler of the button'''
        return self.handler
    
    def state(self):
        '''return True if the button is active'''
        return self.active
         
    def onClick(self):
        self.handler()