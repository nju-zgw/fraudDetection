import networkx as nx
import Queue
import pandas as pd
import os
from pandas import Series
from sklearn.cross_validation import train_test_split


def init(queue,G,alpha):
    df = pd.read_csv('graph_pre.csv')


    no_train, no_test, label_train, label_test = train_test_split(df.no, df.label, test_size=1 - alpha)
    fraud_dict = Series(label_train, index=no_train).to_dict()

    for node in G.nodes:
        if fraud_dict.has_key(node) and fraud_dict[node]>0:
            G.add_nodes_from([node], belief=fraud_dict[node])
            queue.put(node)
    return [no_train, no_test, label_train, label_test]

def broadcast(filename):
    G = nx.DiGraph() # or DiGraph, MultiGraph, MultiDiGraph, etc
    queue = Queue.Queue()


    with open(filename,'r') as f:
        for line in f:
            item = line.split()
            G.add_edge(int(item[0]),int(item[1]))

   # pr = nx.pagerank(G, alpha=0.85)
    [no_train, no_test, label_train, label_test]= init(queue,G,0.8)

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

    fraud_dict = {}
    for (index,value) in label_test.iteritems():
        fraud_dict[no_test[index]] = value

    printBelief(G,fraud_dict,"res_test.csv")

def printBelief(G,test_dict,output="res_test.csv"):
    node_array = [0]*len(test_dict)
    belief = [0]*len(test_dict)
    acc = 0
    i = 0
    for (node,label) in test_dict.items():
        node_array[i] = (node)
        if 'belief' in G.nodes[node]:
            v = G.nodes[node]['belief']
            belief[i] = (v)
            acc = acc + abs(v - label)/label
        else:
            belief[i] = (0)
        i = i+1


    print('acc'+str(acc*1.0/len(test_dict)))
    save = pd.DataFrame({'no': node_array, 'label':test_dict.values(),'belief': belief})
    save[['no','label','belief']].to_csv(output)

if __name__ == "__main__":
    broadcast('../zgw_data/all_callrec_graph_num')
