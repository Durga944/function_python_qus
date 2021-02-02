def check_num():
    num1=int(input("enter any num"))
    num2=int(input("enter any num"))
    if(num1%2==0 and num2%2==0):
        print("num1 and num2 is even")
    else:
        print("not even")
check_num()






def check_num(a,b):
    i=0
    l=len(a)
    while(i<l):
        if(a[i]%2==0 and b[i]%2==0):
            print("even")
        else:
            print("not even")
        i=i+1
check_num([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])