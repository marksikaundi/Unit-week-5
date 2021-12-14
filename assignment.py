
import math


def my_sqrt(a):
    x = 1
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y

    return x


def test_sqrt():
    a = 1
    while a < 10:
        my = my_sqrt(a)
        math_sqrt = math.sqrt(a)
        diff = math.fabs(my - math_sqrt)
        print("a = {a} | my_sqrt(a) = {my} | math.sqrt(a) = {math} | diff = {diff}".format(
            a=a,
            my=my,
            math=math_sqrt,
            diff=diff
        ))

        a += 1


if __name__ == "__main__":
    test_sqrt()

# part 3

