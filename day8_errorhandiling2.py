try:
    
    a=int(input("number:"))
    b = a**2
except ValueError:
    print("invalid value")
  
else:
    print(b)
finally:
    print("prigram finished")
