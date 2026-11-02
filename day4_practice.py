
with open("notes.txt","w") as f:
    f.write("i am a best coder\n ")
    f.write(" i am only 18 years old doing iternships\n")
    f.write(" my name is priyansh\n")
with open("notes.txt","r") as f:
    data=f.read()
    print(data)
with open("notes.txt","a") as f:
    f.write("my hobby is sleeping\n")
    f.write("my plan for this year is to be adict to my work and explore my self in the thing what i am doing now\n")

   
    
count=0
with open("notes.txt","r") as f:
    for lines in f:
        count=count+1
        print(count,"-",lines.strip())
        

        