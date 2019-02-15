import antcolony
import plot

graph = antcolony.Graph()
colony = antcolony.Colony(100, 30, graph.matrix)
cost, solution = colony.solve()
print("Cost: " + str(cost) + ". Solution: ", end="", flush=True)
print(solution)
plot.graph(solution, graph.matrix, graph.nodes)
