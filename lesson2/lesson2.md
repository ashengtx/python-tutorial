## Python 基础补充介绍

### Basic Operators

运算符类型；

- Arithmetic Operators
- Comparison (Relational) Operators
- Assignment Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators

#### Arithmetic Operators 算术运算符

```
+ - * / % ** //
```

#### Comparison (Relational) Operators 比较运算符

a = 20, b = 30

| operator   | example   |
|---|---|
|>  |  (a > b) is False  |
|>= |  (a >= b) is False |
|<  |  (a < b) is True   |
|<= |  (a <= b) is True  |
|== |  (a == b) is False |
|!= |  (a != b) is True  |
|<> |  (a <> b) is True  |

两个等号是判断是否相等，一个等号是赋值

#### Assignment Operators 赋值运算符

| operator   | example   |
|---|---|
|=  |  c = a + b  |
|+= |  c += a -> c = c + a |
|-=  |     |
|*= |    |
|/= |   |
|%= |    |
|**= |  ```c **= a -> c = c ** a```  |
|//= |    |

#### Logical Operators 逻辑运算符

a = True
b = False

| operator   | example   |
|---|---|
| && / and  |  a && b / a and b (False)  |
| ```||``` / or  |  ```a || b / a or b (True)``` |
| not  | not a (False), not b (True)    |

#### Bitwise Operators 位运算符

a = 1111
b = 1010

| operator   | example   |
|---|---|
| & Binary AND  | a & b (1010)   |
| ```|``` Binary OR  |  ```a | b (1111)``` |
| ^ Binary XOR  | a ^ b (0101)    |
| ~ Binary ones complement \\ 按位取反 | ~b (0101)   |
| << Binary left shift  | a << 2 (11 1100)  |
| >> Binary right shift | a >> 2 (11.11)  |

#### Membership Operators 隶属运算符

a = 1
b = [1,2,3,4]

| operator   | example   |
|---|---|
| in  | a in b (True)  |
| not in  |  a not in b (False) |

#### Identity Operators 恒等运算符

a = True

| operator   | example   |
|---|---|
| is  | type(a) is bool (True)  |
| is not  | type(a) is bool (False)  |

[more details](https://www.tutorialspoint.com/python/python_basic_operators.htm)

### String Formatting


```python
name = 'James'
age = 33
print("%s is %d years old." % (name, age))
```

%s 字符串  
%d 整型  
%f 浮点数

![conversion](./img/string-formatting.png)

[more details](https://docs.python.org/2.4/lib/typesseq-strings.html)

### Namespaces and Scoping 命名空间和作用域

Variables are names (identifiers) that map to objects.
变量是名字到对象的映射。

A namespace is a dictionary of variable names (keys) and their corresponding objects (values).
命名空间可以理解为名字和对应对象的目录。

local namespace & global namespace

每个函数有自己的局部命名空间，在函数内使用全局变量要加global标志。
如果同名，局部命名空间的变量会覆盖全局命名空间的变量。

```python
Money = 2000 # 全局
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   Money = Money + 1 

print(Money) # 覆盖前
AddMoney()
print(Money) # 覆盖后

```


## Classes & Objects

**面向对象编程（Object-Oriented Programming, OOP）**


```python
class Employee:
    """所有employee的基类"""

    empCount = 0 # 类变量(Class variable)，被所有实例共享，可以从类的内部和外部通过Employee.empCount访问，不如实例变量常用

    """
    类内部定义的函数叫做类的方法（Method）
    """
    def __init__(self, name, salary):
        """
        实例化一个类的时候会被调用的初始化方法
        """
        self.name = name # 实例变量（Instance vairable），定义在方法内，只属于这个实例
        self.salary = salary
        Employee.empCount += 1
   
    # 定义类方法的时候，注意第一个参数都是self，调用的时候不需要
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)


# 类的实例化(Instantiation)，实例叫做这个类的对象
# This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

# 对象属性用点操作符访问'.'
emp1.displayEmployee()
emp2.displayEmployee()
# 类变量的访问
print("Total Employee %d" % Employee.empCount)

# 对象属性可以随时添加，删除，修改
emp1.age = 27  # Add an 'age' attribute.
emp1.age = 28  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.
```

## Modules

使用模块可以从其他python文件导入定义好的类或者函数

两种导入方法
```python
import module_name # 这种方法通过module_name.method的方式访问模块里的方法或者类
from module_name import function
from module_name import *

```

- 例子1-自建模块

```python
from employee import Employee

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
```

- 例子2-内置模块

```python
import math

print(math.sqrt(9)) #3.0
```

### dir()

输出模块内定义的变量与函数

```python
import math
print(dir(math))

help(math.pow)
```
output：
```
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 
'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 
'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 
'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 
'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 
'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 
'tanh', 'trunc']

pow(...)
    pow(x, y)
    
    Return x**y (x to the power of y).
```

其中，```__name__```是模块名，在当前文件下```__name__ == 'main'```

- 在use_module文件对比import employee 与 employee2

### random 模块介绍

```py
import random

print(dir(random))

#random.seed(2) # 传入种子，初始化随机数生成器

# random 返回下一个[0.0, 1.0)之间的随机数
print(random.random())

# randint(a, b), 返回一个整数N, a <= N <= b
for i in range(10):
    print("randint: ", random.randint(0,10))

# uniform(a, b), 返回一个实数m, a <= m <= b
for i in range(10):
    print("rand float: ", random.uniform(0,10))

# sample(population, k) 不放回的随机抽样
print("sample without replacement:", random.sample(range(1000), k=10))

# choice(seq) 从一个非空序列中随机取出一个元素
print("random choice: ", random.choice(range(1000)))

# choices(population, weights=None, cum_weights=None, k) 有放回抽样
print("sample with replacement:", random.sample(range(10), k=10))

# shuffle(seq) 打乱顺序
alist = list(range(10))
print(alist)
random.shuffle(alist)
print("after shuffling:", alist)
```

## Files I/O

### stdin/stdout 标准输入输出

**print()**

最简单的输出，```print(expression1, expression2, ...)```，
将几个逗号隔开的表达式以字符的形式输出到 **标准输出**，即屏幕。

**input()**

```py
import random
name = input("Hello, may I know your name?:")
reply = ["Wow, %s, such a beautiful name!", "It's so lovely!"]
print(random.choice(reply), name)
```

### Opening and Closing Files

```py
file = open(file_name, access_mode)

do something

file.close()
```

更好的打开文件方式，用with语句，会自动关闭文件

```py
with open(file_name, access_mode) as file:
    do something
```

| mode   | description   |
|---|---|
|r  |  只读，默认模式  |
|rb |  二进制读 |
|r+ |  读+写   |
|rb+ | 读+写 均为二进制  |
|w  |  只写，会重写该文件，文件不存在则自动创建一个 |
|wb |  二进制写，会重写该文件，文件不存在则自动创建一个  |
|w+ |  读+写，会重写该文件，文件不存在则自动创建一个  |
|wb+ | 二进制读和写，会重写该文件，文件不存在则自动创建一个  |
|a  |  在文件末尾追加写，文件不存在则自动创建一个 |
|ab  | ... |
|a+  |  ... |
|ab+  |  ... |

r(read),w(write),a(append),b(binary)

[more details](https://www.tutorialspoint.com/python/python_files_io.htm)

**file object**

| Attribute   | Description   |
|---|---|
|file.closed  |  返回True如果文件已经关闭，否则False  |
|file.mode |  返回访问模式 |
|file.name |  返回文件名 |

```py
with open("../txt/apple.txt", 'r') as f:
    print("file name: ", f.name)
    print("access mode: ", f.mode)
    print("closed or not:", f.closed)
```

### Reading and Writing Files

**file.write()**
**file.read()**
**file.tell()**
**file.seek()**

```py
with open("../txt/output.txt", "r+") as fo:
    str = fo.read(10);
    print("Read String is : ", str)

    # Check current position
    position = fo.tell();
    print("Current file position : ", position)

    # Reposition pointer at the beginning once again
    #fo.seek(offset, from); from = 0表示定位到文件开头，1表示当前位置，2表示文件末尾
    position = fo.seek(10, 0);
    #position = fo.seek(0, 1);
    #position = fo.seek(0, 2);
    str = fo.read(10);
    print("Again read String is : ", str)

```

```py
with open("../txt/apple.txt", 'r') as f:
    chars = []
    for line in f:
        if len(line) > 1:
            chars.append(line.strip()) # str.strip() 去掉首尾空白
        else:
            chars.append(' ')
    print(chars)
    print(''.join(chars)) # 'delimit'.join(alist)
    with open("../txt/output.txt", 'w') as fout:
        #fout.write(''.join(chars)) # 末尾不加换行
        print(''.join(chars), file=fout) # 末尾会加换行
```

### Renaming and Deleting Files

```py
import os

filename = "../txt/testrename.txt"

if not os.path.exists(filename):
    open(filename, 'w')

# 下面这两行一行一行来执行

#os.rename(filename, "../txt/testrename1.txt")
#os.remove("../txt/testrename1.txt")
```

### Directories in Python

```py
import os
import time

# Create a directory "test"
if not os.path.isdir("test"):
    os.mkdir("test")

time.sleep(5)

# remove directory
os.rmdir("test")
```

## 应用：使用python训练词向量Word2Vec

[train word2vec tutorial](https://ashengtx.github.io/2017/10/18/word2vec/)

### python库的安装

windows 下管理员模式打开cmd

列出已经安装的库
```
> pip list
```

安装jiaba分词
```
> pip install jieba
```
