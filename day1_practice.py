'''def double(a):
    work=(a*2)
    return work
ans = double(4)
print(ans)
Level 1 (your original task): Write a function that takes a number
and returns its square (the number multiplied by itself).
Then call it with three different numbers and print each result.'''
'''def square(a):
    work=(a**2)
    return work
square1=square(2)
square2=square(3)
square3=square(6)
print(square1)
print(square2)
print(square3)
Level 2: Write a function that takes two numbers
and returns the bigger one. You can’t use the built-in max. Use an if and else instead.'''
'''def maxi(a,b):
    if a>b:
        return(a)
    else:
        return(b)
    
    
aa = maxi(5,9)
aa1 = maxi(12,3)
aa2 = maxi(7,7)
print(aa)
print(aa1)
print(aa2)
Level 3: Write a function that takes a list of numbers and
returns the sum of only the even numbers in it. Odd numbers should be ignored.'''
'''a=[1, 2, 3, 4, 5, 6]
def sum(a):
    total = 0
    while  i in a.items:
        if i%2==0:
            total=total+i
    return total'''
'''def even_sum(a):
    total=0
    for i in a:
        if i%2==0:
            total=total+i
    return total
gg=even_sum(a=[1, 2, 3, 4, 5, 6])
print(gg)
Level 4: Write a function that takes a word and
returns True if it reads the same backwards (like “madam”), and False if it doesn’t.'''
'''def pali(a):
    if a[::]==a[::-1]:
        return True
    else:
        return False
gg = pali("mada")
print(gg)
Level 5: Write a function that takes a list of numbers and
returns both the smallest and the largest number together.'''
def num(a):
    smallest=a[0]
    largest=a[0]
    for i in a:
        if i < smallest:
            smallest=i
        if i>largest:
            largest=i
    
    return largest,smallest

        
gg=num([4, 5,1])
print(gg)

    
        
         
         