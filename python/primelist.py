# Prime list function(primeList)

def primeList(a):
    for i in range(2, a):
        x=1
        for j in range(2, i):
            n=i%j
            if n==0:
                x=0
                break
        if x==1:
            print(i)

primeList(102)
