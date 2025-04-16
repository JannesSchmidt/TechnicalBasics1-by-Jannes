import time
import random

# This ASCII-Art is AI-Generated
dog_art = r"""
 /^ ^\
/ 0 0 \
V\ Y /V
 / - \
 |    \\
 || (__)
"""

cat_art = r"""
 /\_/\
( o.o )
 > ^ <
"""

tickets = 2

print("Hey there, welcome to this minigame.") # starting sequence
time.sleep(1.5)
print("Please enter your name. Cookies are not optional.")
time.sleep(1.5)
name = input("Your name: ")
time.sleep(1)
print(name, "before you can continue, we quickly have to confirm your age.")
time.sleep(1.5)

age = int(input("Please enter your age: "))
time.sleep(1.5)

print("Your age is being processed. Please wait...")
time.sleep(2)
if age >= 100: # in case the age is to high
    print("!!! Age to high !!!".upper())
    time.sleep(1.5)
    print("!!! Possible risk detected !!!".upper())
    time.sleep(1.5)
    print("!!!!Server shutting down!!!!" .upper())
    time.sleep(2)
    quit()
print("Counting days...")
time.sleep(2)
print(name, age * 365, "days old.")
time.sleep(2)
print(name, age, "scanning browser history...")

time.sleep(2)
print("Building up suspense...")
time.sleep(2.5)
print(type(age), type(name))
time.sleep(0.5)
print("--> Human being confirmed.")
time.sleep(1.5)
print("Downloading invisible textures...")
time.sleep(1.5)
print("Setting up games...")
time.sleep(1.5)
print("Realising this is taking to long...") # at this point I dont even now what I wanted to do with this xD
time.sleep(1.5)
print("i: Synchronization completed.")
time.sleep(3)
print("______________________________________________________________")

if age < 18: # to young
    print("Sorry, this game is not available for you right now. Come back at a later point in time.")
    exit()
else:
    print("Access granted. Welcome!")
    time.sleep(1)
    print("As a welcome gift, you're granted 2 tickets. Do you accept?")
    time.sleep(1)
    accept = int(input("Do you accept the gift? 1 = Yes or 0 = No: "))

    if accept == 1:
        print("Very good, let's start then.")
        time.sleep(2)
    else:
        print("You declined the tickets. They are free. You get them anyway ^-^")
        time.sleep(2)

    while tickets > 0:
        print("___________________________________________________________________")
        print(f"\nYou have {tickets} ticket(s) left.")  # this line is AI-Generated
        print("Now it's time to choose your minigame!")
        time.sleep(1)
        game = int(input("(1) Quiz, (2) Gambling, (3) ASCII-Art. Keep in mind each costs 1 ticket: "))

        if game == 1: # Quiz
            tickets -= 1
            print("Choose difficulty: (1) Easy, (2) Medium, (3) Hard")
            difficulty = int(input("Enter choice: "))

            input('Press "Enter" when you\'re ready to start.')
            time.sleep(1)

            if difficulty == 1: #easy
                answer1 = input("Easy Question: How do you spell Sacrilegious: ")
                if answer1 == "Sacrilegious":
                    print("Well obviously you knew that...")
                    print("But still your reward:")
                    time.sleep(2)
                    print("""
                                               @@ @@
                                               @@@@@
                                                @@@ 
                                                 @  """)
                else:
                    print("Shame on you. It literally said Sacrilegious")



            elif difficulty == 2: # medium
                answer2 = input("Medium Question: What is the capital of Hungary: ")
                if answer2 == "Budapest" or "budapest":
                    print("Nice job! As a reward you get a heart:")
                    time.sleep(2)
                    print("""
                           @@ @@
                           @@@@@
                            @@@ 
                             @  """)
                else:
                    print("Nope it's Budapest")

            elif difficulty == 3: # hard

                answer3 = int(input("Hard Question: How many seconds are in 7 days "))
                if answer3 == 604800:
                    print("That's correct. Nerd...")
                    print("As a reward you get a heart:")
                    time.sleep(2)
                    print("""
                                               @@ @@
                                               @@@@@
                                                @@@ 
                                                 @  """)
                else:
                    print("Nope, it's actually 604800.")
            else:
                print("Invalid difficulty level. You had one job...")

        elif game == 2: # gambling that's why the user has to be over 18
            tickets -= 1
            print("Ah, a fellow gambling addict. I welcome you <3:")
            time.sleep(2)
            guess = int(input("Please guess a number between 1 and 6. \nYou have nothing to lose: "))
            roll = random.randint(1, 6)
            print(f"The dice rolled: {roll}")
            if guess == roll:
                print("Wait what?! You actually guessed correctly.")
                time.sleep(2.5)
                print("Well anyway, let's continue - shall we?")
                time.sleep(2)
            else:
                print("That was wrong. No luck today???")
                time.sleep(2)

        elif game == 3: # Art-Generator
            tickets -= 1
            print("ASCII-Art Generator! Choose your animal:")
            animal = input("Type 'dog' or 'cat': ")
            if animal == "dog":
                print("*Generating your image*")
                time.sleep(2)
                print(dog_art)
                time.sleep(2)
            elif animal == "cat":
                print("*Generating your image*")
                time.sleep(2)
                print(cat_art)
                time.sleep(2)
            else:
                print("invalid input :(")
                time.sleep(0.5)
                print("You had one job. No art for you!")

        else:
            print("Invalid game selection.")
            continue

print(name, "you are out of tickets. You may leave now. Bye") # ending sequence
time.sleep(2)
print("Shutting down Server")
time.sleep(2)
print("Evaluating", name, "...")
time.sleep(3)
print("Score 10/10", age, "is a very cool person <3")
time.sleep(2)
print("__________________________________________________________________________________________")

# credit for the help by the Tutors in the Digital Media Lab <3
# adding notes besides important code was also their idea