import networkx as nx
import pandas as pd
import os

def loadData(name ,id):
    names_call = ['timestamp', 'idno', 'start_time', 'area', 'mode', 'to_mobile', 'mobile', 'duration', 'type',
                  'total_fee', 'carrier_code', 'normal_fee', 'roaming_fee']
    names_app = ['loan_key', 'user_key', 'mobile', 'idno', 'emit_amt', 'emit_time', 'is_final_passed',
                 'final_verify_time']
    names_per = ['loan_key', 'idno_prefix', 'mobile', 'person1', 'person2', 'final_verify_time', 'ip', 'latitude',
                 'logitude', 'due_date', 'payoff_time']
    names_sms = ['timestamp', 'idno', 'start_time', 'area', 'target_phone', 'mode', 'infor_type', 'business_name',
                 'total_fee', 'user_phone']

    names = {}
    names.setdefault('application', names_app)
    names.setdefault('performance', names_per)
    names.setdefault('call', names_call)
    names.setdefault('sms', names_sms)

    filepath = os.path.join('/home', 'thunetwork', 'data', 'thunetwork')

    path_app = os.path.join(filepath, 'application')
    path_per = os.path.join(filepath, 'performance')
    path_call = os.path.join(filepath, 'callrec')
    path_sms = os.path.join(filepath, 'sms')

    paths = {}
    paths.setdefault('application', path_app)
    paths.setdefault('performance', path_per)
    paths.setdefault('call', path_call)
    paths.setdefault('sms', path_sms)

    filename = os.path.join(paths[name], '00000{}_0'.format(id))
    if not os.path.isfile(filename):
        print filename
        print 'not exist!'
        return None
    df = pd.read_csv(filename, sep='    ', header=None, names=names[name])
    return df

if __name__=="__main__":
    df = loadData('call',0);
    print df[1:10,]

    # G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
    # G = nx.Graph(name='my graph')
    # e = [(1, 2), (2, 3), (3, 4)] # list of edges
    # G = nx.Graph(e)
    #
    #
    # print (G.adj)
