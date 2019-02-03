import aco

graph = aco.Graph()
colony = aco.AntColony(graph.matrix, 10, 10)
print(colony.solve())
