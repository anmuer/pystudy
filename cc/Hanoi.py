# coding: UTF-8
# 汉诺伊塔 x、y、z 柱子，x 借助 y 移到 z
def hanoi(n, x, y, z):
    if n == 1:
        print(x + '-->' + z)
    else:
        # 把 n-1 个方块 x->y
        hanoi(n-1, x, z, y)
        # 把第 n 方块从 x->z
        print(x + '-->' + z)
        # 把 n-1 个方块从 y->z
        hanoi(n-1, y, x, z)


if __name__ == '__main__':
    number = int(input("输入方块数："))
    hanoi(number, 'X', "Y", "Z")