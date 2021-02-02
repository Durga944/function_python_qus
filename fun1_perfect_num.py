def perfect():
    i=1
    while(i<=1000):
        a=i
        sum=0
        j=1
        while(j<i):
            if(i%j==0):
                sum=sum+j
            j=j+1
        if(a==sum):
            print(a,"perfect")
        else:
            print(a,"not perfect")
        i=i+1
perfect()