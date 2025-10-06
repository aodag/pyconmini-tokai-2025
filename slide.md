---
title: Pythonでやってはいけないやってみるべきこと
subtitle: PyCon Mini 東海 2025
author: Atsushi Odagiri
---
# Pythonでやってはいけないやってみるべきこと

# __class__ を書き換える

# sys.frameを辿ってローカル変数を書き換える

# pickleファイルを直接編集する

# 実行中にsys.pathを変更する

# 自身をimportする

# 自身をimportしている途中でsys.moduleから削除する

- 無限ループできるのでは
- 停止条件を作れたらチャーチ数を実装できるのでは

# pthハック

# 名前空間パッケージと普通のパッケージを混同する

# __main__.py をカレントディレクトリに置く

# __init__.py をカレントディレクトリに置く

- pytestが混乱するのでは

# モジュール外からグローバル変数を変更する

- 代入
- del
