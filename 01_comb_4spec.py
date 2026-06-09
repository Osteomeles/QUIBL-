# coding=utf-8
from itertools import combinations
from ete3 import Tree
# 给定的元素，这里需要把sp都修改为自己的物种的名称
elements = ['sp1', 'sp2', 'sp3', 'sp4', 'sp5', 'sp6', 'sp7', 'sp8']

# 提取三个元素为一组
combs_3 = list(combinations(elements, 3))
 
# 每组加上'mcap'形成四个元素,Outgroup是外群的名称
combs_4 = [(comb[0], comb[1], comb[2], 'Outgroup') for comb in combs_3]

# 将每个组合写入文件中，每行一个组合
with open('out_four_species_array.txt', 'w') as file:
        for comb in combs_4:
                file.write(' '.join(comb) + '\n')
