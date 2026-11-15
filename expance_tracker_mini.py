total=0

while True:
    
    
    try:
        
        expence_asker=(input("expence_amount:"))
        if expence_asker=="done":
            print("done")
            break

        
        else:
            amount=float(expence_asker)
            if amount<0:
                raise ValueError("value cannot be negatice")
            
            print(amount)
        
        
            
        
    except ValueError:
        print("value is not valid")
    else:
        
        total=total+amount
        print("total amount:",total)
    
    
    
    

        

        
    
    
   
    
    