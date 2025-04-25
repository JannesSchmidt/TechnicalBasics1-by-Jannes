import random
import time

print("Hi, if you are ready to see the weather forecast \nLet's see what you'll get.")
time.sleep(1)
width = None
while width is None:
    try:
        input1 = int(input("Enter the device screen width (12-40): "))
        if 12 <= input1 <= 40:
            width = input1
        else:
            print("Value must be between 12 and 40.")
    except ValueError:
        print("Please enter a number.")

height = None
while height is None:
    try:
        input2 = int(input("Enter the screen height (4-20): "))
        if 4 <= input2 <= 20:
            height = input2
        else:
            print("Value must be between 4 and 20.")
    except ValueError:
        print("Please enter a number.")

device = input("Choose your device ('tv' or 'phone'): ").strip().lower()
if device not in ['tv', 'phone']:
    print("Invalid choice. Defaulting to 'phone'.")
    device = 'phone'

temp_range = list(range(-10, 41))
emoji_list = ['☀️', '🌧️', '⛅', '🌩️', '❄️']
current_temp = random.choice(temp_range)
current_emoji = random.choice(emoji_list)
weather = f"{current_temp}°C {current_emoji}".center(width)

screen = ["┌" + "─" * width + "┐"]
for i in range(height):
    line = weather if i == height // 2 else " " * width
    screen.append("│" + line + "│")
screen.append("└" + "─" * width + "┘")

device_output = []

if device == 'tv':
    antenna = " " * (width // 2) + "╲╱"
    top = " " * ((width - 6) // 2) + "╭" + "═" * 6 + "╮"
    legs = " " * (width // 2 - 2) + "/" + " " * 4 + "\\"
    base = " " * (width // 2 - 3) + "/" + "_" * 6 + "\\"
    device_output = [antenna, top] + screen + [legs, base]

elif device == 'phone':
    phone_top = " " + "_" * width
    phone_bottom = "|" + " " * ((width - 1) // 2) + "◯" + " " * ((width - 1) // 2) + "|"
    device_output = [phone_top] + screen + [phone_bottom]

[print(line) for line in device_output]

if current_emoji == '☀️':
    print("Looks like today will be sunny.")
    time.sleep(1.5)
    if current_temp <= 0:
        print("Sadly you should bring a warm jacket.")
    elif 1 <= current_temp <= 14:
        print("So close to a comfortable weather.")
    elif 15 <= current_temp <= 25:
        print("Perfect to wear a T-Shirt.")
    elif current_temp >= 26:
        print("BE AWARE OF POSSIBLE HEAT STROKES!!!")

elif current_emoji == '🌧️':
    print("It's going to rain today.")
    time.sleep(1.5)
    if current_temp <= 0:
        print("Cold and wet — dress warmly and stay dry.")
    elif 1 <= current_temp <= 14:
        print("Don't forget an umbrella and a jacket.")
    elif 15 <= current_temp <= 25:
        print("A light raincoat will do.")
    elif current_temp >= 26:
        print("Very warm rain — still, bring an umbrella!")

elif current_emoji == '⛅':
    print("Partly cloudy skies today.")
    time.sleep(1.5)
    if current_temp <= 0:
        print("Bundle up, it's chilly under those clouds.")
    elif 1 <= current_temp <= 14:
        print("Mild but not warm — a light jacket should work.")
    elif 15 <= current_temp <= 25:
        print("What a nice day to be outside!")
    elif current_temp >= 26:
        print("Don't get fooled by the clouds. It's gonna get hot!")

elif current_emoji == '🌩️':
    print("Stormy weather ahead.")
    time.sleep(1.5)
    if current_temp <= 0:
        print("Stay indoors if you can — it’s freezing and stormy.")
    elif 1 <= current_temp <= 14:
        print("Risky weather, dress warm and stay safe.")
    elif 15 <= current_temp <= 25:
        print("Not too cold, but be cautious of lightning.")
    elif current_temp >= 26:
        print("Stormy and hot — a rare and dangerous combo.")

elif current_emoji == '❄️':
    print("Snow is falling today.")
    time.sleep(1.5)
    if current_temp <= 0:
        print("Perfect weather for snow, dress very warmly!")
    elif 1 <= current_temp <= 14:
        print("Snow with a bit of melt — could get slushy.")
    elif 15 <= current_temp <= 25:
        print("Unusual for snow — might just be cold rain.")
    elif current_temp >= 26:
        print("Snow? At this temperature??? Please don't ask me how and why...")