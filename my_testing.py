str = "hare rama hare krishna"
d = {}

for i in str:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] = d[i] + 1
