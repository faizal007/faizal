chvc=str(raw_input())
vowel=("a","e","i","o","u")
if(chvc>"a"and chvc<"z" or chvc>="A" and chvc<="Z"):
  if chvc in vowel:
    print("vowel")
  else:
    print("consonant")  
else:
  print("Invalid")   
