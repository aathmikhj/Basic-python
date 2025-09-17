def iseven(num):
    return num%2==0
count=int(input("Enter num:"))
series=1
while count>0:
    flag=iseven(series)
    if flag:
        print(series)
        count -= 1
    series +=1


