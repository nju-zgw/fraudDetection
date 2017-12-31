import struct
import pandas as pd

if __name__ == "__main__":
    byte_len = 4
    nodes = []
    vectors = []
    with open('vec_all.txt', 'rb') as fd:
        line = fd.readline()
        infos = line.split(' ')
        num_v = int(infos[0])
        dim = int(infos[1])
        i = 0
        while 1:
            line = fd.readline()
            vec = [0]*dim
            if i == 0:
                index = line.find(' ')
                nodes.append(line[0:index])
                line = line.replace('\n', '')
                line = line[index + 1:]
            j = 0
            while j < len(line):
                bf = struct.unpack('f', line[j:j + 4])
                vec[i] = (bf)
                j = j + 4
                i = i + 1
            if i == dim:
                vectors.append(vec)
                if len(nodes) == num_v:
                    break
                i = 0
    df = pd.DataFrame({'nodes':nodes,'embedding':vectors})
    df[['nodes','embedding']].to_csv('embedding.csv')
   # print(nodes,vectors)
