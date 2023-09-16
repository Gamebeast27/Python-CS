
print('PATTERNS')

#pattern 1

print('1st')
for j in range(4):
    for i in range(5):
        print('*',end=' ')
    print()

#pattern2

print('2nd')    

i=1
while i<6:
    print('* ' * i,)
    i+=1

print()

for i in range(1,6):
    print('* ' *i)    

#3
    
print('3rd')

i=5
while i >0:
    print('* ' * i,)
    i-=1

print()

for i in range(5,0,-1):
    print('* ' * i)

print()    


for j in range(6):
    for i in range(j):
        print('*',end=' ')
    print()


print()


for j in range(5,0,-1):
    for i in range(j):
        print('*', end=' ')
    print()    

#4
    
print('4th')

 
for i in range(5):
    for j in range(4-i):
        print(' ',end=' ')
    for k in range(i+1):
        print('*', end=' ')
    print() 

#5
    
print('5th')

for i in range(5):
    for j in range(i):
        print(' ',end=' ')
    for k in range(5-i):
        print('*',end=' ')
    print()

#6
    
print('6th')

row = 5
k = 2 * row - 2
for i in range(0,row):
    for j in range(0,k):
        print(' ',end=' ' )
    k-=1
    for l in range(0,i+1):
        print("*",end=' ' )
    print()

k= row- 2
for i in range(row,-1,-1):
    for j in range(k,0,-1):
        print(' ',end=' ')
    k+=1
    for l in range(0,i+1):
        print('*',end=' ')
    print()   

#7
    
print('7th')

for i in range(5):
    for j in range(i):
        print(' ',end=' ')
    for k in range(5-i):
        print('*',end=' ')
    print()    

for i in range(5):
    for j in range(4-i):
        print(' ', end= ' ')
    for k in range(i+1):
        print('*' , end=' ')
    print()

print('perfection')

for i in range(5):
    for j in range(i):
        print(' ',end=' ')
    for k in range(5-i):
        print('*',end=' ')
    print()
for l in range(4):
    for m in range(3-l):
        print(' ',end=' ')
    for n in range(2+l):
        print('*',end=' ')
    print()
#8

print('8th')

for i in range(5):
    for j in range(4-i):
        print(' ', end=' ' )
    for k in range(i+1):
        print('*',end=' ')
    for m in range(i):
        print('*',end=' ')
    print()    

for i in range(4):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range(4-i):
        print('*',end=' ')
    for m in range(3-i):
        print('*',end=' ')
    print()

print('maze')
for i in range(11,0,-1):
    if (i-2)%2!=0:
        for k in range(1):
            while k < 5: 
                for l in range(k):
                    print('a',end=' ')
                k+=1
        for j in range(i-2):
            if (i-2)%2!=0: 
                print('*',end=' ')
    
    print()

for i in range(5):
    for j in range(i):
        print('a',end=' ')
    
    print()

#9

print('9th')

#             1
#           2 2 
#         3 3 3 
#       4 4 4 4
#     5 5 5 5 5
#   6 6 6 6 6 6
# 7 7 7 7 7 7 7

for i in range(1,8):
    for k in range(7-i):
        print(' ',end=' ')
    for j in range(i):
        print(i,end=' ')
    print()    

print()
print()

print('10th')
#         1
#       2 1 2 
#     3 2 1 2 3 
#   4 3 2 1 2 3 4 
# 5 4 3 2 1 2 3 4 5

for i in range(1,6):
    for k in range(5-i):
        print(' ', end=' ')
    for m in range(i,1,-1):
        print(m,end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print()
print()

print('11th')

for i in range(4):
    for j in range(3-i):
        print(' ',end=' ')
    for l in range(i+1):
        print('*',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()   
for i in range(3):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range(3-i):
        print('*',end=' ')
    for l in range(2-i):
        print('*',end=' ')
    print()

print()
print()

print('12th')

for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    for k in range(i):
        print(' ',end=' ')
    for l in range(i):
        print(' ',end=' ')
    for m in range(5-i):
        print('*',end=' ')
    print()    
for i in range(2,6):
    for j in range(i):
        print('*',end=' ')
    for k in range(5-i):
        print(' ',end=' ')
    for l in range(5-i):
        print(' ',end=' ')
    for m in range(i):
        print('*',end=' ')
    print()

print()
print()

print('13th')

print()
#  0 1 2 
#0 *
#1 * *
#2 * * *
#3 * *
#4 *

for i in range(5):
    for j in range(3):
        if j==0 or (i==1 and j==1) or (i==2 and j==1) or (i==3 and j==1) or (i==2 and j==2):
            print('*',end=' ')
        else :
            print(' ',end=' ')
    print()  

print()
print()
print('14th')
print()

# 0 1 2 3
# *
# * *
# *   *
# *     *
# *   *  
# * *
# *

for i in range(7):
    for j in range(4):
        if j==0 or (i==1 and j==1) or (i==2 and j==2) or (i==3 and j==3) or (i==4 and j==2) or (i==5 and j==1):
            print('*',end= ' ')
        else:
            print(' ',end=' ')
    print()        

print()
print()

print('15th')

print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print()
print()

print('15th')

print()
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()    

print()
print()

print('16th')
print()
# 0 1 2 3 4
#0  *
#1 * *
#2*   *
#3 * *
#4  *

for i in range(5):
    for j in range(5):
        if (i==0 and j==2) or (i==1 and (j==1 or j==3)) or (i==2 and (j==0 or j==4)) or (i==3 and (j==1 or j==3)) or (i==4 and j==2):
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()
print()

#17

print('17th')

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()    

print()
print()

#18

print('18th')

#A
#B B
#C C C
#D D D D
#E E E E E

for i in range(6):
    for j in range(i):
        if i==1:
            print('A',end=' ')
        elif i==2:
            print('B',end=' ')
        elif i==3:
            print('C',end=' ')
        elif i==4:
            print('D',end=' ')
        elif i==5:
            print('E',end=' ')
    print()

print()
print()
print('OR')

print()
print()

for j in range(65,70):
    for i in range(65,j+1):
        print(chr(j),end= ' ')
    print()

print()
print()
#19
print('19th')

print()
print()

n=int(input('Enter digits: ' ))
print()
k = n-2
for i in range(n,-1,-1):
    for j in range(k,0,-1):
        print('',end=' ')
    k = k + 1
    for m in range(0,i+1):
        print('*',end=' ')
    print()    
k = 2 * n - 2
for i in range(0,n+1):
    for j in range(0,k):
        print('',end=' ')
    k -= 1
    for m in range(0,i+1):
        print('*',end=' ')
    print()    

print()
print()
print('OR')
print()
print()

for i in range(5):
    for j in range(i):
        print('',end=' ')
    for k in range(5-i):
        print('*',end=' ')
    print()    
for i in range(5):
    for j in range(4-i):
        print('',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()    


#20
print()
print()
print('20th')
print()
print()

for i in range(5):
        for k in range(i):
            print(' ',end=' ')
        for j in range(5-i):
            print('*',end=' ')
        for m in range(4-i):
            print('*',end=' ')
        print()    
        
for i in range(5):
        for j in range(4-i):
            print(' ',end=' ')
        for k in range(i+1):
            print('*',end=' ')
        for m in range(i):
            print('*',end=' ')
        print()    

#21
print()
print()
print('21st')
print()
print()

for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print() 
for i in range(4):
    for j in range(i+2):
        print('',end=' ')
    for k in range(4-i):
        print('*',end=' ')
    print()    

print()
print()
print('22nd')
print()
print()

#A
#A B
#A B C
#A B C D
#A B C D E

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()

print()
print()
