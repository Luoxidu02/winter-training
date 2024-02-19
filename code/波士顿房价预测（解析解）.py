import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 添加一个支持中文字符的字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc")

plt.rcParams['font.sans-serif'] = [font.get_name()]  # 设置默认字体
plt.rcParams['axes.unicode_minus'] = False

def load_data():
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

    #定义全局变量，最后好进行反归一化
    # global max_values
    # global min_values
    # global avg_values
    # max_values = maximums
    # min_values = minimums
    # avg_values = avgs

    # 划分训练集，测试集
    ratio = 0.8
    offset = int(data.shape[0]*ratio)
    training_data = data[:offset]
    test_data = data[offset:]
    return training_data,test_data


def add_bias(X):
    # 为特征矩阵X添加偏置项（全1列）
    return np.hstack([np.ones((X.shape[0], 1)),X])#最后一列全是一


def normal_equation_regression(X_train, y_train):
    # 计算权重的解析解
    theta = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)
    return theta


def predict(X_test, theta):
    # 使用权重进行预测
    return X_test.dot(theta)


def mean_squared_error(y_true, y_pred):
    # 计算均方误差
    return ((y_true - y_pred) ** 2).mean()


# 获取数据
train_data, test_data = load_data()
X_train_std = x_train = train_data[:, :-1]  # 训练集的特征值
y_train = train_data[:, -1:]  # 训练集的目标值
X_test_std = x_test = test_data[:, :-1]  # 测试集的特征值
y_test = test_data[:, -1:]  # 测试集的目标值


class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # 初始化权重和偏置
        self.weights = np.zeros(n_features)
        self.bias = 0

        # 梯度下降
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            # 计算梯度
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # 更新权重和偏置
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted


# 实例化模型
model = LinearRegression(learning_rate=0.01, n_iters=1000)

# 训练模型
model.fit(X_train_std, y_train)

# 进行预测
y_pred = model.predict(X_test_std)

# 计算均方误差
mse = np.mean((y_test - y_pred) ** 2)
print("Mean Squared Error:", mse)


