def happpy_count(ssum):
    sum1=0
    happy=0
    lst = []
    while(ssum!=0):
        #print(ssum)
        lst = int(ssum%10)
        ssum=int(ssum/10)
        #print(lst)
        lst=lst*lst
        s= str(lst)
        #print(s)
        for i in s:
            sum1=sum1+int(i)
        #print(sum1)
        ssum=sum1
    return sum1
