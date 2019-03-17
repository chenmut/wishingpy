#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print("hello, world")
# print('The quick brown fox', 'jumps over', 'the lazy dog')
# print('100 + 200')

# name = input()
# print(name)

# name = input('please enter your name: ')
# print('hello,', name)

# print('1024 * 768 =', 1024 * 768)

# ------python 基础
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

## 数据类型和变量
print('I\'m  ok.')
print("I\'m learning\nPython")
print(r'\\\t\\')
print('''line1 \n line2 \n line3''')
print(r'''hello, \n
    world''')
True 
False
3 > 2
not 1 > 2
None
a = 'ABC'
b = a
a = 'XYZ'
print(b)
10 / 3 
9 / 3 
11 // 3 
13 % 4

## 字符串和编码
print('包含中文的str')
ord("A")
ord("中")
ord("国")
chr(25991)
"abc".encode('ascii')
'中文'.encode('utf-8')
b'ABC'.decode('ascii')
'Hello, %s' % 'world'
print('%2d-%02d' % (300.000, 100.00))
print('%.2f' % 3.1415926)
'growth rate: %d%%' % 7

## list

## 条件判断

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

## 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

list(range(5))

sum = 0
for x in range(101):
    sum = sum + x 
print(sum)
    
## 使用dict和set
d = {'Michael':95, 'Bob':75, 'Tracy':85}
d["Michael"]

## set是一个无序不重复元素集
s = set([1, 2, 3, 4])
s = set([1, 2, 3, 4, (1, 2, 3)])
s

d = {(1, ):10}
print(d)

print(str(hex(110)) + '\n' + str(hex(120)))

## 定义函数
def my_abs( x ):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

from abstest import my_abs
print(my_abs(-110))

def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type~')
    if x >= 0:
        pass
    else:
        return
print(my_abs2('a'))

## 位置函数
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1 
        s = s * x
    return s

print(power(5, 9))

# func(*args, **kw)

## 切片
L = list(range(100))
L[:10]
L[-10:]
L[10:20]
L[:10:2]
L[::5]

(0, 1, 2, 3, 4, 5)[:3]

'ABCDEFG'[::2]

# from collections import Iterable
# isinstance('abc', Iterable)
# isinstance([1, 2, 3], Iterable)
# isinstance(123, Iterable)


for i, value in enumerate(['A', 'B', 'C', 'D']):
    print(i, value)

## 列表生成式
list(range(1, 11))

L = []
for x in range(1, 11):
    L.append(x * x)

[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]

import os
[d for d in os.listdir('.')]

g = (x * x for x in range(10))
g
next(g)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
f

for n in fib(6):
    print(n)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

## 函数式编程（build-in)，变量
abs 
## map/reduce
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 9])

sorted([36, 5, -12, 9, -21])

## 模块
# mycompany
# ├─ __init__.py
# ├─ abc.py
# └─ xyz.py

# mycompany.abc  mycompany.xyz

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

# 面向对象编程
+ 类：class 
+ 示例：instance

class Student(object):
    pass

tcl = Student()
tcl
Student
tcl.name = 'tian chenmu'
tcl.name

class Student2(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

tcl = Student2('tian chenmu', 70)
tcl.name 
tcl.score

## 2个下划线__代表私有变量（private）

# 文件操作
##操作文件和目录 
import os 
os.name
os.uname()
os.environ
os.environ.get('key')
os.environ.get('PATH')

# 进程、线程
## 多进程
import os 
print('Process (%s) start...' % os.getpid())

