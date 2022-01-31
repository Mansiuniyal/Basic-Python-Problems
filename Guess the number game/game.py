a=25
s=7
print("Welcome to Guess the number Game!!")
print("You have only 7 chances to guess the number right")
c=1
while(c<=s):
    print("Guess the number between 1 to 30")
    n=int(input())
    if(n<a):
        print("Wrong\nHint:Your no. is smaller than actual no.")
        print("No of guesses left -",(s-c))
        c=c+1
    elif(n>a):
        print("Wrong\nHint:Your no. is greater than actual no.")
        print("No of guesses left -",(s-c))
        c=c+1
    elif(n==a):
        print("Well played! You got it right")
        break
    else:
        print("Invalid Input")
if n!=a and c>s:
    print("The actual no. was",a)
    print("Better luck next time!")


