from collections import Counter

from kaprekar_flip import kaprekar_flip


def aggregate(width):
    """width桁の全ての数で6と9を入れ替えるカプレカの操作をし、行き着くループごとの件数を数える。

    ループは並べ替えたタプルにして、入る位置が違っても同じループとして数える。
    """
    result = Counter()
    for n in range(10 ** (width - 1), 10 ** width):
        _, loop = kaprekar_flip(n, width)
        result[tuple(sorted(loop))] += 1
    return result


def zero_breakdown():
    """4桁で0に行き着く数を、0になる理由ごとに数える。"""
    result = Counter()
    for n in range(1000, 10000):
        history, loop = kaprekar_flip(n)
        if loop != [0]:
            continue
        digits = set(str(n))
        if len(digits) == 1:
            result["最初からゾロ目"] += 1
        elif digits <= {"6", "9"}:
            result["最初から6と9だけ"] += 1
        elif 6996 in history:
            result["途中で6996を経由"] += 1
        else:
            result["その他"] += 1
    return result


def longest():
    """4桁で、ループに入るまでの手数が一番多い数とその手数を返す。"""
    def steps(n):
        """nからループに入るまでの手数を返す。"""
        history, loop = kaprekar_flip(n)
        return len(history) - len(loop)

    n = max(range(1000, 10000), key=steps)
    return n, steps(n)


if __name__ == "__main__":
    for width in (3, 4, 5):
        print(f"== {width}桁")
        for loop, count in aggregate(width).most_common():
            print(count, loop)

    print("== 0になる内訳")
    for kind, count in zero_breakdown().most_common():
        print(kind, count)

    print("== ループに入るまで一番長い数字")
    print(longest())
