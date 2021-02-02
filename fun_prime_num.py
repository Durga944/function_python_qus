def prime(n):
    i=1
    while(i<=n):
        j=2
        while(j<i):
            if(i%j==0):
                print(i,"not prime")
                break
            j=j+1
        else:
                print(i,"prime")
        i=i+1
prime(100)