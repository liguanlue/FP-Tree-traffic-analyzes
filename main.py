import pandas as pd
import numpy as np
import csv
from pprint import pprint

column = ["ID","time","longitude","latitude","passenger"]
data = pd.DataFrame(columns=column)
Sum = 0
same = 0
i = 0
line = "1"
data_list = []
with open("./data/20160901.txt",encoding='UTF-8') as file_txt:
    while i < 2000:
        i += 1
        line = file_txt.readline()
        if line.find("定位有效") == -1:
            continue
        if line.find("重车") > 0:
            flag = 1
        else:
            flag = 0
        Str = line.split('\t')
        Str[4] = round(int(Str[4]) / 10)
        Str[5] = round(int(Str[5]) / 10)
        data.loc[data.shape[0]+1]={"ID":Str[1],"time":Str[2],"longitude":Str[4],"latitude":Str[5],"passenger":flag}
        data_list.append([Str[1],Str[2],str(Str[4])+str(Str[5])])
        Sum += 1
pprint(data_list)
print("sum")
print(sum)
data.to_csv("./data/data.csv",index=True,sep=' ')
