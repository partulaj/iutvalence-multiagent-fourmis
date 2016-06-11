from Arc import Arc


class Graphe():
    def __init__(self, listNoeuds):
        self.listNoeuds = listNoeuds
        self.initArcs()

    def initArcs(self):
        self.arcs = []
        for i in range(0, len(self.listNoeuds)):
            ligne = []
            for j in range(0, len(self.listNoeuds)):
                if j < (i + 1):
                    ligne.append(None)
                else:
                    arc = Arc(self.listNoeuds[i], self.listNoeuds[j])
                    ligne.append(arc)
            self.arcs.append(ligne)
        self.runArcs()

    def runArcs(self):
        for i in range(0, len(self.listNoeuds)):
            for j in range(i+1, len(self.listNoeuds)):
                self.arcs[i][j].start()

    def getArc(self, noeudDebut, noeudArrive):
        for i in range(0, len(self.listNoeuds)):
            for j in range(i + 1, len(self.listNoeuds)):
                if self.arcs[i][j].sameArc(Arc(noeudDebut, noeudArrive)):
                    return self.arcs[i][j]
                elif self.arcs[i][j].sameArc(Arc(noeudArrive, noeudDebut)):
                    return self.arcs[i][j]
        return None

    def getRoads(self, noeudActuel, roadsTraveled):
        l = []
        for i in range(0, len(self.listNoeuds)):
            for j in range(i + 1, len(self.listNoeuds)):
                if self.arcs[i][j].getDebut() == noeudActuel and self.arcs[i][j].getMetrique()>0 and self.arcs[i][j] not in roadsTraveled:
                    l.append(self.arcs[i][j])
                elif self.arcs[i][j].getArrive() == noeudActuel and self.arcs[i][j].getMetrique()>0 and self.arcs[i][j] not in roadsTraveled:
                    l.append(self.arcs[i][j])
        return l
