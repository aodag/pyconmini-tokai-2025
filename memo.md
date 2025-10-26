# 主にボツネタ退避場所

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

# 名前空間パッケージと普通のパッケージを混同する

# sys.frameを辿ってローカル変数を書き換える

## 案

停止条件のフラグを外部から書き換えるとか

