import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number greater than 0')
        quit()
else:
    print('Please type a number next time')
    quit()


random_number = random.randint(0, top_of_range)
print(random_number)
guesses = 0
while True:
    user_guess = input('Make a guess please: ')
    if user_guess.isdigit():
        guesses += 1
        user_guess = int(user_guess)
        if user_guess < 0:
            print("Please enter a number greater than 0")
            continue
    else:
        print("Please enter a positive number")
        continue
    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print('You are below the number')

print("You got it in", guesses, "guesses")
