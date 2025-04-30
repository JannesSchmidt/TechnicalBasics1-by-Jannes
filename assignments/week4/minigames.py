import time
import random

DEBUG = False  # Set to True to skip name/age input for quick testing


def evaluate(score, mistakes): # Evaluation function
    return score - mistakes

# ASCII Art
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

def main():
    # Game variables
    tickets = 3
    score = 7
    mistakes = 0

    if DEBUG:
        name = "Admin"
        age = 99
        print("\033[31mDEBUG MODE ENABLED. Skipping intro.\033[0m")
        time.sleep(1)
        print("\033[31mAdmin registered\033[0m")
    else:
        print(r"""
__        __   _                                   
\ \      / /__| | ___ ___  _ __ ___   ___    
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \  
  \ V  V /  __/ | (_| (_) | | | | | |  __/ 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  
""")

        time.sleep(1.5)
        print("Please enter your name. Cookies are not optional.")
        time.sleep(1.5)
        name = input("Your name: ")

        time.sleep(1)
        print(name, "before you can continue, we quickly have to confirm your age.")
        time.sleep(1.5)

        while True:
            try:
                age = int(input("Please enter your age: "))
                break
            except ValueError:
                print("That was not a valid number. Please enter your age using digits.")
                mistakes += 1

        time.sleep(1.5)
        print("Your age is being processed. Please wait...")
        time.sleep(2)

        if age >= 125:
            print("!!! AGE TOO HIGH !!!")
            time.sleep(1.5)
            print("!!! POSSIBLE RISK DETECTED !!!")
            time.sleep(1.5)
            print("!!!! SERVER SHUTTING DOWN !!!!")
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
        print("i: Synchronization completed.")
        time.sleep(3)
        print("___________________________________________________________________")

        if age < 18:
            print("Sorry, this game is not available for you right now. Come back at a later point in time.")
            exit()
        else:
            print("Access granted. Welcome!")
            time.sleep(1)
            print("As a welcome gift, you're granted 3 tickets. Do you accept?")
            time.sleep(1)
            accept = int(input("Do you accept the gift? 1 = Yes or 0 = No: "))

            if accept == 1:
                print("Very good, let's start then.")
                time.sleep(2)
            else:
                print("You declined the tickets. They are free. You get them anyway ^-^")
                time.sleep(2)

    # Game loop
    while tickets > 0:
        print("___________________________________________________________________")
        print(f"\nYou have {tickets} ticket(s) left.")
        print("Now it's time to choose your minigame!")
        time.sleep(1.4)
        try:
            game = int(input("(1) Quiz, (2) Gambling, (3) ASCII-Art. Keep in mind each costs 1 ticket: "))
        except ValueError:
            print("Invalid input.")
            mistakes += 1
            continue

        if game == 1:
            tickets -= 1
            while True:
                try:
                    difficulty = int(input("Choose difficulty: (1) Easy, (2) Medium, (3) Hard: "))
                    if 1 <= difficulty <= 3:
                        break
                    else:
                        print("Difficulty must be between 1 and 3.")
                        mistakes += 1
                except ValueError:
                    print("That was not a valid number. Please enter 1, 2 or 3.")
                    mistakes += 1

            if difficulty == 1:
                answer1 = input("Easy Question: How do you spell Sacrilegious: ")
                if answer1 == "Sacrilegious":
                    print("Well obviously you knew that...")
                    score += 1
                    time.sleep(2)
                    print("""
                                           @@ @@
                                           @@@@@
                                            @@@ 
                                             @  """)
                else:
                    print("Shame on you. It literally said Sacrilegious")
                    mistakes += 1

            elif difficulty == 2:
                answer2 = input("Medium Question: What is the capital of Hungary: ")
                if answer2.lower() == "budapest":
                    print("Nice job! As a reward you get a heart:")
                    score += 1
                    time.sleep(2)
                    print("""
                       @@ @@
                       @@@@@
                        @@@ 
                         @  """)
                else:
                    print("Nope it's Budapest")
                    mistakes += 1

            elif difficulty == 3:
                try:
                    answer3 = int(input("Hard Question: How many seconds are in 7 days: "))
                    if answer3 == 604800:
                        print("That's correct. Nerd...")
                        score += 1
                        time.sleep(2)
                        print("""
                                           @@ @@
                                           @@@@@
                                            @@@ 
                                             @  """)
                    else:
                        print("Nope, it's actually 604800.")
                        mistakes += 1
                except ValueError:
                    print("Invalid input. That's a mistake.")
                    mistakes += 1

        elif game == 2:
            tickets -= 1
            print("Ah, a fellow gambling addict. I welcome you <3:")
            time.sleep(2)
            try:
                guess = int(input("Please guess a number between 1 and 6. \nYou have nothing to lose: "))
            except ValueError:
                print("Not a valid number.")
                mistakes += 1
                continue
            roll = random.randint(1, 6)
            print(f"The dice rolled: {roll}")
            if guess == roll:
                print("Wait what?! You actually guessed correctly.")
                score += 1
                time.sleep(2.5)
                print("Well anyway, let's continue - shall we?")
                time.sleep(2)
            else:
                print("That was wrong. No luck today???")
                mistakes += 1
                time.sleep(2)

        elif game == 3:
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
                print("Invalid input :(")
                mistakes += 1
                time.sleep(0.5)
                print("You had one job. No art for you!")

        else:
            print("Invalid game selection.")
            mistakes += 1

    # Final evaluation
    print(name, "you are out of tickets. You may leave now. Bye")
    time.sleep(2)
    print("Shutting down Server...")
    time.sleep(2)
    print("Evaluating", name, "...")
    print("Counting score and mistakes...")
    time.sleep(3)

    final_score = evaluate(score, mistakes)

    if 0 < final_score < 5:
        message = f"\033[33mScore {final_score}/10 - {name} disappointed me. -_-\033[0m"  # Gelb
    elif final_score == 10:
        message = f"\033[92mScore {final_score}/10 - {name} is the coolest person ever <3\033[0m"  # Hellgrün
    elif 5 < final_score < 10:
        message = f"\033[36mScore {final_score}/10 - {name} is a cool person <3\033[0m"  # Cyan
    elif final_score <= 0:
        message = f"\033[91mScore {final_score}/10 - {name} how could this even happen...?!?!\033[0m"  # Rot

    for word in message.split():
        print(word, end=' ', flush=True)
        time.sleep(0.3)

    print("\n__________________________________________________________________________________________")


# Entry point
if __name__ == "__main__":
    main()


# Credit: Tutors in the Digital Media Lab <3
