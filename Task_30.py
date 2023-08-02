a1 = int(input("Input a1 "))
n = int(input("Input n "))
d = int(input("Input d "))

def prog(a1,n,d):
    list=[]
    for i in range (n):
        list.append(a1+i*d)
    return list

print(*prog(a1,n,d))

#an = a1 + (n-1) * d