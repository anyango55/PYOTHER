Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [25,12,636,95,14]
>>> nums
[25, 12, 636, 95, 14]
>>> nums[0]
25
>>> nums[4]
14
>>> nums[2:]
[636, 95, 14]
>>> nums[-1]
14
>>> names = ['navin','kiran','john']
>>> names
['navin', 'kiran', 'john']
>>> values = [9.5.'Navin',25]
SyntaxError: invalid syntax
>>> values = [9.5.'Navin',25]
SyntaxError: invalid syntax
>>> values = [9.5,'Navin',25]
>>> mil = [nums,names]
>>> mil
[[25, 12, 636, 95, 14], ['navin', 'kiran', 'john']]
>>> nums.append(45)
>>> nums
[25, 12, 636, 95, 14, 45]
>>> nums.insert(2,77)
>>> nus.remove(14)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    nus.remove(14)
NameError: name 'nus' is not defined
>>> nums.remove(14)
>>> nums
[25, 12, 77, 636, 95, 45]
>>> nums.pop(1)
12
>>> nums.pop()
45
>>> 
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> 
