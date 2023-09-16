import random
print(" WELCOME TO THE GUESSING GAME ")
print(''' INSTRUCTIONS \n You will enter a range and then the computer will select a number from it.
 Then you have to guess the number within 5 guesses..''')
print()
print()
a=int(input("Enter the upper limit: "))
b=int(input("Enter the lower limit: "))
print()
num=random.randint(b,a)
#print(num)

for i in range(5):
    print()
    use=int(input("Enter your guess:  "))
    if use<num:
        print("You entered a smaller number!")
    elif use > num:
        print("You entered a greater number!")
    else :
        print("Correct Guess")
        break
else :
    print()
    print("The number was",num)
    print("You LOST, you were not able to guess the number")
    print()
print()
print("Thank You for playing")


