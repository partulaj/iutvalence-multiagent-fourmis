from threading import Thread
from random import random
from time import sleep


class Fourmis(Thread):
    '''
        Constructeur de la classe
    '''
    def __init__(self, graphe, type):
        Thread.__init__(self)
        self.noeudActuel = "F"
        self.noeudDepart = "F"
        self.noeudDestination = "N"
        self.chemin = "F"
        self.graphe = graphe
        self.type = type
        self.roadsTraveled = []
        self.roadsForbidden = []
        self.noeudsParcourus = []
        self.noeudsParcourus.append(self.noeudActuel)

    '''
        to string de la classe
    '''
    def __str__(self):
        return "Fourmis {} {}".format(self.type,Thread.getName(self))

    '''
        Méthode pour avancer
    '''
    def forward(self):
        road = self.selectRoad()
        if road != None:
            if road.getDebut()==self.noeudActuel:
                nextStep = road.getArrive()
            else:
                nextStep = road.getDebut()
            if nextStep not in self.noeudsParcourus:
                self.noeudActuel = nextStep
                self.noeudsParcourus.append(nextStep)
                self.chemin = self.chemin+" "+nextStep
                #print(str(self)+" "+str(road))
                self.roadsTraveled.append(road)
                sleep(road.getMetrique()*0.1)
            else:
                # Debug self.chemin = self.chemin+" "+nextStep
                road = self.backward()
                self.roadsForbidden.append(road)

    def backward(self):
        road = self.roadsTraveled.pop()
        if road != None:
            if road.getDebut()==self.noeudActuel:
                self.nextStep = road.getArrive()
            else:
                self.nextStep = road.getDebut()
            self.noeudActuel = self.nextStep
            self.chemin = self.chemin+" "+self.nextStep
            road.addPheromones()
            #print(str(self)+" "+str(road))
            sleep(road.getMetrique()*0.1)
            return road


    def selectRoad(self):
        roads = self.graphe.getRoads(self.noeudActuel, self.roadsTraveled+self.roadsForbidden)
        numerateur = []
        denominateur = 0
        for i in range(0, len(roads)):
            if i<1:
                numerateur.append((1/(roads[i].getMetrique()**self.type.getAlpha()))*(roads[i].getPheromone()**self.type.getBeta()))
                denominateur += numerateur[i]
            else :
                numerateur.append((1/(roads[i].getMetrique()**self.type.getAlpha()))*(roads[i].getPheromone()**self.type.getBeta()))
                numerateur[i] += numerateur[i-1]
                denominateur += numerateur[i]
        if len(roads)>0:
            rand = random()
            for i in range(0, len(roads)):
                if rand < (numerateur[i]/denominateur):
                    return roads[i]
        return None

    def run(self):
        while self.noeudActuel != self.noeudDestination:
            self.forward()
        #print(str(self)+" "+self.chemin)
        while self.noeudActuel != self.noeudDepart:
            self.backward()
        print(str(self)+" "+self.chemin)