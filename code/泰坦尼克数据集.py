import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
from IPython.display import display
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 添加一个支持中文字符的字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc")

plt.rcParams['font.sans-serif'] = [font.get_name()]  # 设置默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
#加载数据
df=pd.read_csv ('C:\\Users\潘敏菊\Downloads\\train.csv')
#查看缺失值
print(df.isnull().sum())
#Age,Embarked,Cabin存在缺失值
#Fare只存在1个缺失值，将Fare的众数赋给缺失值
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode().iloc[0])
#Cabin大部分缺失，且不缺失的样本存活率远高于缺失样本，则将cabin是否缺失作为新的变量
df['cabin_na']=df['Cabin'].isnull()#创建一个新的列，如果Cabin中的值缺失，则Cabin_na的值为False
#根据cabin_na列的值来进行分组，所有Cabin_na为True的行被分为一组，为False的分为一组
#   cabin_na  Survived
#0     False  0.666667
#1      True  0.299854
cabin_prec=df[['cabin_na','Survived']].groupby(['cabin_na'],as_index=False).mean()
fig, (axis1,axis2) =plt.subplots(1,2,figsize=(10,4))
sns.countplot(x='cabin_na',data=df,ax=axis1)
sns.barplot(x='cabin_na',y='Survived',data=cabin_prec,ax=axis2)
axis1.set_xticklabels(['has_cabin','lose_cabin'],rotation=0)
axis2.set_xticklabels(['has_cabin','lose_cabin'],rotation=0)
sex_count=df.groupby(by='Sex')['Survived'].value_counts()
'''
Sex     Survived
female  1           233
        0            81
male    0           468
        1           109'''
plt.figure(figsize=(2*5,5))
#按性别分
axes1 = plt.subplot(1,2,1)
axes1.pie(sex_count.loc['female'],explode = [0.05,0.05],labels=['Surivie','die'], autopct='%1.2f%%', shadow=True)
axes1.set_title("women suvive")

axes2 = plt.subplot(1,2,2)
axes2.pie(sex_count.loc['male'],explode = [0.05, 0.05],labels=['Surivie','die'], autopct='%1.2f%%', shadow=True,colors=['pink','#AFEEEE'])
axes2.set_title("men suvive")

#按年龄分类
age_range =df['Age']
age_num,_ = np.histogram(age_range,range=[0,80],bins=16)
age_survived = []
for age in range(5,81,5):
    survived_num = df.loc[(age_range>=age-5)&(age_range<=age)]['Survived'].sum()
    age_survived.append(survived_num)
plt.figure(figsize=(12,6))
plt.bar(np.arange(2,78,5)+0.5,age_num,width=5,label='allaccount',color='seagreen')
plt.bar(np.arange(2,78,5)+0.5,age_survived,width=5,label='suvivaccount',color='royalblue')
plt.xticks(range(0,81,5))
plt.yticks(range(0,121,10))
plt.xlabel('age',position=(0.95,0),fontsize=15)
plt.ylabel('account',position=(0,0.95),fontsize=15)
plt.title('people about suvive')
plt.grid(True,linestyle=':',alpha=0.6)


#按embark登入港口来分
embarked_count = df.groupby(by='Embarked')['Survived'].value_counts()
plt.figure(figsize=(3*5,5))

first=plt.subplot(1,3,1)
first.pie(embarked_count.loc['C'],autopct='%1.2f%%',labels=['die','surivive'],pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0.05,0.05],textprops=dict(size=15),colors=['coral','darkseagreen'])
first.set_title('法国')

first=plt.subplot(1,3,2)
first.pie(embarked_count.loc['Q'],autopct='%1.2f%%',labels=['die','surivive'],pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0.05,0.05],textprops=dict(size=15),colors=['gold','dodgerblue'])
first.set_title('爱尔兰')

first=plt.subplot(1,3,3)
first.pie(embarked_count.loc['S'],autopct='%1.2f%%',labels=['die','surivive'],pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0.05,0.05],textprops=dict(size=15),colors=['lightblue','darkkhaki'])
first.set_title('英国')


#按船舱等级来分类
pclass_count = df.groupby(by='Pclass')['Survived'].value_counts()
plt.figure(figsize=(3*5,5))

axes1=plt.subplot(1,3,1)
axes1.pie(pclass_count.loc[1][::-1],autopct='%.2f%%',labels=['die','suvive'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=['#9400D3','#FFB6C1'],startangle=45)
axes1.set_title('class1')
t1 = plt.subplot(1,3,2)
t1.pie(pclass_count.loc[2],startangle=60,autopct='%.2f%%',labels=['die','suvive'],pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0.05,0.05],textprops=dict(size=15),colors=['darkseagreen','coral'])
t1.set_title('class2')
t3 = plt.subplot(1,3,3)
t3.pie(pclass_count.loc[3],startangle=30,autopct='%.2f%%',labels=['die','suvive'],shadow=True,pctdistance=0.4,labeldistance=0.6,explode=[0.05,0.05],colors=['gold','dodgerblue'],textprops=dict(size=15))
t3.set_title('class3')


#按票价来分
fare_count = df.groupby(by='Fare')['Survived'].value_counts()
fare_count = pd.DataFrame(fare_count)
fare_count.rename(columns={'Survived':'Number'},inplace=True)
fare_count.reset_index(inplace=True)
fare_num = fare_count.groupby(by='Fare')['Number'].sum()
fare_num = pd.DataFrame(fare_num)
fare_num.rename(columns={'Number':'Total'},inplace=True)
fare_survived = fare_count.loc[fare_count['Survived']==1]
fare_survived = fare_survived.merge(fare_num,left_on='Fare',right_index=True,how='inner')
survived_rate = fare_survived['Number'].div(fare_survived['Total'])
survived_rate.index = fare_survived['Fare']
fare_death = fare_count.loc[fare_count['Survived']==0]
fare_death = fare_death.merge(fare_num,left_on='Fare',right_index=True,how='inner')
death_rate = fare_death['Number'].div(fare_death['Total'])
death_rate.index = fare_death['Fare']
plt.figure(figsize=(2*10,5))

# 乘客的生还率和票价关系散点图
axes1=plt.subplot(1,2,1)
axes1.scatter(survived_rate.index,survived_rate,marker='o',color='r')
axes1.set_title('乘客生还率和票价关系散点图')

# 乘客的死亡率和票价关系散点图
axes2=plt.subplot(1,2,2)
axes2.scatter(death_rate.index,death_rate,marker='^',color='b')
axes2.set_title('乘客死亡率和票价关系散点图')
plt.show()
