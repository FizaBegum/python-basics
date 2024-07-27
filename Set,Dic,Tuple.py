Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1={11,12,13,14}
>>> num1.add(15)
>>> print(num1)
{11, 12, 13, 14, 15}
>>> num2={16,17,18,19,20}
>>> z=num1.difference(num2)
>>> print(z)
{11, 12, 13, 14, 15}
>>> z=num1.intersection(num2)
>>> print(z)
set()
>>> z=num1.union(num2)
>>> print(z)
{11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
>>> z=num1.copy()
>>> print(z)
{11, 12, 13, 14, 15}
>>> num2.clear()
>>> print(num2)
set()
>>> print(num1)
{11, 12, 13, 14, 15}
>>> num1.remove(11)
>>> print(num1)
{12, 13, 14, 15}
>>> num1.pop()
12
>>> print(num1)
{13, 14, 15}
>>> num1.pop(2)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    num1.pop(2)
TypeError: set.pop() takes no arguments (1 given)
>>> car={"num1":11,"num2":12,"num3":13}
>>> x=car.get("num2")
>>> print(x)
12
>>> x=car.items()
>>> print(x)
dict_items([('num1', 11), ('num2', 12), ('num3', 13)])
>>> x=cae.keys()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x=cae.keys()
NameError: name 'cae' is not defined. Did you mean: 'car'?
x=car.keys()
print(x)
dict_keys(['num1', 'num2', 'num3'])
x=car.values()
print(x)
dict_values([11, 12, 13])
car.update({"num4:"14})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
car.update({"num4":14})
print(car)
{'num1': 11, 'num2': 12, 'num3': 13, 'num4': 14}
car.popitem()
('num4', 14)
print(car)
{'num1': 11, 'num2': 12, 'num3': 13}
x=car.copy()
print(x)
{'num1': 11, 'num2': 12, 'num3': 13}
car.clear()
print(car)
{}
a=(1,3,5,7,9,7,6,5,4,2,3,4,3)
x=z.count(5)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x=z.count(5)
AttributeError: 'set' object has no attribute 'count'
x=a.count(5)
print(x)
2
x=a.count(3)
print(x)
3
x=a.index(2)
print(x)
9
x=a.index(5)
print(x)
2

