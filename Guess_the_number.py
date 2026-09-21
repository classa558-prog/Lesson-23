import random 
secret_number = random.randint(1, 100)
guesses = 0
while guesses <= 10:
    user_guess = int(input("Enter a number: "))
    print("Guesses: ", guesses)
    if user_guess == secret_number:
        print("You Won!")
        break
    elif user_guess > secret_number:
        print("Too Large!")
    elif user_guess < secret_number:
        print("Too Small!")

    guesses+=1
if guesses >= 10:
    print("You Lost!")
else:
    pass
    


