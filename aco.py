import random

class Graph:
    def __init__(self):
        with open("distance", "r") as rf:
            self.adjacent = sorted([x[:-1].split(" ") for x in rf.readlines()])
            self.nodes = sorted(list(set(' '.join([' '.join([y for y in x if not y.isdigit()]) for x in self.adjacent]).split(" "))))
            self.matrix = [[]]
            for i in range(len(self.nodes)):
                for t in range(len(self.nodes)):
                    for j in self.adjacent:
                        if (self.nodes[i] == j[0] and self.nodes[t] == j[1]) or (self.nodes[i] == j[1] and self.nodes[t] == j[0]):
                            self.matrix[i].append(int(j[-1]))
                            break
                    else:
                        self.matrix[i].append(0)
                self.matrix.append([])
            self.matrix = self.matrix[:-1]

class AntColony:
    def __init__(self, matrix, antcount, cycles):
        #Arbitrary constants
        self.alpha = 0.7
        self.beta = 0.7
        self.rho = 0.7
        self.Q = 1
        self.ants = []
        self.antcount = antcount    
        self.cycles = cycles
        self.matrix = matrix
        self.pheromones = [[0 for x in y] for y in self.matrix]
        self.heuristics = [[1/x if x else 0 for x in y] for y in self.matrix]
        for x in range(antcount):
            self.addAnt()
    def addAnt(self):
        ant = Ant(self)
        self.ants.append(ant)
    def updatePheromone(self):
        for i in range(len(self.pheromones)):
            for j in range(len(self.pheromones)):
                self.pheromones[i][j] *= self.rho
                for ant in self.ants:
                    self.pheromones[i][j] += ant.deltaPheromones[i][j]
    def solve(self):
        cost = float('inf')
        solution = []
        for cycle in range(self.cycles):
            for ant in self.ants:
                for x in self.matrix[:-1]:
                    ant.move()
                #print(ant.totalcost, cost, ant.tabulist)
                if 0 != ant.totalcost < cost and len(ant.tabulist) == len(self.matrix):
                    cost = ant.totalcost
                    solution = ant.tabulist
                ant.updatePheromoneDelta()
                self.updatePheromone()
        return cost, solution
 

class Ant:
    def __init__(self, colony):
        self.colony = colony
        self.totalcost = 0
        self.pos = random.randint(0, len(self.colony.matrix) - 1)
        self.allowed = [x for x in range(len(self.colony.matrix)) if x != self.pos]
        self.deltaPheromones = [[0 for x in y] for y in self.colony.matrix]
        self.tabulist = [self.pos]
    def updatePheromoneDelta(self):
        for i in range(len(self.colony.matrix)):
            for j in range(len(self.colony.matrix)):
                try:
                    self.deltaPheromones[i][j] = self.colony.Q / self.colony.matrix[i][j]
                except ZeroDivisionError:
                    self.deltaPheromones[i][j] = 0
    def move(self):
        p = 0
        h = 0
        choice = self.pos
        for link in self.allowed:
            try:
                p = (self.colony.pheromones[self.pos][link] ** self.colony.alpha) * (self.colony.heuristics[self.pos][link] ** self.colony.beta)
                h = sum([(self.colony.pheromones[self.pos][x] ** self.colony.alpha) * (self.colony.heuristics[self.pos][x] ** self.colony.beta) for x in self.allowed])
                p /= h
            except ZeroDivisionError:
                p = 0
            rand = random.random() - p
            if rand <= 0:
                choice = link
                break
        try:
            self.allowed.remove(choice)
            self.tabulist.append(choice)
        except ValueError:
            pass
        self.totalcost += self.colony.matrix[self.pos][choice]
        self.pos = choice
