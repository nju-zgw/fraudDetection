import networkx as nx
import pandas as pd
import os
import time
import pickle


filename = '../jyf_src/loan.csv'

df = pd.read_csv(filename)


label = [0]*len(df)

for k in range(len(df)):
    row=df.iloc[k]
    finaltime=str(row.final_verify_time)
    due=str(row.due_date)
    payoff=str(row.payoff_time)
    mobile=str(row.mobile)
    if payoff=="\\N" and due=="\\N":
        label[k]=0.5	
    elif payoff=="\\N" and due!="\\N":
        label[k]=1
    else:
        label[k] = 0
    
df.insert(0,'label',label)
df1 = df[['mobile','label']]
df1.to_csv('../cxw/label.csv')

