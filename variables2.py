Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 5
>>> id(num)
1711855856
>>> name = 'navin'
>>> id(name)
30895648
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
1711855936
>>> id(b)
1711855936
>>> id(10)
1711855936
>>> k = 10
>>> id(k)
1711855936
>>> a =9
>>> id(a)
1711855920
>>> id(b)
1711855936
>>> k=a
>>> id(k)
1711855920
>>> b=8
>>> id(b)
1711855904
>>> name='joe'
>>> id(name)
30958848
>>> PI = 3.14
>>> PI
3.14
>>> PI = 3.15
>>> type(PI)
<class 'float'>
>>> 
