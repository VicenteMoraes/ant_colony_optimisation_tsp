import aco
import plot

graph = aco.Graph()
colony = aco.AntColony(graph.matrix, 100, 30)
cost, solution = colony.solve()
print("Cost: " + str(cost) + ". Solution: ", end="", flush=True)
print(solution)
plot.graph(solution, graph.matrix, graph.nodes)
