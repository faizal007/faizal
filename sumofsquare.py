n=int(input())
m=0
while(n>0):
    d=n%10
    m=m+(d*d)
    n=n//10
print(m)
