# python学习（1.18）

## <font color='red'>条件控制</font>

以下实例演示了狗的年龄计算判断：

```python
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
 
### 退出提示
input("点击 enter 键退出")
```

输出：

```python
请输入你家狗狗的年龄: 1

相当于 14 岁的人。
点击 enter 键退出
```

##### <font color='orange'> 嵌套</font>

在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。

```python
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
```

```python
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")
输出：
输入一个数字：6
你输入的数字可以整除 2 和 3
```

#### <font color='orange'>match...case</font>

Python 3.10 增加了 **match...case** 的条件判断，不需要再使用一连串的 **if-else** 来判断了。

match 后的对象会依次与 case 后的内容进行匹配，如果匹配成功，则执行匹配到的表达式，否则直接跳过，**_** 可以匹配一切。

语法格式如下：

```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```

**case _:** 类似于 C  中的 **default:**，当其他 case 都无法匹配时，匹配这条，保证永远会匹配成功。

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))
```



## <font color='red'>循环控制</font>

同样需要注意冒号和缩进。另外，<font color='green'>**<u>在 Python 中没有 do..while 循环</u>**。</font>

以下实例使用了 while 来计算 1 到 100 的总和：

```python
#!/usr/bin/env python3
 
n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))
```

执行结果如下：

```
1 到 100 之和为: 5050
```

### while 循环使用 else 语句

如果 while 后面的条件语句为 false 时，则执行 else 的语句块。

语法格式如下：

```
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

expr 条件语句为 true 则执行 statement(s) 语句块，如果为 false，则执行 additional_statement(s)。

```python
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```

执行以上脚本，输出结果如下：

```
0  小于 5
1  小于 5
2  小于 5
3  小于 5
4  小于 5
5  大于或等于 5
```

### 简单语句组

类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与 while 写在同一行中， 如下所示：

```    
flag = 1
 
while (flag): print ('欢迎访问菜鸟教程!')
 
print ("Good bye!")
```

**注意：**以上的无限循环你可以使用 CTRL+C 来中断循环。

执行以上脚本，输出结果如下：

```
欢迎访问菜鸟教程!
欢迎访问菜鸟教程!
欢迎访问菜鸟教程!
欢迎访问菜鸟教程!
欢迎访问菜鸟教程!
……
```

### for 语句

Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

for循环的一般格式如下：

```   
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：

```python
#!/usr/bin/python3
 
sites = ["Baidu", "Google","Nowcoder","Taobao"]
for site in sites:
    if site == "Nowcoder":
        print("牛客教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```

执行脚本后，在循环到 "Nowcoder"时会跳出循环体：

```python
循环数据 Baidu
循环数据 Google
牛客教程!
完成循环!
```

### range()函数

如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:

```python
>>>for i in range(5):
...     print(i)
...
0
1
2
3
4
```

你也可以使用range指定区间的值：

```python
>>>for i in range(5,9) :
    print(i)
 
 
5
6
7
8
```

也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):

```
>>>for i in range(0, 10, 3) :
    print(i)
 
 
0
3
6
9
```

负数：

```
>>>for i in range(-10, -100, -30) :
    print(i)
 
 
-10
-40
-70
```

您可以结合range()和len()函数以遍历一个序列的索引,如下所示:

```
>>>a = ['Google', 'Baidu', 'Nowcoder', 'Taobao', 'QQ']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Google
1 Baidu
2 Nowcoder
3 Taobao
4 QQ>>>a = [``'Google'``, ``'Baidu'``, ``'Nowcoder'``, ``'Taobao'``, ``'QQ'``]``>>> ``for` `i in range(len(a)):``...   print(i, a[i])``...``0` `Google``1` `Baidu``2` `Nowcoder``3` `Taobao``4` `QQ
```

还可以使用range()函数来创建一个列表：

```
>>>list(range(5))
[0, 1, 2, 3, 4]
>>>
```

### pass 语句

Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句，如下实例

```
>>>while True:
...     pass  # 等待键盘中断 (Ctrl+C)
```

最小的类:

```

1
2
>>>class MyEmptyClass:
...     pass
```

以下实例在字母为 o 时 执行 pass 语句块:

```
#!/usr/bin/python3
 
for letter in 'Nowcoder':
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
```

执行以上脚本输出结果为：

```
当前字母 : N
执行 pass 块
当前字母 : o
当前字母 : w
当前字母 : c
执行 pass 块
当前字母 : o
当前字母 : d
当前字母 : e
当前字母 : r
Good bye!
```

## <font color='red'>推导式</font>

Python推导式（Comprehensions）是Python语言中一个强大的特性，它可以快速、简洁地创建一个新的数据结构。它的语法非常简单，可以轻松地在一行代码中完成许多常见的操作，如过滤、映射、计算等。

Python推导式的语法如下：

```text
[expression for item in iterable if condition]
```

其中，expression 是每个元素应用的表达式，item 是可迭代对象中的每个元素，condition 是可选的筛选条件

Python推导式分为三种类型：列表推导式（List Comprehensions）、字典推导式（Dictionary Comprehensions）和集合推导式（Set Comprehensions）。

### 列表推导式

列表推导式是Python中最常见和最常用的推导式类型。它可以快速地生成一个新的列表，该列表根据原始列表或其他可迭代对象中的元素和指定的表达式生成。

案例

```python
list_derivation = [i for i in range(1, 20) if i % 2 == 0]
print("列表推导式", list_derivation)

list_tuple = [(i, j) for i in range(1, 3) for j in range(2)]

print("返回元组", list_tuple)
```

结果

```text
列表推导式 [2, 4, 6, 8, 10, 12, 14, 16, 18]
返回元组 [(1, 0), (1, 1), (2, 0), (2, 1)]
```

### 字典推导式

字典推导式与列表推导式类似，它也可以从原始字典或其他可迭代对象中生成一个新的字典。它的语法如下：

```text
{key_expression: value_expression for item in iterable if condition}
```

其中，key_expression 和 value_expression 是每个键值对的表达式，item 是可迭代对象中的每个元素，condition 是可选的筛选条件。

案例

```python
original_dict = {'a': 1, 'b': 2, 'c': 3}
doubled_dict = {key: value * 2 for key, value in original_dict.items()}#original_dict 是一个已经存在的字典。.items() 是一个方法，它返回字典中每一对键和值的元组。
print("字典推导式", doubled_dict)

dict_derivation = {x: x ** 2 for x in range(1, 11)}
print("开平方", dict_derivation)
```

结果

```text
字典推导式 {'a': 2, 'b': 4, 'c': 6}
开平方 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

### 集合推导式

集合推导式与列表推导式和字典推导式类似，但它生成一个新的集合。它的语法如下：

```text
{expression for item in iterable if condition}
```

其中，expression 是集合中每个元素应用的表达式，item 是可迭代对象中的每个元素，condition 是可选的筛选条件。

案例

```python
set_derivation = {i for i in range(1, 20)}#这是一个集合推导式（set comprehension），用于创建一个集合。
print(type(set_derivation))#这行代码打印set_derivation的类型。
#type()是一个内置函数，它返回传入对象的类型。
print("集合推导式", set_derivation)
```

结果

```text
<class 'set'>
集合推导式 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
```

## <font color='red'>错误和异常捕获</font>

Python 有两种错误很容易辨认：语法错误和异常。

## 语法错误

Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例

```python
>>>while True print('Hello world')
  File "<stdin>", line 1, in ?
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

这个例子中，函数 print() 被检查到有错误，是它前面缺少了一个冒号（:）。

语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。

## 异常

即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。

大多数的异常都不会被程序处理，都以错误信息的形式展现在这里:

```python
>>>10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: Can't convert 'int' object to str implicitly
```

异常以不同的类型出现，这些类型都作为信息的一部分打印出来: 例子中的类型有 ZeroDivisionError，NameError 和 TypeError。

错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息。

## 异常处理

以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。用户中断的信息会引发一个 KeyboardInterrupt 异常。

```python
>>>while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")
```

try语句按照如下方式工作；

- 首先，执行try子句（在关键字try和关键字except之间的语句）
- 如果没有异常发生，忽略except子句，try子句执行后结束。
- 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
- 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。

处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:

```python
except (RuntimeError, TypeError, NameError):
        pass
```

最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
```

try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。例如:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常。

异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。例如:

```python
>>>def this_fails():
        x = 1/0

>>> try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)

Handling run-time error: int division or modulo by zero
```

## 抛出异常

Python 使用 raise 语句抛出一个指定的异常。例如:

```python
>>>raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: HiThere
```

raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。

```python
>>>try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise

An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in ?
NameError: HiThere
```

## 用户自定义异常

你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:

```python
>>>class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

>>> try:
        raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)

My exception occurred, value: 4
>>> raise MyError('oops!')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
__main__.MyError: 'oops!'
```

在这个例子中，类 Exception 默认的 **init**() 被覆盖。

当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:

```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```

大多数的异常的名字都以"Error"结尾，就跟标准的异常命名一样。

## 定义清理行为

try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。 例如:

```python
>>>try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
... 
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

以上例子不管 try 子句里面有没有发生异常，finally 子句都会执行。

如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出。

下面是一个更加复杂的例子（在同一个 try 语句里包含 except 和 finally 子句）:

```python
>>>def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("division by zero!")
        else:
            print("result is", result)
        finally:
            print("executing finally clause")

>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

## 预定义的清理行为

一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。这面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:

```python
for line in open("myfile.txt"):
    print(line, end="")
```

以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。

关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。

## <font color='red'>map，lambda，filter函数的使用</font>

### map函数

`map()` 函数是 Python 内置的高阶函数之一，它接收一个函数和一个可迭代对象（如列表、元组等）作为参数，然后使用这个函数对可迭代对象的每一个元素进行处理，并返回一个新的可迭代对象。

这里有一个简单的例子来说明 `map()` 函数的工作原理。

假设我们有一个列表，包含一些数字，我们想要将这些数字都转换成它们的平方。我们可以定义一个函数来计算平方，然后使用 `map()` 函数将这个函数应用到列表的每一个元素上。

```python
# 定义一个计算平方的函数  
def square(n):  
    return n ** 2  
  
# 创建一个包含数字的列表  
numbers = [1, 2, 3, 4, 5]  
  
# 使用 map() 函数将 square 函数应用到 numbers 列表的每一个元素上  
squared_numbers = map(square, numbers)  
  
# map() 函数返回的是一个迭代器，所以我们可以使用 list() 函数将其转换为列表  
squared_numbers = list(squared_numbers)  
  
# 输出结果  
print(squared_numbers)  # 输出: [1, 4, 9, 16, 25]
```

在这个例子中，`map()` 函数接收了 `square` 函数和 `numbers` 列表作为参数，并返回了一个新的迭代器，其中包含了 `numbers` 列表中每个元素的平方。然后，我们使用 `list()` 函数将这个迭代器转换为一个列表，并打印出来。

另外，从 Python 3 开始，`map()` 函数返回的是一个迭代器，而不是一个列表。这意味着你可以在需要时才计算结果，这对于处理大数据集时非常有用，因为它可以节省内存。但是，如果你想要一次性获取所有的结果，你可以使用 `list()` 函数将迭代器转换为列表。

### lambda函数

`lambda` 函数是 Python 中的一种简洁的、定义匿名函数（即没有名字的函数）的方式。`lambda` 函数通常用于需要一个简单函数作为参数的地方，例如在 `map()`、`filter()`、`reduce()` 等高阶函数中。`lambda` 函数的语法非常简洁，它允许你快速定义简单的函数而不必使用 `def` 关键字来定义一个完整的函数。

下面是一个使用 `lambda` 函数的例子，这个例子中，我们定义了一个简单的 `lambda` 函数来计算两个数的和，并使用 `map()` 函数将这个 `lambda` 函数应用到两个列表的元素上，以计算对应元素的和。

```python
# 定义两个列表  
list1 = [1, 2, 3, 4, 5]  
list2 = [10, 20, 30, 40, 50]  
  
# 使用 lambda 函数和 map() 函数计算两个列表中对应元素的和  
sums = map(lambda x, y: x + y, list1, list2)  
  
# 将 map 对象转换为列表  
sums_list = list(sums)  
  
# 输出结果  
print(sums_list)  # 输出: [11, 22, 33, 44, 55]
```

在这个例子中，`lambda x, y: x + y` 定义了一个匿名函数，它接收两个参数 `x` 和 `y`，并返回它们的和。然后，`map()` 函数将这个 `lambda` 函数应用到 `list1` 和 `list2` 的对应元素上，生成一个新的迭代器，其中包含了每个对应元素的和。最后，我们使用 `list()` 函数将这个迭代器转换为一个列表，并打印出来。

`lambda` 函数非常适合用于简单的、一次性的操作，它们不需要在代码中重复使用，因此不需要给它们取一个正式的名字。

### filter函数

`filter()` 函数是 Python 的另一个内置高阶函数，用于过滤可迭代对象中的元素，返回由符合指定条件的元素组成的新可迭代对象。`filter()` 函数接收两个参数：第一个参数是一个函数，这个函数用于测试可迭代对象中的每个元素是否满足某个条件；第二个参数是要过滤的可迭代对象。

下面是一个使用 `filter()` 函数的例子，我们将定义一个函数来检查一个数是否是偶数，然后使用 `filter()` 函数来过滤一个数字列表，只保留偶数。

```python
# 定义一个检查是否为偶数的函数  
def is_even(n):  
    return n % 2 == 0  
  
# 创建一个包含数字的列表  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
  
# 使用 filter() 函数过滤出偶数  
even_numbers = filter(is_even, numbers)  
  
# filter() 函数返回的是一个迭代器，因此我们可以将其转换为列表来查看结果  
even_numbers = list(even_numbers)  
  
# 输出结果  
print(even_numbers)  # 输出: [2, 4, 6, 8, 10]
```

在这个例子中，`is_even` 函数检查一个数字是否是偶数。然后，`filter()` 函数使用这个函数来测试 `numbers` 列表中的每个元素，并返回一个新的迭代器，其中只包含满足条件的元素（即偶数）。最后，我们使用 `list()` 函数将迭代器转换为列表，并打印出结果。

`filter()` 函数在处理大数据集时非常有用，因为它可以按需生成结果，而不是一次性生成所有结果，从而节省内存。此外，它还可以与其他高阶函数（如 `map()` 和 `reduce()`）结合使用，以创建更复杂的数据处理管道。

