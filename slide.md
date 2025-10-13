---
title: Pythonでやってはいけないやってみるべきこと
subtitle: PyCon Mini 東海 2025
author: Atsushi Odagiri
aspectratio: 169
---
# Pythonでやってはいけないやってみるべきこと

## はじめに

## お前だれよ

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

# pickleファイルを直接編集する


# 実行中にsys.pathを変更する

# 自身をimportする

## 自身をimportしている途中でsys.moduleから削除する

- 無限ループできるのでは
- 停止条件を作れたらチャーチ数を実装できるのでは

# sys.frameを辿ってローカル変数を書き換える

## 案

停止条件のフラグを外部から書き換えるとか

# pthハック

# 名前空間パッケージと普通のパッケージを混同する

# \_\_main\_\_.py をカレントディレクトリに置く

## メモ

あまりおもしろくないので不採用

## 3.13
3.13では塞がってるかも

```python
>>> import __main__
>>> __main__
<module '__main__' from '/usr/lib/python3.13/_pyrepl/__main__.py'>
```

## 3.12

```python
>>> import __main__
>>> __main__
<module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
```

## 3.11

```python
>>> import __main__
>>> __main__
<module '__main__' (built-in)>
```

## 3.10以前

```python
>>> import __main__
>>> __main__
<module '__main__' (built-in)>
```

# \_\_init\_\_.py をカレントディレクトリに置く

## pytestが混乱するのでは

# モジュール外からグローバル変数を変更する

## 代入
## del
