from Fourmis import Fourmis
from Graphe import Graphe
from Type import Type

if __name__ == '__main__':
    l = ["A", "B", "C", "D", "E", "F", "N"]
    graphe = Graphe(l)
    #print(graphe.arcs)
    graphe.getArc("F","D").setMetrique(3)
    graphe.getArc("F","E").setMetrique(1)
    graphe.getArc("D","C").setMetrique(4)
    graphe.getArc("E","C").setMetrique(1)
    graphe.getArc("C","B").setMetrique(1)
    graphe.getArc("C","A").setMetrique(5)
    graphe.getArc("B","N").setMetrique(1)
    graphe.getArc("A","N").setMetrique(5)

    fourmis=[]

    for i in range(0,10):
        fourmis.append(Fourmis(graphe, Type('Explorer')))

    for i in range(0,10):
        fourmis[i].start()