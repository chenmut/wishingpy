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

