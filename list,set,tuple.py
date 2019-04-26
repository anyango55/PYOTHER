Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = (21,3,14,25)
>>> tup
(21, 3, 14, 25)
>>> tup[1]
3
>>> tup[1] = 33
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1] = 33
TypeError: 'tuple' object does not support item assignment
>>> tup.count
<built-in method count of tuple object at 0x01C742A0>
>>> s = {22,25,14,21,5}
>>> s
{5, 14, 21, 22, 25}
>>> s = {25,14,98,63,75,98}
>>> s
{98, 75, 14, 25, 63}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[2]
TypeError: 'set' object does not support indexing
>>> 
