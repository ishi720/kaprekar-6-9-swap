import sys


def kaprekar_step(n, width=4):
    """nをwidth桁として、並べ替えた最大の数から最小の数を引いた値を返す。"""
    digits = f"{n:0{width}d}"
    big = int("".join(sorted(digits, reverse=True)))
    small = int("".join(sorted(digits)))
    return big - small


def kaprekar(n, width=4):
    """nからカプレカの操作を繰り返し、同じ数が出るまでの履歴を返す。"""
    history = [n]
    while True:
        n = kaprekar_step(n, width)
        if n in history:
            return history
        history.append(n)


if __name__ == "__main__":
    arg = sys.argv[1]
    print(arg, kaprekar(int(arg), len(arg)))
