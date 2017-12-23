import networkx as nx
import pandas as pd
import os
import time
import pickle


def create_graph():
    edges = []

    for i in range(0, 7):
        filename = '../../data/preprocess/callrec_{}'.format(i)
        df = pd.read_csv(filename)

        for k in range(1000):
            try:
                row = df.iloc[k]
                idno = str(row.idno)
                mobile = str(row.mobile)
                to_mobile = str(row.to_mobile)
                mode = int(row['mode'])
                stime = str(row.start_time)
                stime = time.mktime(time.strptime(stime, '%Y-%m-%d %H:%M:%S'))
                duration = int(row.duration)

                if mode == '1':
                    edge = (mobile, to_mobile)
                elif mode == '2':
                    edge = (to_mobile, mobile)

                edges.append(edge)

            except Exception as e:
                print(e)
                continue

    pickle.dump(edges, open("callrec_graph", 'wb'), True)


if __name__ == "__main__":
    create_graph()
    print('Done!')


    # G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
    # G = nx.Graph(name='my graph')
    # e = [(1, 2), (2, 3), (3, 4)] # list of edges
    # G = nx.Graph(e)
    #
    #
    # print (G.adj)
