lis = [10, 20, 30, 40, 10]
s = set()
for i in lis:
    s.add(i)
print(s)
li = list(s)
li.sort()
print(li[-2])
