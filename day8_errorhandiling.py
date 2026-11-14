'''while True:
    try:
    
        a = int(input("first number:"))
        b = int(input("second number:"))
        c = a/b
        print(c)
        break
    
    except ZeroDivisionError:
        print("cannot divide by zero")
        
    except ValueError:
        print("invalid value")

try:
    
    a=int(input("number:"))
    b = a**2
except ValueError:
    print("invalid value")
  
else:
    print(b)
finally:
    print("prigram finished")

try:

    a=input("file name:")
    b=open(a,"r")
except FileNotFoundError:
    print("file not found")
else:
    text= b.read()
    print(text)
    b.close()
finally:
    print("done")
    '''

try:
    a=int(input("your marks:"))
    if 0>a or a>100:
        raise ValueError("value must be between 0 to 100")
            
except ValueError as e:
    print(e)
else:
    print("marks saved")
        
    
