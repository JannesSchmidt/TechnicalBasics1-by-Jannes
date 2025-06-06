import time

# Important Game variables
inventory = [{"name": "Rope", "type": "tool"}, {"name": "Ice Axe", "type": "tool"}, {"name": "Pill", "type": "healing"}]
MAX_INVENTORY_SIZE = 3
health = 2
MAX_HEALTH = 5
current_room = "Living Room"
escaped = False
bathroom_unlocked = False

# Definition for the beginning
def starting_sequence():
    print("What happened?")
    time.sleep(1)
    print("I know I was climbing a mountain...")
    time.sleep(1.5)
    print("... I must have slipped.")
    time.sleep(1)
    print("But how did I end up here?")
    time.sleep(1)
    print("It looks like a glacier.")
    time.sleep(1)
    print("Shit.")
    time.sleep(1)
    print("I need to find a way out of here.")
    time.sleep(1)
    print("\n <<< You're stuck on a glacier. Ice walls surround you.>>>")
    time.sleep(1)

    while True:
        choice = input("<<< Use 'rope' or 'ice axes'? >>> ").strip().lower()
        if choice == "rope":
            print("<<< You throw the rope... but it doesn't catch on anything.>>>")
            time.sleep(1.5)
        elif choice in ["ice axes", "ice axe", "axes"]:
            print("<<< You use your ice axes to climb up the cold and icy wall... >>>")
            time.sleep(1.8)
            print("<<< You make it to the top and find an old abandoned house. >>>")
            time.sleep(1)
            print("<<< As it's starts snowing and a huge dark cloud aproaches you seek resuce in the house >>>")
            time.sleep(2)
            print("<<< You go through the front door and end up in the living room. >>>\n")
            time.sleep(2)
            print("<<< To see the commands just type 'help'>>>.")
            time.sleep(3)
            break
        else:
            print("<<< Choose either 'rope' or 'ice axes'. >>>")

# Desription for the locations
rooms = {
    "Living Room": {
        "description": "You are in a dusty room with some broken furniture. There is a door to the bathroom and one to the kitchen.",
        "items": [
            {"name": "Axe", "type": "tool"},
            {"name": "old Phone", "type": "tool"}
        ],
        "exits": ["Kitchen", "Bathroom", "Outside"]
    },
    "Bathroom": {
        "description": "It smells like mold. There is a small cabinet here.",
        "items": [
            {"name": "Medicine", "type": "healing"}
        ],
        "exits": ["Living Room"]
    },
    "Kitchen": {
        "description": "An old kitchen food and other stuff is lying around.",
        "items": [
            {"name": "Apple", "type": "food", "good": False},
            {"name": "Bread", "type": "food", "good": False},
            {"name": "Oil", "type": "tool"},
            {"name": "Batteries", "type": "tool"}
        ],
        "exits": ["Living Room"]
    },
    "Outside": {
        "description": "It's freezing! Don't go outside now.",
        "items": [],
        "exits": ["Living Room"]
    }
}

# Help commands
def show_health():
    print("Health:", "❤️" * health, "♡" * (MAX_HEALTH - health))

def show_my_stuff():
    print("\nMy Inventory:")
    if not inventory:
        print(" - Empty")
    else:
        for item in inventory:
            print(" -", item["name"])

def where_am_i():
    print("\nYou are in the", current_room)
    print(rooms[current_room]["description"])
    if rooms[current_room]["items"]:
        print("You see:")
        for item in rooms[current_room]["items"]:
            print(" -", item["name"])
    else:
        print("Nothing to pick up.")
    print("Exits:", ", ".join(rooms[current_room]["exits"]))
    show_health()

# Item Functions
def grab_item(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your bag is already full!")
        return
    for item in rooms[current_room]["items"]:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            rooms[current_room]["items"].remove(item)
            print("Picked up:", item["name"])
            return
    print("Can't find that here.")

def put_down_item(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            print("Dropped:", item["name"])
            return
    print("You don't have that.")

def look_at_item(item_name):
    for item in inventory + rooms[current_room]["items"]:
        if item["name"].lower() == item_name.lower():
            print("Item:", item["name"], "| Type:", item["type"])
            return
    print("Can't find that item.")

def try_to_use(item_name):
    global health, escaped, bathroom_unlocked
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "healing":
                if health < MAX_HEALTH:
                    health = min(MAX_HEALTH, health + 1)
                    print("Took the pill. Feeling a bit better.")
                    inventory.remove(item)
                else:
                    print("You're already at full health.")
            elif item["type"] == "food":
                if item.get("good", True):
                    health = min(MAX_HEALTH, health + 1)
                    print("The food was good!")
                else:
                    health -= 1
                    print("Ugh... that was bad food.")
                    if health <= 0:
                        print("You died from food poisoning.")
                        exit()
                inventory.remove(item)
            elif item["name"].lower() in ["axe", "oil"]:
                open_bathroom(item["name"])
                inventory.remove(item)
            elif item["name"].lower() == "fuel":
                print("You have fuel. Maybe you can power something.")
            elif item["name"].lower() == "old phone":
                print("You combine the old phone with the batteries and manage to call for help!")
                escaped = True
                inventory.remove(item)
            else:
                print("That didn’t do anything.")
            return
    print("You don't have that item.")
def open_bathroom(tool):
    global bathroom_unlocked
    if not bathroom_unlocked:
        print(f"You used the {tool}. You can now enter the Bathroom.")
        bathroom_unlocked = True
    else:
        print("The Bathroom is already open.")

def go_to(room_name):
    global current_room
    if room_name not in rooms[current_room]["exits"]:
        print("You can't go there from here.")
        return
    if room_name == "Bathroom" and not bathroom_unlocked:
        print("The bathroom door won't open. Try using something before trying to enter.")
        return
    if room_name == "Outside":
        print("You went outside... Walked a bit. Lost orientation and you died.")
        exit()
    current_room = room_name
    where_am_i()

# Game Loop
def game_time():
    starting_sequence()
    where_am_i()
    while not escaped:
        command = input("\nWhat now? > ").strip().lower()
        if command == "help":
            print("Commands: look, inventory, pickup [item], drop [item], use [item], examine [item], go [room], quit")
        elif command == "look":
            where_am_i()
        elif command == "inventory":
            show_my_stuff()
        elif command.startswith("pickup "):
            grab_item(command[7:])
        elif command.startswith("drop "):
            put_down_item(command[5:])
        elif command.startswith("use "):
            try_to_use(command[4:])
        elif command.startswith("examine "):
            look_at_item(command[8:])
        elif command.startswith("go "):
            go_to(command[3:].title())
        elif command == "quit":
            print("Did you really just give up?!?!")
            time.sleep(2)
            print("Left in that house to die...")
            break
        else:
            print("Huh? Try 'help' for a list of commands.")

    if escaped:
        print("\n🎉 Help is on the way! Well done ^-^")

if __name__ == "__main__":
    game_time()