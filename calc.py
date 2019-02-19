a=int(input("a:"))
b=int(input("b:"))
print("1-ADD")
print("2-SUBTRACTION")
print("3-MULTIPLICATION")
print("4-DIVISION")
choice=float(input("Enter 1 or 2 or 3 or 4 :"))
choice=round(choice)
if (choice==1):
  c=a+b
  print(c)
elif (choice==2):
  c=a-b 
  print(c) 
elif (choice==3):
  c=a*b
  print(c)
elif (choice == 4):
  if b==0:
    print("Infinity")
  else:
    c=a/b
    print(c)  
else:
  print("INVALID")    
