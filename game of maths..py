# A Game of Maths 
print('Hello,\n what\'s your name buddy')
name=input('My name is : ')
print('OK', name,'Let\'s play a game.') 
print()
print('LEVEL ONE , addition')
a=float(input('entre first number(a): '))
b=float(input('entre second number(b): '))
c=float(input('entre third number/answer,(a+b): '))
d=a+b
print()
print()
print(d==c)
if d!=c :
    print('well tried')
    print('answer is')
    print(d)
    print('Your Score = 0%')
else:
    print('congratulations')
    print()
    print()
    print('LEVEL TWO , subtraction')
    e=float(input('entre first number(a): '))
    f=float(input('entre second number(b): '))
    g=float(input('entre third number/answer,(a-b): '))
    h=e-f
    print()
    print()
    print(h==g)
    if h!=g :
        print('well tried')
        print('answer is')
        print(h)
        print('Your Score = 25%')
    else:
        print('congratulations')
        print()
        print()
        print('LEVEL THREE , multiplication ')
        i=float(input('entre frist number(a): '))
        j=float(input('entre second number((b): '))
        k=float(input('entre third number/answer,(a*b): '))
        l=i*j
        print()
        print()
        print(l==k)
        if l!=k :
            print('well tried')
            print('answer is')
            print(l)
            print('Your Score = 50%')
        else:
            print('congratulations')
            print()
            print()
            print('LEVEL FOUR, division')
            m=float(input('entre first number(a): '))
            n=float(input('entre second number(b): '))
            o=float(input('entre third numbre(a/b): '))
            p=m/n
            print()
            print()
            print(p==o)
            if p!=o :
                print('well tried')
                print('answer is')
                print(p)
                print('Your Score = 75%')
            else:
                print()
                print()
                print('WELL DONE , YOU HAVE COMPLETED THE GAME')
                print('YOUR SCORE = 100%')
                print('YOU ARE A MATHEMATICIAN',name)
print()
print()
print('THANK YOU FOR PLAYING')