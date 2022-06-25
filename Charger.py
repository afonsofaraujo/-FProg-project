###########################################################################################
#   2º Semestre do 1º ano do curso de Engenharia Mecânica - Instituto Superior Técnico    #
#   Unidade Curricular do Projeto - Fundamentos da Programação                            #
#   Nome do Projeto: Robô da Fruta                                                        #
#   Autores: Afonso Araújo (102685) e Lucas Feijó (103968)                                #
#   Grupo: G45                                                                            #
#   Data: 25.06.2022                                                                      #
#   Módulo: Charger                                                                       #
###########################################################################################

from graphics import *

class Charger:
    def __init__(self, PosX, PosY, win):
        self.PosX = PosX
        self.PosY = PosY
        self.body = Rectangle(Point(PosX-20, PosY+20), Point(PosX+20, PosY-20))
        self.body.setFill('yellow')
        self.body.draw(win)

    def undraw(self):
        self.body.undraw()

    def delete(self):
        del self

    def getX(self):
        return self.PosX

    def getY(self):
        return self.PosY
