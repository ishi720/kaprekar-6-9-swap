# kaprekar

6を逆さにして9として扱うルールで、カプレカ数が成立するかを検証するコードです。

## 動作環境

- Python 3.13

標準ライブラリのみを使用しています。

## ファイル

| ファイル | 内容 |
|:--|:--|
| `kaprekar.py` | 普通のカプレカの操作 |
| `kaprekar_flip.py` | 大きい数では6を9に、小さい数では9を6にするカプレカの操作 |
| `aggregate.py` | 3桁・4桁・5桁の全パターンの集計 |

## 実行方法

`kaprekar.py` と `kaprekar_flip.py` は、引数で数値を指定します。桁数は入力した文字数で決まります。

```sh
py kaprekar.py 4567
py kaprekar_flip.py 99831
py aggregate.py
```
