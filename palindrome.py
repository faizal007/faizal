nfz=int(input())
tempfz=nfz
nfz<=1000
revfz=0
while(nfz>0):
    digfz=nfz%10
    revfz=revfz*10+digfz
    nfz=nfz//10
if(tempfz==revfz):
    print("yes")
else:
    print("no")
