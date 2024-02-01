'''pandas数据结构
            #1.Series
            # 2.DataFrame
            # 3.从DataFrame中查询出Series
'''
import pandas as pd
import numpy as np
'''Series是一种类似于一维数组的对象，它由一组数据（不同数据类型）以及
    与之相关的数据标签（即索引）组成'''
s1=pd.Series([1,'a',5.2,7])#左侧是索引，右侧是数据
print('''1.1仅由数据列表即可产生最简单的Series''')
print(s1)
print(s1.index)#获取索引
print(s1.values)#获取数据

s2 = pd.Series([1, 'a', 5.2, 7], index=['d', 'b', 'a', 'c'])
print('''1.2创建一个具有标签索引的Series''')
print(s2)
print(s2.index)

sdata={'Ohio':35000,'Texas':72000,'Oregon':16000,'Utah':5000}
s3=pd.Series(sdata)
print('1.3使用Python字典创建Series')
print(s3)

print('1.4根据标签索引查询数据（类似于Python的字典dict）')
print(s2['a'])
print(type(s2['a']))
print(s2[['a','b']])
print(type(s2[['b','a']]))




