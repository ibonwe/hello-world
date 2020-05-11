# Short code written in python
# Code added to print a prime number on each line

print("My name is Melanie")

for i in range(2,101):
    x=1
    for j in range(2, i):
        n=i%j
        if n==0:
            x=0
            break
    if x==1:
        print (i)
