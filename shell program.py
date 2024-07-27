Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello World")
Hello World

num1=5
print(num1)
5
num2=5.5
print(num2)
5.5
a=int(input())
5
b=int(input())
print(b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b=int(input())
ValueError: invalid literal for int() with base 10: 'print(b)'
b=float(input())
5.5
print(b)
5.5
name="Fiza"
print(name)
Fiza
a=str(input())
print 
a=str(input())
fiza
print(a)
fiza
x=5
y=10
print(bool(x==y))
False
a=[1,3,5,7,9]
a.append(2)
print(a)
[1, 3, 5, 7, 9, 2]
a.sort()
print(a)
[1, 2, 3, 5, 7, 9]
a.reverse()
print(a)
[9, 7, 5, 3, 2, 1]
a.reverse()
print(a)
[1, 2, 3, 5, 7, 9]
a.count()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
a.count(2)
1
a.index(3)
2
>>> a.clear()
>>> print(a)
[]
>>> b=[2,4,6,8,10]
>>> a.copy(b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.copy(b)
TypeError: list.copy() takes no arguments (1 given)
>>> a=b.copy()
>>> print(a)
[2, 4, 6, 8, 10]
>>> a.extend(b)
>>> print(a)
[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]
>>> a.pop(2)
6
>>> b.pop(3)
8
>>> print(a)
[2, 4, 8, 10, 2, 4, 6, 8, 10]
>>> print(b)
[2, 4, 6, 10]
>>> a.insert(4,2)
>>> print(a)
[2, 4, 8, 10, 2, 2, 4, 6, 8, 10]
>>> len(a)
10
>>> a={1,,3,5,7}
SyntaxError: invalid syntax
>>> a={1,3,5,7}
>>> b={2,4,6,8}
>>> c=a.union(b)
>>> print(c)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> c=a.intersection(b)
>>> print(c)
set()
>>> c=a.difference(b)
>>> print(c)
{1, 3, 5, 7}

