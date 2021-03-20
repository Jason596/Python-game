i = 1
while i < 10:
    j = 1
    while j <= i:
        # print(i)
        print(f"{j}*{i}={i*j}", end=" ")
        print("%d*%d=%d" %(j, i, i*j), end=" ")
        # print(j)
        j += 1

    # 换行
    print()
    i += 1
