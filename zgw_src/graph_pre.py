# coding: utf-8
import pandas as pd
import codecs
from pandas import Series

if __name__ == "__main__":
    print ('start trans')
    label_file = 'label.csv'
    df = pd.read_csv(label_file)
    fraud_dict = Series(df.label.values, index=df.mobile).to_dict()


    table_file = "all_callrec_graph_num"
    doc = codecs.open(table_file, 'rU', 'UTF-8')
    all_mobile = pd.read_csv(doc,names=['mobile','no'],header = None,sep='\t')
    label = [0] * len(all_mobile)


    for i in range(len(all_mobile)):
        row = all_mobile.iloc[i]
        if row['mobile'] in fraud_dict:
            label[i] = fraud_dict[row['mobile']]
        else:
            label[i] = 0
    all_mobile.insert(2,'label',label)

    all_mobile[['mobile','label']].to_csv('graph_pre.csv')
    print ('end trans')