nfz=int(input())
mfz=0
while(nfz>0):
    dfz=nfz%10
    mfz=mfz+(dfz*dfz)
    nfz=nfz//10
print(mfz)
