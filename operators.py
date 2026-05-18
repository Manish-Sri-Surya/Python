Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3]
>>> b =[1,2,3]
>>> print(a is b)
False
>>> print(a == b)
True
>>> print(id(a), id(b))
4514453120 4390416000
>>> print(95 << 3)
760
>>> print(95 << 4)
1520
>>> print(256 >> 8)
1
