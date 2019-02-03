import aco
import plot

graph = aco.Graph()
colony = aco.AntColony(graph.matrix, 10, 10)
solution = colony.solve()
print(solution)
plot.graph(solution[1], graph.matrix)
