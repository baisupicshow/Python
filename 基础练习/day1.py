import string
# 删数
# 输入

N = int(input())
a = [1]*N
for i in range(N):
    a[i] = i
num = N
i = 0
k = 0
while(num > 1):
    if (k == 2 ):
        del a[i]
        num = num - 1
        k = 0
    else:
        i = i + 1
        k = k + 1
    if (i >= num):
        i = 0
print(a[0])