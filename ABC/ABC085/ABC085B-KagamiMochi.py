# ネットを参考にした記憶あり
N = int(input())
l_tmp = list(dict.fromkeys( [int(input()) for i in range(N)] ))
print(len(l_tmp))