#_*_ coding:utf-8 _*_


import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import os
import sys
#import networkx as nx

def getDataframe(name, id):
    """
    读取项目数据
    
    name:文件类型，包括：
         ’application‘：贷款
         'performance': 贷款表现
         ’call': 通话记录
         'sms': 短信记录
    
    id: 文件序号，
        贷款文件有2个，id取值0或1
        贷款表现文件有2个，id取值0或1
        通话记录文件有7个，id取值0,1,...,6
        短信记录文件有2个，id取值0或1
    """
    filepath = os.path.join(os.pardir, "data", "thunetwork")

    names_call= ['timestamp', 'idno', 'start_time', 'area', 'mode', 'to_mobile', 'mobile', 'duration', 'type', 'total_fee', 'carrier_code', 'normal_fee', 'roaming_fee']
    names_app = ['loan_key', 'user_key', 'mobile', 'idno', 'emit_amt','emit_time', 'is_final_passed', 'final_verify_time']
    names_per = ['loan_key', 'idno_prefix', 'mobile', 'person1', 'person2', 'final_verify_time', 'ip', 'latitude', 'logitude', 'due_date', 'payoff_time']
    names_sms = ['timestamp', 'idno', 'start_time', 'area', 'target_phone', 'mode', 'infor_type', 'business_name', 'total_fee', 'user_phone']
    
    names = {}
    names.setdefault('application', names_app)
    names.setdefault('performance', names_per) 
    names.setdefault('call', names_call)
    names.setdefault('sms', names_sms)
  
    path_app = os.path.join(filepath, 'application')
    path_per = os.path.join(filepath, 'performance')
    path_call = os.path.join(filepath, 'callrec')
    path_sms = os.path.join(filepath, 'sms')
    
    paths={}
    paths.setdefault('application', path_app)
    paths.setdefault('performance', path_per)
    paths.setdefault('call', path_call)
    paths.setdefault('sms', path_sms)

    filename = os.path.join(paths[name], '00000{}_0'.format(id))
    if not os.path.isfile(filename):
        print filename
        print 'not exist!'
        return None
    df = pd.read_csv(filename, sep='	', header=None, names=names[name])
    return df

def merge():
    """
    合并文件，将较小的贷款、贷款表现文件各合并为1个
    """

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
   
   df_loan = pd.concat([df_app.set_index('loan_key'), df_per.set_index('loan_key')], axis=1, join='inner')
  
   f_df_loan = os.path.join('..', 'data', 'thunetwork', 'loan', 'loan.csv')
   df_loan.to_csv(f_df_loan, index=True, sep=',')

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
   
   # name = 'performance' 
   # fileid = [0, 1]
   # for id in fileid:
   #     df = getDataframe(name, id)
        
#       print df.loan_key
#	print df.idno_prefix
#	print df.mobile
#	print df.person1
#	print df.person2
#	print df.final_verify_time
#	print df.ip
#	print df.latitude
#	print df.logitude
#	print df.due_date
#	print df.payoff_time
 
#    name = 'call'
#    df = getDataframe(name, 0)
#    print df.dtypes
#    print df.describe()
#    for i in range(3):
#        print df.iloc[i] 
#        print '\n'
#
 
if __name__=="__main__":
    main()
