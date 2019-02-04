import matplotlib.pyplot as plt
import numpy as np

def graph(nodes, matrix, names):
    distance = [matrix[nodes[0]][nodes[x + 1]] for x in range(len(nodes)-1)]
    distance.insert(0, 0)
    plt.plot(distance,nodes, zorder=1, label="Links", color="r")
    plt.scatter(distance[0], nodes[0], marker="o", color="green", s=20 ** 2, zorder=2, label="Start")
    plt.scatter(distance[1:-1], nodes[1:-1], marker="o", color="blue", s=20 ** 2, zorder=2, label="Nodes")
    plt.scatter(distance[-1], nodes[-1], marker="o", color="red", s=20 ** 2, zorder=2, label="End")
    for x in range(len(distance)):
        plt.annotate(names[nodes[x]], (distance[x], nodes[x]))
    plt.legend()
    plt.xlabel("Distance in relation to Start")
    plt.ylabel("Node Number")
    plt.show()
