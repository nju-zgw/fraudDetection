import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import os
import sys
#import networkx as nx

def getDataframe(name, id):

    filepath = os.path.join(os.pardir, "data", "thunetwork")


 #   names_call= ['timestamp', 'idno', 'start_time', 'area', 'mode', 'to_mobile', 'mobile', 'duration', 'type', 'total_fee', 'carrier_code', 'normal_fee', 'roaming_fee']
    names_app = ['loan_key', 'user_key', 'mobile', 'idno', 'emit_amt','emit_time', 'is_final_passed', 'final_verify_time']
    names_per = ['loan_key', 'idno_prefix', 'mobile', 'person1', 'person2', 'final_verify_time', 'ip', 'latitude', 'logitude', 'due_date', 'payoff_time']
#    names_sms = ['timestamp', 'idno', 'start_time', 'area', 'target_phone', 'mode', 'infor_type', 'business_name', 'total_fee', 'user_phone']

    names = {}
    names.setdefault('application', names_app)
    names.setdefault('performance', names_per)
 #   names.setdefault('call', names_call)
 #   names.setdefault('sms', names_sms)

    path_app = os.path.join(filepath, 'application')
    path_per = os.path.join(filepath, 'performance')
 #   path_call = os.path.join(filepath, 'callrec')
 #   path_sms = os.path.join(filepath, 'sms')

    paths={}
    paths.setdefault('application', path_app)
    paths.setdefault('performance', path_per)
 #   paths.setdefault('call', path_call)
 #   paths.setdefault('sms', path_sms)

    filename = os.path.join(paths[name], '00000{}_0'.format(id))
    if not os.path.isfile(filename):
        print filename
        print 'not exist!'
        return None
    df = pd.read_csv(filename, sep='    ', header=None, names=names[name])
    return df

def merge():
    f_app = os.path.join('..', 'data', 'thunetwork', 'application', 'app.csv')
    f_per = os.path.join('..', 'data', 'thunetwork', 'performance', 'per.csv')
    df_app = pd.read_csv(f_app)
    df_per = pd.read_csv(f_per)


def main():
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

   df_app = pd.read_csv(os.path.join('..', 'data', 'thunetwork', 'application', 'app.csv'), dtype=dtype_app)
   df_per = pd.read_csv(os.path.join('..', 'data', 'thunetwork', 'performance', 'per.csv'), dtype=dtype_per)

   #df_loan = pd.concat([df_app.set_index('loan_key'), df_per.set_index('loan_key')], axis=1, join='inner')

   f_df_app = os.path.join('..', 'data', 'thunetwork', 'fraudDetection','data', 'app.csv')

   f_df_per = os.path.join('..', 'data', 'thunetwork', 'fraudDetection','data', 'per.csv')
   df_app.to_csv(f_df_app, index=True, sep=',')
 # df_loan.to_csv(f_df_info, index=True, sep=',')

   # name = 'application'
   # fileid = 0
   # df = getDataframe(name, fileid)

   # 
   # print df.loan_key  
   # print df.user_key
   # print df.mobile
   # print df.idno
   # print df.emit_amt
   # print df.emit_time
   # print df.is_final_passed
   # print df.final_verify_time
   # print sum(df.is_final_passed)
