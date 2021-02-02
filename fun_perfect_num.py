def perfect():
    user=int(input("enter any num"))
    a=user
    sum=0
    i=1
    while(i<user):
        if(user%i==0):
            sum=sum+i
        i=i+1
    if(a==sum):
        print("perfect")
    else:
        print("not perfect")
perfect()