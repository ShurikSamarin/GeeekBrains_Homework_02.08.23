lst = [3, 4, 2, 5, 7]
min = int(input("Input min "))
max = int(input("Input max "))

for i in range (len(lst)):
    if lst[i]>min and lst[i]<max:
        print(i)