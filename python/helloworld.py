# Short code written in python
# Code added to print a prime number on each line

a= int(input("Insert any number more than 2: "))

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

print("My name is Melanie and my prime list from 2 till %d is: " %(a))       
primeList(a)
