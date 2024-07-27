def recur(x):
    if(x>0):
        r=x+ recur(x-1)
        print(r)
    else:
        r=0
    return r

recur(7)
