import networkx as nx
import Queue
import pandas as pd
import os
from pandas import Series



def init(queue,G):
    df = pd.read_csv('graph_pre.csv')
    fraud_dict = Series(df.label.values, index=df.no).to_dict()

    for node in G.nodes:
        if node in fraud_dict[node] and fraud_dict[node]>0:
            G.add_nodes_from([node], belief=fraud_dict[node])
            queue.put(node)

def broadcast(filename):
    G = nx.DiGraph() # or DiGraph, MultiGraph, MultiDiGraph, etc
    queue = Queue.Queue()

    with open(filename,'r') as f:
        for line in f:
            item = line.split()
            G.add_edge(int(item[0]),int(item[1]))

   # pr = nx.pagerank(G, alpha=0.85)
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