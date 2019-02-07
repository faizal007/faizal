yearfz=int(input())
if(( yearfz%400 == 0)or (( yearfz%4 == 0 ) and ( yearfz%100 != 0))):
  print("yes")
else:
  print("no")
