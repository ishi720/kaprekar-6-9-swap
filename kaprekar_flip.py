import sys


def kaprekar_flip_step(n, width=4):
    """nをwidth桁として、6を9にした最大の数から、9を6にした最小の数を引いた値を返す。"""
    digits = f"{n:0{width}d}"
    big = int("".join(sorted(digits.replace("6", "9"), reverse=True)))
    small = int("".join(sorted(digits.replace("9", "6"))))
    return big - small


def kaprekar_flip(n, width=4):
    """nから6と9を入れ替えるカプレカの操作を繰り返し、履歴とループ部分を返す。"""
    history = [n]
    while True:
        n = kaprekar_flip_step(n, width)
        if n in history:
            return history, history[history.index(n):]
        history.append(n)


if __name__ == "__main__":
    arg = sys.argv[1]
    history, loop = kaprekar_flip(int(arg), len(arg))
    print(arg, history, "loop:", loop)
