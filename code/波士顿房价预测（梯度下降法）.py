import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 添加一个支持中文字符的字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc")

plt.rcParams['font.sans-serif'] = [font.get_name()]  # 设置默认字体
plt.rcParams['axes.unicode_minus'] = False


datafile = "C:\\Users\潘敏菊\Desktop\housing.csv"
data = np.fromfile(datafile,sep=' ')
feature_names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
                     'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
feature_num = len(feature_names)
data = data.reshape(data.shape[0]//feature_num,feature_num)

#对数据进行归一化
maximums,minimums,avgs = data.max(axis=0),data.min(axis=0),data.sum(axis=0)/data.shape[0]
for i in range(feature_num):
   data[:,i] = (data[:,i]-minimums[i])/(maximums[i]-minimums[i])

# 划分训练集，测试集
ratio = 0.8
offset = int(data.shape[0]*ratio)
train_data = data[:offset]
test_data = data[offset:]

x_train = train_data[:, :-1]  # 训练集的特征值
y_train = train_data[:, -1:]  # 训练集的目标值
x_test = test_data[:, :-1]  # 测试集的特征值
y_test = test_data[:, -1:]  # 测试集的目标值

# 为特征矩阵在左边添加偏置项（全为1的1列）
xtrain = np.hstack([np.ones((x_train.shape[0], 1), dtype=float), x_train])
xtest = np.hstack([np.ones((x_test.shape[0], 1), dtype=float), x_test])

#初始化权重
weight = np.random.randn(xtrain.shape[1]).reshape(-1,1)#weights是一竖条，有14行，每行只有一个数

#梯度下降参数
learning_rate = 0.01
epochs = 10000
tolerance = 1e-4

#梯度下降
for epoch in range(epochs):
    y_pred = xtrain.dot(weight).reshape(-1,1)#也是一竖条，每行只有一个数
    error = y_pred-y_train#同上
    # print(y_train.shape)
    # print(y_pred.shape)
    # print(error.shape)
    gradient = xtrain.T.dot(error)/len(xtrain)#梯度是由偏导数组成的向量
    # print(gradient.shape)
    weight -= learning_rate*gradient
    #检查收敛性
    if np.linalg.norm(gradient)<tolerance:
        break
#预测
y_pred_test = np.dot(xtest, weight)

#计算均方误差
error = ((y_test-y_pred_test)**2).mean()

# 设置画布大小，以适应多个图
plt.figure(figsize=(21, 28))
# 创建一个 4x4 的子图网格，并设置最后一行只有一个子图
#画13个散点图，查看预测值与实际值
for i in range(13):
    # 使用 subplots() 函数创建一个子图，sharex=True 和 sharey=True 使得所有子图共享x轴和y轴刻度
    if i < 12:
        plt.subplot(4, 4, i + 1)  # 4x4网格中的第i+1个子图
    else:
        plt.subplot(4, 4, 13)  # 最后一行只有一个子图

    # 绘制散点图
    plt.scatter(x_test[:, i], y_test, color='blue', label='房价实际值')  # 使用scatter代替plot来创建散点图
    plt.scatter(x_test[:, i], y_pred_test, color='red', marker='x', label='房价预测值')  # 使用不同的标记来区分预测值

    plt.legend()
    plt.xlabel('%s值'%(feature_names[i]))
    plt.ylabel('房价')

plt.show()
print('均方误差为：%f'%(error))




