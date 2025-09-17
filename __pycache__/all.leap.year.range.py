def isleapyear(year):
    return((year%100!=0 and year%4==0)or(year%400 ==0))
s_year=int(input("Enter start year:"))
e_year=int(input("Enter end year:"))
if(s_year>e_year):
    print("Invalid input")
else:
    print("Leap year:")
    for i in range(s_year,e_year):
        flag=isleapyear(i)
        if flag:
            print(i, end=" ")