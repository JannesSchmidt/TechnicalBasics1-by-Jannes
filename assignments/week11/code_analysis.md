
### Where I found it and why:
    - I found the code here: https://github.com/itspyguru/Python-Games/blob/master/Cave%20Story/main.py
    - I chose it, because I was surprised on what the possibilities with pygame are (far beyond my first thoughts).

### What does it do?:
    Uses pygame for game graphics and input.
    Loads external modules like:
    World, Player, Portal, and button logic from objects.py.
    More in the step by step analysis.


## Function analysis:
### What does it do?:
    It's a platform puzzle game where a player tries to reach a portal.
    The game supports multiple levels, a replay option, and touch-based movement with button overlays.
    It features background music, sound effects, and a win screen.
### What are the inputs and outputs?:
    pressed_keys: list of booleans for movement directions: [Up, Down, Left, Right].
    game_over: current game over state.
    Returns True if the player is "dead" or the game ends, otherwise False.
### How does it work (step by step)?:
    After importing pygame and pickle the games gets initialized.
    The screen size, framerate and other things like images/assets are being defined.
    Buttons are being set as images in the screen, by being linked with images.
    After importing and defining, the code continues with variables.
    Additionally, a dictionary is created to check if the player clicked on a directional button.
    After defining the sprite groups (like diamonds, spikes, plants, etc.), they are added to a list called groups.
    The game then loads the current level data using load_level() and gets the player's and portal's positions using game_data().
    The world, player, and portal objects are created and added to the screen using the previously loaded data.
    A set of Boolean variables is defined to track the state of the game, such as whether it has started, if the player won or lost, and whether the replay menu is open.
    The game loop starts by drawing the background image.
    All sprite groups (like spikes or diamonds) are drawn to the screen, followed by the world map.
    If the game hasn’t started yet, it displays the intro image. Once the play button is clicked, the game begins.
    If the player has already won, a win image is shown instead of the gameplay.
    Otherwise, the movement button image is drawn on the screen and slightly moves back and forth to attract attention.
    The code then checks for mouse events.
    If the mouse is pressed inside any of the directional buttons, the corresponding pressed_keys entry is set to True.
    When the mouse is released, all keys are reset to False.
    Next, the portal is updated visually, and the player is moved based on the pressed_keys.
    If the player hits a trap or loses, the game switches to the replay menu.
    If the player reaches the portal and is in the right position, the next level is loaded (unless the final level was completed, in which case the win screen is triggered).
    When in the replay menu, the player can choose to quit, toggle sound, or replay the current level.
    

## Key Takeaways for my own assignment:
    I really like the  thought of using the mouse to click on directional buttons,
    which is why I will probaly get "inspired" why this  block of code:
    			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				if show_keys:
					if dir_dict["Up"].collidepoint(pos):
						pressed_keys[0] = True
					if dir_dict["Down"].collidepoint(pos):
						pressed_keys[1] = True
					if dir_dict["Left"].collidepoint(pos):
						pressed_keys[2] = True
					if dir_dict["Right"].collidepoint(pos):
						pressed_keys[3] = True
    SOund and animation is cool, but too much, but this code definetly gave me some ideas to work with...
## What was confusing or difficult to understand?:
    The use of many external modules like World, Player, Portal from objects.py — initially I didn't know what each one was responsible for.
    pressed_keys looked like it came from a keyboard, but it's actually for touch/click zones mapped to directions.
    The way collisions with the portal were checked: it's based on both rectangle collision and player position within portal bounds.