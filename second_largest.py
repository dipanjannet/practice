alist = [10, 20, 30, 10, 50]
largest, larger = alist[0], alist[0]

for num in alist:
    if num > largest:
        largest, larger = num, largest
        print('largest', largest)
        print('larger', larger)
    elif num > larger:
        larger = num
        print(larger)
print(larger)
