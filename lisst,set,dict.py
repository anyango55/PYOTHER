Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 2.5
>>> type(num)
<class 'float'>
>>> num = 5
>>> type(num)
<class 'int'>
>>> num = 6+9j
>>> type(num)
<class 'complex'>
>>> a = 5.6
>>> b  = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k = float(b)
>>> k
5.0
>>> k = 6
>>> c = complex(b,k)
>>> c
(5+6j)
>>> b < k
True
>>> bool = b < k
>>> type(bool)
<class 'bool'>
>>> b>k
False
>>> int(True)
1
>>> int(False)
0
>>> list = [25,36,45,12]
>>> type(list)
<class 'list'>
>>> s = {25,36,45,15,12,25}
>>> s
{36, 12, 45, 15, 25}
>>> type(s)
<class 'set'>
>>> t = (25,36,4,57,12)
>>> type(t)
<class 'tuple'>
>>> range(10)
range(0, 10)
>>> list(range(10))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
>>> range(10)
range(0, 10)
>>> list(range(10))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
>>> range(15)
range(0, 15)
>>> 
>>> list(range(15))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list(range(15))
TypeError: 'list' object is not callable
>>> 
>>> list(2,10,2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list(2,10,2)
TypeError: 'list' object is not callable
>>> list(range(2,10,2))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list(range(2,10,2))
TypeError: 'list' object is not callable
>>> 
>>> 
>>> d = {'navin':'samsung','rahul':'iphone','kiran':'oneplus'}
>>> d
{'navin': 'samsung', 'rahul': 'iphone', 'kiran': 'oneplus'}
>>> d.keys()
dict_keys(['navin', 'rahul', 'kiran'])
>>> d.values
<built-in method values of dict object at 0x019783F0>
>>> d.value()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d.value()
AttributeError: 'dict' object has no attribute 'value'
>>> d.values()
dict_values(['samsung', 'iphone', 'oneplus'])
>>> d['rahul']
'iphone'
>>> d.get('kiran')
'oneplus'
>>> 
