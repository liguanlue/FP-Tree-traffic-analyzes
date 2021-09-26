import collections
from pprint import pprint
support = 2
data = []
CountItem = collections.defaultdict(int)

with open("./data/20160901.txt",encoding='UTF-8') as file_txt:
    for i in range(20000):
        line = file_txt.readline()
        if line.find("定位有效") == -1:
            continue
        Str = line.split('\t')
        Str[4] = round(int(Str[4]) / 10)
        Str[5] = round(int(Str[5]) / 10)
        data.append([Str[1],Str[2],str(Str[4])+str(Str[5])])
        CountItem[Str[1]] += 1
        CountItem[Str[2]] += 1
        CountItem[str(Str[4])+str(Str[5])] += 1
a = sorted(CountItem.items(),key=lambda x:x[1],reverse=True)
for i in range(len(a)):
    if a[i][1] < support:
        a = a[:i]
        break
for i in range(len(data)):
    data[i] = [char for char in data[i] if CountItem[char] >= support]
    data[i] = sorted(data[i], key=lambda x:CountItem[x],reverse=True)
pprint(data)

class node(object):
    def __init__(self,val,char):
        self.val = val #当前节点计数
        self.char = char  #节点字符
        self.children = {}
        self.next = None #链表，连接到另一个孩子处
        self.father = None
        self.visit = 0


class FPTree(object):
    def __init__(self):
        self.root = node(-1, 'root')
        self.FrequentItem =collections.defaultdict(int)

    def BuildTree(self,data):
        for line in data:
            root = self.root
            for item in line:
                if item not in root.children.keys():
                    root.children[item] = node(1,item)
                    root.children[item].father = root
                else :
                    root.children[item].val += 1
                root = root.children[item]


