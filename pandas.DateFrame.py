#DataFrame是一个表格型数据结构
#每行可以是不同的值类型（数值，字符串，布尔值等）
#既有行索引index，也有列索引columns
#可以被看作由Series组成的字典
import pandas as pd
print('根据多个字典序列创建dataframe')
data={
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}
print(data)
df=pd.DataFrame(data)
print(df)
'''{'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9'''
print('每一列类型')
print(df.dtypes)
'''每一列类型
state     object
year       int64
pop      float64
dtype: object'''
print('列索引')
print(df.columns)
'''Index(['state', 'year', 'pop'], dtype='object')'''
print('行索引')
print(df.index)
'''RangeIndex(start=0, stop=5, step=1)'''

'''从DataFrame中查出Series'''
#如果只查询一行，一列，返回的是pd.Series
#如果查询多行，多列，返回的是pd.DataFrame
print('3.1查询一列，结果是一个pd.Series')
print(df['year'])
print(type(df['year']))
'''
0    2000
1    2001
2    2002
3    2001
4    2002
Name: year, dtype: int64
<class 'pandas.core.series.Series'>
'''

print('3.2查询多列，结果是一个pd.Dataframe')
print(df[['year','pop','state']])
print(type(df[['year','pop','state']]))
'''
   year  pop   state
0  2000  1.5    Ohio
1  2001  1.7    Ohio
2  2002  3.6    Ohio
3  2001  2.4  Nevada
4  2002  2.9  Nevada
<class 'pandas.core.frame.DataFrame'>'''


print('3.3查询一行，结果是一个pd.Series')
print(df.loc[1])
print(type(df.loc[1]))
'''
state    Ohio
year     2001
pop       1.7
Name: 1, dtype: object
<class 'pandas.core.series.Series'>
'''

print('查询多行，结果是一个pd.DataFrame')
print(df.loc[1:3])#这里和python不一样，末尾元素要包含进去
print(type(df.loc[1:3]))
'''
    state  year  pop
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
<class 'pandas.core.frame.DataFrame'>'''