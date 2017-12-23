# -*- coding:utf-8 -*-
import os
import sys
import time
import pickle
import numpy as np
import pandas as pd
import networkx as nx

def merge_app_per():    
    dtype_app = {'loan_key': str,
                 'user_key': str,
                 'mobile': str,
                 'idno': str,
                 'emit_amt': np.float64,
                 'emit_time':str,
                 'is_final_passed': np.int64,
                 'final_verify_time': str}

    dtype_per = {'loan_key': str,
                 'idno_prefix': str,
                 'mobile': str,
                 'person1': str,
                 'person2': str,
                 'final_verify_time': str,
                 'ip': str,
                 'latitude': np.float64,
                 'logitude': np.float64,
                 'due_date': str,
                 'payoff_time': str}

    df_app = pd.read_csv(os.path.join('/home', 'thunetwork', 'data', 'thunetwork', 'application', 'app.csv'), dtype=dtype_app)
    df_per = pd.read_csv(os.path.join('/home', 'thunetwork', 'data', 'thunetwork', 'performance', 'per.csv'), dtype=dtype_per)

    #df_loan = pd.concat([df_app.set_index('loan_key'), df_per.set_index('loan_key')], axis=1, join='inner')
    df_loan = pd.merge(df_app, df_per, how='outer')
    print(df_loan.dtypes)
    # print df_loan
    df_loan.to_csv('/opt/thunetwork/fraudDetection/zgw_src/loan.csv', index=True, sep=',')


def filter_callrec():
    for i in range(1, 7):
        filename = os.path.join('/home', 'thunetwork', 'data', 'thunetwork','callrec', '00000{}_0'.format(i))
        df = pd.read_csv(filename, names=['timestamp', 'idno', 'start_time', 'area', 'mode', 'to_mobile', 'mobile', 'duration', 'type', 'total_fee', 'carrier_code', 'normal_fee', 'roaming_fee'], sep='\t')
        dfn = df[['idno', 'mobile', 'to_mobile', 'mode', 'start_time', 'duration']]
        filename_new = '/opt/thunetwork/callrec_{}'.format(i)
        dfn.to_csv(filename_new, index=True, sep=',')
        print(i)

def create_graph():
    nodes = {}
    edges = {}
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
       
                if nodes.setdefault(mobile, idno) == '':
                    nodes[mobile] = idno
                
                nodes.setdefault(to_mobile, '')
        
                edge = (mobile, to_mobile)
                edges.setdefault(edge, [])
                edges[edge].append((mode, stime, duration))
            
            except Exception as e:
                print(e)
                continue
        
    print(len(nodes))
    print(len(edges))
      
    G = nx.Graph()
    for node in nodes.keys():
        G.add_node(node, idno=str(nodes[node]))
    for edge in edges.keys():
        G.add_edge(str(edge[0]), str(edge[1]), calls=str(edges[edge]))
    nx.write_gexf(G, "callrec_graph.gexf")
    pickle.dump(G, open("callrec_graph.pklb", 'wb'), True) 

  
if __name__=="__main__":
    create_graph()
    print('Done!')
