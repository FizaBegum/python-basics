def prime(n):
    f=0
    for i in range(2,int(n/2)):
        f=1

    if(f==0):
        print("Prime")
    else:
        print("Not Prime")

n=int(input())
prime(n)
