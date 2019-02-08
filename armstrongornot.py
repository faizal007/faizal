fz=int(input())
afz=list(map(int,str(fz)))
bfz=list(map(lambda x:x**3,afz))
if(sum(bfz)==fz):
  print("yes")
else:
  print("no")  
