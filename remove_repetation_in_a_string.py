def replace_char(s):
    count = 0
    if len(s) == 1:
        return s
    else:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                save = s[i]
                s = s.replace(save, "")
                count = count+1
                if count > 0:
                    for r in range(count):
                        s = replace_char(s)
            else:
                continue
            return s


s = 'aabddbccv'
p = replace_char(s)
print("Original String:", s)
print("ans:", p)
