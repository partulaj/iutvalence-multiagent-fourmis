from threading import Thread
from time import sleep

MAX_PHEROMONE = 50
MIN_PHEROMONE = 1

class Arc(Thread):
    '''
        Constructeur de la classe
    '''
    def __init__(self, noeudDepart, noeudArrive):
        Thread.__init__(self)
        self.noeudDepart = noeudDepart
        self.noeudArrive = noeudArrive
        self.metrique = 0
        self.pheromone = 1

    def run(self):
        while True:
            self.evaporationPheromone()
            sleep(10)

    '''
        toString de la classe
    '''
    def __str__(self):
        return "Arc {}<->{} longeur : {} pheromone : {}".format(self.noeudDepart, self.noeudArrive, self.metrique, self.pheromone)

    '''
        equals de la classe
    '''
    def sameArc(self, other):
        if other.noeudDepart == self.noeudDepart and other.noeudArrive == self.noeudArrive:
            return True
        else:
            return False

    '''
        getter pour noeudDebut
    '''
    def getDebut(self):
        return self.noeudDepart

    '''
        getter pour noeudArrive
    '''
    def getArrive(self):
        return self.noeudArrive

    '''
        setter pour metrique
    '''
    def setMetrique(self,metrique):
        self.metrique = metrique

    def getMetrique(self):
        return self.metrique

    def getPheromone(self):
        return self.pheromone
    '''
        méthode pour ajouter des phéromones sur l'arc
    '''
    def addPheromones(self):
        if (self.pheromone<MAX_PHEROMONE):
            self.pheromone+=0.5

    def evaporationPheromone(self):
        if (self.pheromone>MIN_PHEROMONE):
            self.pheromone= self.pheromone*0.95
            print(str(self)+" Evaporation de 5%")
