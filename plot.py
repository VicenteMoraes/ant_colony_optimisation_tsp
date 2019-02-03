import matplotlib.pyplot as plt
import numpy as np

def graph(nodes, matrix):
    distance = [matrix[x][x + 1] for x in range(len(nodes)-1)]
    distance.append(0)
    color = ["w" if nodes.index(x) == 0 else "b" if nodes.index(x) == len(nodes)-1 else "r" for x in nodes]
    plt.plot(distance, nodes, marker="o", markersize=30, markerfacecolor="r")
    plt.xlabel("Distance")
    plt.ylabel("Node Number")
    plt.show()
