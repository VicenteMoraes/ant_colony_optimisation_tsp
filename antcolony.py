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

class Colony:
    def __init__(self, generations, antcount, matrix):
        self.alpha = 10
        self.beta = 10
        self.rho = 0.5
        self.Q = 1
        self.generations = generations
        self.matrix = matrix
        self.ants = [Ant(self) for ant in range(antcount)]
        self.pheromones = [[0 for x in y] for y in self.matrix]
        self.heuristic = [[1/x if x else 0 for x in y] for y in self.matrix]
    def updatePheromone(self):
        for i in range(len(self.pheromones)):
            for j in range(len(self.pheromones)):
                self.pheromones[i][j] *= self.rho
                for ant in self.ants:
                    self.pheromones[i][j] += ant.deltaPheromone[i][j]
    def solve(self):
        cost = float("inf")
        solution = []
        for generation in range(self.generations):
            for ant in self.ants:
                for x in self.matrix[:-1]:
                    ant.move()
                if 0 != ant.cost < cost and len(ant.tour) >= len(self.matrix):
                    cost = ant.cost
                    solution = ant.tour
                ant.updatePheromoneDelta()
                self.updatePheromone()
        return cost, solution

class Ant:
    def __init__(self, colony):
        self.colony = colony
        self.pos = random.randint(0, len(self.colony.matrix) - 1)
        self.allowed = [x for x in range(len(self.colony.matrix)) if x != self.pos]
        self.tour = [self.pos]
        self.cost = 0
        self.deltaPheromone = [[0 for x in y] for y in self.colony.matrix]
    def updatePheromoneDelta(self):
        for i in range(len(self.colony.matrix)):
            for j in range(len(self.colony.matrix)):
                try:
                    self.deltaPheromone[i][j] = self.colony.Q / self.colony.matrix[i][j]
                except ZeroDivisionError:
                    self.deltaPheromone[i][j] = 0
    def move(self):
        choice = self.pos
        p = 0
        for link in self.allowed:
            try:
                p = (self.colony.pheromones[self.pos][link] ** self.colony.alpha) * (self.colony.heuristic[self.pos][link] ** self.colony.beta)
                h = sum([(self.colony.pheromones[self.pos][x] ** self.colony.alpha) * (self.colony.heuristic[self.pos][x] ** self.colony.beta) for x in self.allowed])
                p /= h
            except ZeroDivisionError:
                p = 0
            if random.random() <= p:
                choice = link
                break
        try:
            self.allowed.remove(choice)
            self.tour.append(choice)
        except ValueError:
            pass
        self.cost = sum([self.colony.matrix[self.tour[x]][self.tour[x+1]] for x in range(len(self.tour) - 1)])
        self.pos = choice
