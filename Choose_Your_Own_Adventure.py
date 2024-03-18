name = input('Please enter your name: ')
print('Welcome to Jumanji-Copy', name)

answer = input("You are on a grass field, a rocket is coming from behind. Do you want to dodge left or right? ").lower()

if answer == "left":
    answer = input("You have come to a river. You can either walk around it or swim across the stinky river. What do you want to do? ").lower()
    if answer == "swim":
        print("Your tried swimming and your body rotted.")
    elif answer == "walk":
        print("You kept walking and ran out of food and eventually died hungry.")
    else:
        print('The option is not valid!')
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to take your chances or turn back? (cross/back)").lower()
    if answer == "cross":
        print("Congratulations! You crossed the bridge and successfully made it to safe haven.")
        answer = input("You meet people of different ethnicity. Do you want to ask them for help or run away from them? (talk/run)").lower()
        if answer == "talk":
            print('Congratulations, you finally won the game and live happliy.')
        elif answer == "run":
            print('YOu see no other humans, you are alone and hungry and zombies eat you')
        else:
            print('Not a valid option! YOu lose noob.')
    elif answer == "back":
        print("You decided to go back but there are zombies sorrounding you now and you lose!")
    else:
        print("Not a valid option. YOu lose noob!")
else:
    print('The option is not valid!')

print('Thank you for playing my game!')


