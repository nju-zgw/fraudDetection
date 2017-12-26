import networkx as nx
import Queue
import os


def init(queue,G):

    queue.put(1)
    queue.put(27)
    queue.put(714636)

    G.add_nodes_from([1], belief=1)
    G.add_nodes_from([27], belief=1)
    G.add_nodes_from([714636], belief=1)

def broadcast(filename):
    G = nx.DiGraph() # or DiGraph, MultiGraph, MultiDiGraph, etc
    queue = Queue.Queue()

    with open(filename,'r') as f:
        for line in f:
            item = line.split()
            G.add_edge(int(item[0]),int(item[1]))

    pr = nx.pagerank(G, alpha=0.85)
    init(queue,G)

    alpha = 2.0

    while not queue.empty():
        now = queue.get()
        now_b = G.nodes[now]['belief']
        for nbr in G.successors(now):

            if 'belief' not in G.nodes[nbr]:
                G.add_nodes_from([nbr], belief=now_b*1.0/alpha)
                queue.put(nbr)
            else:
                G.add_nodes_from([nbr], belief= G.nodes[nbr]['belief'] + now_b * 1.0 / alpha)

    printBelief(G)

def printBelief(G):
    for node in G.nodes:
        if 'belief' in G.nodes[node]:
            print(node,G.nodes[node]['belief'])
        else:
            print(node, 0)

if __name__ == "__main__":
    broadcast('testg.txt')