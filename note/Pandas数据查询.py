'''
pandas中.loc查询数据的5种方法：
数值
列表
区间
条件
函数（这些方法既用于行，也用于列，注意观察降维DataFrame>Series>值'''
import pandas as pd

'''Pandas查询数据的几种方法
1.df.loc方法，根据行、列的标签值查询（既能查询，又能覆盖写入，强烈推荐）
2.df.iloc方法，根据行、列的数字位置查询
3.df.where方法
4.df.query方法
'''

'''0.读取数据'''
import pandas as pd
import csv

# 指定CSV文件的位置
df=pd.read_csv('C:\\Users\潘敏菊\Downloads\\test.csv')
print(df.head())
'''
查看前五行数据
   PassengerId  Pclass  ... Cabin Embarked
0          892       3  ...   NaN        Q
1          893       3  ...   NaN        S
2          894       2  ...   NaN        Q
3          895       3  ...   NaN        S
4          896       3  ...   NaN        S

[5 rows x 11 columns]'''
df.set_index('Pclass',inplace=True)#设置索引为日期，方便按日期查询
print(df.head)
'''
<bound method NDFrame.head of         PassengerId  ... Embarked
Pclass               ...         
3               892  ...        Q
3               893  ...        S
2               894  ...        Q
3               895  ...        S
3               896  ...        S
...             ...  ...      ...
3              1305  ...        S
1              1306  ...        C
3              1307  ...        S
3              1308  ...        S
3              1309  ...        C

[418 rows x 10 columns]>'''
print(df.index)
'''
Int64Index([3, 3, 2, 3, 3, 3, 3, 2, 3, 3,
            ...
            3, 3, 3, 1, 3, 3, 1, 3, 3, 3],
           dtype='int64', name='Pclass', length=418)
'''

# '''1.使用单个label值查询数据'''
#行或者列，都可以只传入单个值，实现精确匹配
print(df.loc[3,'Age'])#得到单个值（一维数据）
'''
Pclass
3    34.5
3    47.0
3    27.0
3    22.0
3    14.0
     ... 
3    28.0
3     NaN
3    38.5
3     NaN
3     NaN
Name: Age, Length: 218, dtype: float64'''

#2.使用值列表批量查询
print(df.loc[[3,2],'Age'])
'''
Pclass
3    34.5
3    47.0
3    27.0
3    22.0
3    14.0
     ... 
2    57.0
2    47.0
2    38.0
2    20.0
2    23.0
Name: Age, Length: 311, dtype: float64
'''

#3.使用数值区间进行范围查询
#print(df.loc[2:3,'Age'])
'''在这里这个代码无法执行。因为多行具有相同的索引'''

#4.使用条件表达式查询
print(df.loc[df['Age']<20,:])
'''
        PassengerId  ... Embarked
Pclass               ...         
3               897  ...        S
3               900  ...        C
3               913  ...        S
3               927  ...        C
3               947  ...        Q
...             ...  ...      ...
3              1281  ...        S
3              1284  ...        S
1              1287  ...        S
1              1295  ...        S
3              1301  ...        S
[61 rows x 10 columns]
'''
print(df['Age']<10)
'''
Pclass
3    False
3    False
2    False
3    False
3    False
     ...  
3    False
1    False
3    False
3    False
3    False
Name: Age, Length: 418, dtype: bool
'''
#复杂条件查询
print(df.loc[(df['Age']<70)&(df['Sex']=='male')])
'''
        PassengerId  ... Embarked
Pclass               ...         
3               892  ...        Q
2               894  ...        Q
3               895  ...        S
3               897  ...        S
2               899  ...        S
...             ...  ...      ...
1              1296  ...        C
2              1297  ...        C
2              1298  ...        S
1              1299  ...        C
3              1307  ...        S

[205 rows x 10 columns]'''


#5.调用函数查询
print(df.loc[lambda df : (df['Age']<30)&(df['Fare']>70), :])
#这个函数是用来进行的筛选
'''        PassengerId  ... Embarked
Pclass               ...         
1               904  ...        S
1               945  ...        S
1               956  ...        C
1              1042  ...        C
1              1048  ...        S
1              1076  ...        C
1              1088  ...        C
2              1104  ...        S
1              1144  ...        C
1              1164  ...        C
1              1179  ...        S
2              1244  ...        S
1              1282  ...        S

[13 rows x 10 columns]
'''




