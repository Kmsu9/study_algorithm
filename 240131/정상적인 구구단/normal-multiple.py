n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n:
            print("%d * %d = %d"%(i, j, i*j), end = '')
        else:
            print("%d * %d = %d"%(i, j, i*j), end = ', ')
    print()