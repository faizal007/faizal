from math import*
while True:
  try:

    sour=float(input("Enter source:"))
    dest=float(input("Enter Destination:"))

    if(sour>=0 and dest>=0 and sour<dest ):
      print("1-auto")
      print("2-mini")
      print("3-micro")
      print("4-prime")
      choice=float(input("Enter your choice(1 or 2 or 3 or 4):"))
      choice=round(choice) 
      if choice== 1:
        m=10.0
        fare=(dest-sour)*m
        print("your fare=",fare)
      elif choice== 2:
        m=20.0
        fare=(dest-sour)*m
        print("your fare=",fare)
      elif choice== 3:
        m=50.0
        fare=(dest-sour)*m
        print("your fare=",fare)  
      elif choice== 4:
        m=100.0
        fare=(dest-sour)*m
        print("your fare=",fare) 
      else:
        print("INVALID")   
      c=(dest-sour)
      print("\n\n\t-----------------------------------")  
      print("\n\t\t\t CAB DETAILS")
      print("\n\t-----------------------------------")
      print("\t\tYOUR TOTAL DISTANCE: ",c,"km")
      print("\t\tFARE PER KM        :Rs.",m)
      print("\t-----------------------------------")
      print("\t\tTOTAL FARE         :Rs.",fare)
      print("\t-----------------------------------") 
    else:
      if(sour<0 and dest<0):
        print("INVALID SOURCE AND DESTINATION")
      elif(sour<0):
        print("INVALID SOURCE")  
      elif(dest<=0):
        print("INVALID DESTINATION")    
      else:
        print("INVALID SOURCE AND DESTINAION")  
  except:
    print("INVALID")      
