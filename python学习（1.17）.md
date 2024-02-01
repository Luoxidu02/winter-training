# 



- ## <font color='blue'>数据类型</font>

  ###   1.<font color='orange'>整数类型-int</font>

  - 整数就是没有小数部分的数字，`Python` 中的整数包括正整数、0 和负整数。

  ```python
  n = 78
  print(n)
  print(type(n))
  ```

  在Python中，可以使用多种进制来表示整数：

  - 十进制形式：每位用十种状态计数，逢十进一，写法是0~9。

    > 注意，使用十进制形式的整数不能以 0 作为开头，除非这个数值本身就是 0。

  - 二进制形式：每位用二种状态计数，逢二进一，写法是<font color='orange'><u>0b</u></font>开头，后跟0或者1。

  - 八进制形式：每位用八种状态计数，逢八进一，写法是<u>0o</u>开头，后跟0~7。

  - 十六进制形式：每位用十六种状态计数，逢十六进一，写法是<u>0x</u>开头，后跟0~9,A~F,a~f

### 	2.<font color='orange'>浮点数-float</font>

​		在编程语言中，小数通常以浮点数的形式存储。Python中的小数有两种书写形式

- 十进制形式

  - 就是我们平时看到的小数形式，例如 34.6、346.0、0.346。

    > 书写小数时必须包含一个小数点，否则会被 Python 当作整数处理。

- 指数形式

  ```text
  aEn 或 aen
  ```

  - a为尾数部分，是一个十进制数，n为指数部分，是一个十进制整数。
  - `E`或`e`是固定的字符，用于分割尾数部分和指数部分
  - 2.1E5 = 2.1×105
  - 3.7E-2 = 3.7×10-2

  > 只要写成指数形式就是小数，例如 14E3 等价于 14000.0

### 	3.<font color='orange'>字符串-str</font>

​	字符串由单引号、双引号、多引号包裹。字符串的内容可以包含字母、标点、特殊符号、中文、日文等全世界的所有文字。

- 内置函数ord（）可以把字符转换成Unicode码

- 内置函数chr（）可以把十进制数字转换成对应的字符

  ```python
  ord('A')  #65
  ord('高') #39640
  chr(66)   #'B'
  ```

- 连续三个单引号或双引号，在长字符串中会保留原始的格式，例如

```python
s='''
	I
		live
			me'''
print(s)
```

- 不换行打印，可以加上end="任意字符串"

```python
print("ss",end="")
print('ss',end='#')   #  ssss#
```

- 从控制台读取字符串

```
myname=input("请输入名字:")
print("您的名字是:"+myname)   #请输入名字:haha
                             您的名字是:haha
```



- 允许空字符串的存在，不包含任何字符且长度为0

```python
c=''
print(len(c))   #0
```

- 字符串中的引号问题：当字符串内容中出现引号时，我们需要进行特殊处理，否则 	Python 会解析出错

```python
str1 = 'I'm a great coder!'
```

使用不同的引号包围字符串：如果字符串内容中出现了单引号，那么我们可以使用双引号包围字符串，反之亦然。

```python
str1 = "I'm a great coder!"
```

### 	4.<font color='orange'>布尔值-bool</font>

真-true，假-false



- ## <font color='blue'>数据结构</font>

## <font color='orange'>1. 字符串</font>

字符串，用来存储描述性质的数据。例如：姓名、地址、自我介绍等。字符串是一个有序的字符的集合

> str()可以将任意数据类型转换成字符串类型,字符串是不可变的

### 1.1 字符串的内置功能

我们在开发程序时需要频繁对数据进行操作，为了提升我们的开发效率， python针对这些常用的操作，为每一种数据类型内置了一系列方法。我们现在要学习的是python为我们提供的这些方法

1. `strip`移除字符串首尾的空白字符(空格、\n、\t)，得到一个新字符串

   ```python
   str1 = ' hello world' 
   print(str1.strip())
   ```

2. 判断字符串是否以 XX 开头`startswith`/XX结尾`endswith`，得到一个布尔值

   ```python
   str2 = 'hello world'
   print(str2.endswith('L'))
   
   str3 = 'hello world'
   print(str3.endswith('L'))
   ```

3. 判断字符串是否是数字组成`isdigit`，返回结果为True或False

   ```python
   str4 = '5201314'
   print(str4.isdigit())
   ```

4. 字符串变大写`upper`/小写`lower`，得到一个新字符串

   ```python
   str5 = 'My nAme is tonY！'
   print(str5.lower())  # 将英文字符串全部变小写
   print(str5.upper())  # 将英文字符串全部变大写
   ```

5. 用新的字符替换字符串中旧的字符`replace`

   ```python
   str6 = 'my name is xxx, my age is 18!'  # 将xxx的年龄由18岁改成73岁
   print(str6.replace('18', '73'))  # 语法:replace('旧内容', '新内容')
   ```

6. <u>格式化输出</u>`format`

   1. **使用`%`操作符**：这是最原始的字符串格式化方法。

   ```python
   name = "张三"  
   age = 30  
   print("我的名字是%s，我%d岁了。" % (name, age))
   ```

   2.**使用`str.format()`方法**：这种方法更加灵活，提供了更多的控制选项。

   ```python
   name = "张三"  
   age = 30  
   print("我的名字是{}，我{}岁了。".format(name, age))
   ```

   ```python
   python复制代码
   
   print("我的名字是{name}，我{age}岁了。".format(name=name, age=age))
   ```

   ```python
   str7 = 'my name is {}, my age is {}!'.format('tony', 18)
   print(str7)   #my name is tony, my age is 18!
   ```

   字符串切割`split`，得到一个列表

   ```python
   # 括号内不指定字符，默认以空格作为切分符号
   str8 = 'hello world'
   print(str8.split())  #['hello', 'world']
   
   # 括号内指定分隔字符，则按照括号内指定的字符切割字符串
   str9 = '127.0.0.1'
   print(str9.split('.'))  #['127', '0', '0', '1']
   ```

### 1.2 通用操作

- 相加：字符串 + 字符串

- 相乘：字符串 * 整数

- 求长度：len函数

- 索引

  ```python
  # 正向索引从0开始，第二个索引为1，最后一个为len(s)-1。
  # 反向索引从-1开始,-1代表最后一个,-2代表倒数第二个,以此类推,第一个是-len(s)。
  
  str10 = 'hello python!'
  # 1.按索引取值(正向取，反向取)：
  # 1.1 正向取(从左往右)
  print(str10[6])  # p
  
  # 1.2 反向取(负号表示从右往左)
  print(str10[-4])  # h
  ```

- 获取字符串中的子序列，切片

  ```python
  # 2.切片(顾头不顾尾，步长)
  # 2.1 顾头不顾尾：取出索引为0到8的所有字符
  print(str10[0:9]) # hello pyt
  # 2.2 步长：0:9:2,第三个参数2代表步长，会从0开始，每次累加一个2即可，所以会取出索引0、2、4、6、8的字符
  print(str10[0:9:2] )   # hlopt 
  ```

- for循环取值

  ```python
  str11 = '中职通教育'
  
  # 依次取出字符串中每一个字符，赋值给变量i
  for i in str11:
      print(i)
  ```

- 成员运算符：`数据 in 字符串` 如果在指定的字符串中找到值，返回bool类型。

## 2.<font color='orange'> 列表</font>

在实际开发中，经常需要将多个数据存储起来，以便后边的代码使用。列表`list`，是一个有序且可变的容器，在里面可以存放多个不同类型的元素。

列表会将所有元素都放在一对中括号`[ ]`里面，相邻元素之间用逗号`,`分隔

```python
[element1, element2, element3, ..., elementn]
```

> element1 ~ elementn 表示列表中的元素，个数没有限制，只要是 Python 支持的数据类型就可以。
>
> 虽然可以将不同类型的数据放入到同一个列表中，但通常情况下不这么做，同一列表中只放入同一类型的数据，这样可以提高程序的可读性。
>
> 类型转换：只要能被for循环遍历的数据类型都可以传给list()转换成列表类型，list()会跟for循环一样遍历出数据类型中包含的每一个元素然后放到列表中

### 2.1 列表的内置功能

- 字符串，不可变，即：创建好之后内部就无法修改。【内置功能都是新创建一份数据】

- 列表，可变，即：创建好之后内部元素可以修改。【内置功能都是直接操作列表内部，不会创建新的一份数据】

- 列表添加元素

  ```python
  l = ['Python', 'C++', 'Java']
  # 1. 追加 在原列表中尾部追加值。
  l.append('PHP')
  
  # 追加列表，整个列表也被当成一个元素
  l.append(['Ruby', 'SQL'])
  print(l)
  
  # 2. 批量追加，将一个列表中的元素逐一添加另外一个列表。
  l.append(['Ruby', 'SQL'])
  print(l)
  
  # 3. 插入，在原列表的指定索引位置插入值
  l = ['Python', 'C++', 'Java']
  #插入元素
  l.insert(1, 'C')
  print(l)
  ```

- 列表删除元素

  ```python
  # 1. remove()：根据元素值进行删除
  nums = [40, 36, 89, 2, 36, 100, 7]
  nums.remove(36)  # 删除36
  
  # 2. pop()：根据索引值删除元素
  nums = [40, 36, 89, 2, 36, 100, 7]
  nums.pop(3)  # [40, 36, 89, 36, 100, 7]
  # 3. clear()：删除列表所有元素
  
  nums = [40, 36, 89, 2, 36, 100, 7]
  nums.clear()
  ```

- 列表查找元素

  ```python
  # index 根据值获取索引（从左到右找到第一个删除）
  nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
  #检索列表中的所有元素
  print( nums.index(2) )
  # 检索3~7之间的元素
  print( nums.index(100, 3, 7) )
  # 检索4之后的元素
  print( nums.index(7, 4) )
  ```

### 2.2 通用操作

- 相加，两个列表相加获取生成一个新的列表。
- 相乘，列表*整型 将列表中的元素再创建N份并生成一个新的列表。
- 运算符in包含
- 获取长度
- 索引
- 切片
- for循环

## 3. <font color='orange'>元组</font>

元组（tuple），是一个有序且不可变的容器，在里面可以存放多个不同类型的元素。

```python
# 使用 ( ) 直接创建
当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号,
```

> 能被for循环的遍历的数据类型都可以传给tuple()转换成元组类型

### 3.1 通用操作

1. 相加
2. 相乘
3. 获取长度
4. 索引
5. 切片
6. 步长
7. for循环

## 4. <font color='orange'>字典</font>

字典是 **无序**、**键不重复**且元素只能是**键值对**的**可变的**容器。

```python
data = { "k1":1,  "k2":2 }
```

- 键必须为不可变数据类型、必须唯一
- 键不重复，重复则会被覆盖
- 可存放任意多个value、可修改、可以不唯一
- 无序
- 查询速度快，且不受dict的大小影响

### 4.1 字典的内置功能

- 获取值

  ```python
  data = { "k1":1,  "k2":2 }
  result = data.get("k1")
  print(result)
  ```

- 获取所有的键

  ```python
  data = { "k1":1,  "k2":2 }
  result = data.keys()
  print(result)
  ```

- 获取所有的值

  ```python
  data = { "k1":1,  "k2":2 }
  result = data.values()
  print(result)
  ```

- 获取所有的键值

  ```python
  data = { "k1":1,  "k2":2 }
  result = data.items()
  print(result)
  ```

- 设置值

  ```python
  # key不存在则新增键值对，并将新增的value返回
  data = {
      "email": 'xxx@live.com',
  }
  data.setdefault("age", 18)
  print(data)
  ```

- 更新字典键值对

  ```python
  # 用新字典更新旧字典，有则修改，无则添加
  info = {"age":12, "status":True}
  info.update({"age":14,"name":"哈哈哈"})
  print(info) 
  ```

- 移除指定键值对

  ```python
  info = {"age":12, "status":True}
  data = info.pop("age")
  print(info)
  ```

### 4.2 通用操作

1. 长度
2. 是否包含
3. 索引
4. 根据键 修改值 和 添加值 和 删除键值对
5. for循环

## 5.<font color='orange'> 集合</font>

由一系列不重复的不可变类型(元组/数/字符串)组成的可变散列容器。

```python
v1 = { 11, 22, 33}
```

> 能被for循环的遍历的数据类型（强调：遍历出的每一个值都必须为不可变类型）都可以传给set()转换成集合类型

- 无序，无法通过索引取值。
- 可变，可以添加和删除元素。

### 5.1 集合的内置方法

- set 集合中添加元素

  ```python
  a = {1,2,3}
  a.add((1,2))
  print(a)
  ```

- 删除元素

  ```python
  a = {1,2,3}
  a.discard(3)
  ```

- 用集合主要来干2件事，**去重和关系运算**

  ```python
  # 1.交集&：返回共同元素。
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s3 = s1 & s2  # {2, 3}
  
  # 2.并集：返回不重复元素
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s3 = s1 | s2  # {1, 2, 3, 4}
  
  # 3. 差集(-)：
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1 - s2  # {1} 属于s1但不属于s2
  
  # 4. 对称差集(^)
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s3 = s1 ^ s2  
  ```

