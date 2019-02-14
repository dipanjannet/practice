lis = [12, 13, 11, 10, 15]
dis = {}
for i in lis:
    if i not in dis.keys():
        dis[i] = 1
    else:
        dis[i] += 1
print(dis)
