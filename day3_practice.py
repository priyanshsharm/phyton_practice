#dictionary
'''
Level 1

Make a dictionary of three students and their marks. Print one student’s marks by name.
Add a fourth student, then change one student’s marks.'''
students = {
    "priyansh":{'phy':81,
                'chem':90,
                'maths':88},
    "rahyl":{'phy':80,
                'chem':91,
                'maths':86},
    "titu":{'phy':82,
                'chem':92,
                'maths':89}}

#print(dict)
students['nonu']={'phy':84,
                'chem':95,
                'maths':70}
#print(dict)
#print(students["priyansh"]['maths'])
students["priyansh"]['phy']=89
#print(students["priyansh"]['phy'])
'''Loop through the dictionary and print each student’s name with their marks on one line,
like “priyansh: phy 89, chem 90, maths 88”.
Looping over a dictionary gives you the keys, so think about how to get the marks from each key.
Print only the students whose maths mark is above 85.
Find the total of each student’s three marks and print it next to their name.
You’ll need a second loop inside the first, going through the subjects.'''
'''for name,marks in students.items():
    if  marks['maths']>85:
        print(name)'''
'''for name ,marks in students.items():
    total=0
    for i in marks.values():
        total=total+i
    print(name,total)'''
gg=("the cat saw the dog and the cat ran")
word=gg.split()

count={}
for i in word:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count)
        
    
        

