---
title: Pythonでやってはいけないやってみるべきこと
subtitle: PyCon Mini 東海 2025
author: Atsushi Odagiri
aspectratio: 169
---
# Pythonでやってはいけないやってみるべきこと

## はじめに

## お前だれよ

## ハックルベリーと黒魔術

- プログラミングをお仕事にしていると
  - 構成管理
  - 静的型チェック
  - テストとかカバレージ
  - レビュー
  - ...
- 趣味でのプログラミング
  - 同じツールセット使うとか
  - pytest, ruff, pyright, mypy...
  - ちょっと窮屈感
  - お前らに何がわかるってんだ！
- プログラミングは楽しい！
  - 作りたいものが動くこと
  - 疑問を突き詰めること
  - もっとめちゃくちゃなことをしよう
  - 悪いことをしよう
- 疑問を突き詰めるのは冒険
  - ハックルベリー
- 黒魔術とは違うのか
  - 達成したいのは疑問の解消
    - それとちょっとした冒険
  - 黒魔術は欲望を解消する
    - これをなんとかして動かさないと！
- テクニックは近いかもしれない

# 今日のお話

- ちょっとした冒険的なプログラミングの一例
- たまにはこんなことしてもいいじゃないですか

# \_\_class\_\_ を書き換える

## 2つのクラス

```python
>>> class Dog:
...     def greet(self):
...         print("わん！")
...
>>> class Cat:
...     def greet(self):
...         print("にゃー")
...
```

## 変えれちゃう

```python
>>> aodog = Dog()
>>> type(aodog)
<class '__main__.Dog'>
>>> aodog.greet()
わん！
>>> aodog.__class__
<class '__main__.Dog'>
>>> aodog.__class__ = Cat
>>> type(aodog)
<class '__main__.Cat'>
```

## だが、メソッドはバウンドされているのでは？

```python
>>> aodog.greet()
にゃー
>>> aodog.greet
<bound method Cat.greet of <__main__.Cat object at 0x7f73a6f84830>>
>>> aodog.__class__ = Dog
>>> aodog.greet
<bound method Dog.greet of <__main__.Dog object at 0x7f73a6f84830>>
```

ちゃんと変わってる

## メソッドを書き換えたなら？

```python
>> Dog.greet = lambda self: print("わんわん！")
>>> aodog.greet()
わんわん！
```

## classをdelしたら？

```python
>>> del Dog
>>> aodog.greet()
わんわん！
>>> aodog.__class__
<class '__main__.Dog'>
>>> Dog = aodog.__class__
>>> Dog
<class '__main__.Dog'>
```

## メソッドを変数に退避しておいたら？

```python
>>> g = aodog.greet
>>> Dog.greet = lambda self: print("わんわんわん！")
>>> g()
わんわん！
>>> aodog.greet()
わんわんわん！
```

# 自身をimportする

## 自身をimportしたら無限ループになる？

a.py

```python
import a
```

問題なし

## なぜだろう？

- importはincludeとは違う
- もうインタプリタにロードされてるモジュールを再評価しない
- 変数に入れるだけ

## import済というフラグ

- sys.modules

## importされてる間に例外が発生すると？

- importの事実を撤回

# モジュール外からグローバル変数を変更する
## なんとかしてみよう

- sys.modulesを参照して自分を別モジュールのグローバル変数に代入
- その後例外を投げてsys.modulesから自分を消去

a.py
```python
x = None
v = 0
try:
  import b
except Exception as e:
  print(f"{e=}")
print(f"{x=}")
```

b.py
```python
import sys
import a

a.x = sys.modules["b"]
a.v += 1
print(f"{a.x=}")
raise ValueError
```

## TODO importで数を数える

## TODO generatorで無限import

## iterableなモジュール

- モジュールに `__iter__` があってもiterableと解釈されない

```python
>>> import i
>>> i.__iter__()
<list_iterator object at 0x7f13aaae5f30>
>>> iter(i)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    iter(i)
    ~~~~^^^
TypeError: 'module' object is not iterable
```

## モジュールよ、お前は今からIterableになるんだよ！

```python
>>> from collections.abc import Iterable
>>> i.__class__
<class 'module'>
>>> i.__class__ = Iterable
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    i.__class__ = Iterable
    ^^^^^^^^^^^
TypeError: __class__ assignment only supported for mutable types or ModuleType subclasses
```

## 強情なやつだね！

- これならどうだい！？

```python
>>> class IterableModule(m, Iterable):
...     pass
...
>>> i.__class__ = IterableModule
>>> iter(i)
<generator object Iterable.__iter__ at 0x7f4cda3c2bc0>
``

# pthハック

# なんでもキャッチ、sys.exit

## sys.exit

```python
$ python
>>> import sys
>>> sys.exit()
$
```

## Exceptionでキャッチできない

```python
$ python
>>> import sys
>>> try:
...     sys.exit()
... except Exception as e:
...     print(e)
...
$
```

## BaseExceptionでキャッチ

```python
$ python
>>> import sys
>>> try:
...     sys.exit()
... except BaseException as e:
...     print(type(e))
...     print(e)
...
<class 'SystemExit'>

>>>
```

## atexit

```python
$ python
>>> import sys
>>> import atexit
>>> atexit.register(lambda: print("good-bye"))
<function <lambda> at 0x7f003d65ab60>
>>>
good-bye
```

## atexitで無限ループできるか？

```python
$ python
>>> import sys
>>> import atexit
>>> import time
>>> def main():
...     for i in range(10):
...         print(i)
...         time.sleep(1)
...     sys.exit()
...
>>> atexit.register(main)
<function main at 0x7f24f549a8e0>
>>>
0
1
2
3
4
5
6
7
8
9
Exception ignored in atexit callback <function main at 0x7f24f549a8e0>:
Traceback (most recent call last):
  File "<python-input-3>", line 5, in main
SystemExit:
```

# 変な変数名

## オブジェクトのattr

```python
>>> class A:
...     pass
...
>>> a = A()
>>> a.a = 1
>>> setattr(a, "b", 2)
>>> a.b
2
>>> setattr(a, "(´・ω・｀)", 3)
>>> getattr(a, "(´・ω・｀)")
3
>>> dir(a)
['(´・ω・｀)', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b']
>>> vars(a)
{'a': 1, 'b': 2, '(´・ω・｀)': 3}
```

## \_\_main\_\_

```python
>>> import sys
>>> sys.modules["__main__"]
<module '__main__' from '/usr/lib/python3.13/_pyrepl/__main__.py'>
>>> setattr(sys.modules["__main__"], "a", 1)
>>> a
1
```

# まとめ

- 役に立たない
- やってるときだけ楽しい
  - 資料に起こしてみるとなぜこんなことを真剣にやったのだろうと思う
- 楽しいのだからそれでいい
- こうなるはずだというのをやってみるのは大事
