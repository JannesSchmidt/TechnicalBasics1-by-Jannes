import random
import time

# Adding in the Art
ascii_art_library = {
    "Dog": r"""
   ,_____ ,
  ,._ ,_. 7\
 j `-'     /
 |o_, o    \
.`_y_`-,'   !
|/   `, `._ `-,
|_     \   _.'*\
  >--,-'`-'*_*'``---.
  |\_* _*'-'         '
 /    `               \
 \.         _ .       /
  '`._     /   )     /
   \  |`-,-|  /c-'7 /
    ) \ (_,| |   / (_
   ((_/   ((_;)  \_)))       -nabis
""",
    "Cat": r"""
 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
""",
    "Elephant": r"""
Art by Joan G. Stark
                        _
                      .' `'.__
                     /      \ `'""-,
    .-''''--...__..-/ .     |      \
  .'               ; :'     '.  a   |
 /                 | :.       \     =\
;                   \':.      /  ,-.__;.-;`
/|     .              '--._   /-.7`._..-;`
; |       '                |`-'      \  =|
|/\        .   -' /     /  ;         |  =/
(( ;.       ,_  .:|     | /     /\   | =|
 ) / `\     | `""`;     / |    | /   / =/
   | ::|    |      \    \ \    \ `--' =/
  /  '/\    /       )    |/     `-...-`
 /    | |  `\    /-'    /;
 \  ,,/ |    \   D    .'  \
jgs `""`   \  nnh  D_.-'L__nnh
""",
    "Owl": r"""
, _ ,
( o o )
/'` ' `'\\
|'''''''|
|\\'''//|
   HHH
""",
    "Dolphin": r"""
                                       .--.
                _______             .-"  .'
        .---u"""       """"---._  ."    %
      .'                        "--.    %
 __.--'  o                          "".. "
(____.                                  ":
 `----.__                                 ".
         `----------__                     ".
               ".   . ""--.                 ".
                 ". ". bIt ""-.              ".
                   "-.)        ""-.           ".
                                   "".         ".
                                      "".       ".
                                         "".      ".
                                            "".    ".
                      ^~^~^~^~^~^~^~^~^~^~^~^~^"".  "^~^~^~^~
                                            ^~^~^~^  ~^~
                                                 ^~^~^~
"""
}

# as a random and surprising effect
def generate_ascii_art(rows, cols, hspace=5, vspace=2):
    stolen_number = random.randint(1, 7)
    if stolen_number == 7:
        print("\nOh no! The art has been stolen. Sorry.")
        print(" :(")
        return

    animals = list(ascii_art_library.keys())
    selected_animal = random.choice(animals)
    # So that the art is also random.
    print(f"\nGenerating your art with the animal: {selected_animal}")
    time.sleep(1)
    art_lines = ascii_art_library[selected_animal].strip().split('\n')
    num_art_rows = len(art_lines)
    # Drawing as many animals as the User decides later on.
    for i in range(rows):
        for j in range(num_art_rows):
            line_to_print = ""
            for k in range(cols):
                line_to_print += art_lines[j] + (" " * hspace)
            print(line_to_print)
        print("\n" * vspace)  


print("Welcome to the interactive ASCII Art Generator!")
print("Create a grid of animals by entering some parameters.")
print("-------------------------------------------------------")
# User input time:
rows_input = None
while rows_input is None:
    try:
        rows_input = int(input("Enter the number of rows (1-3): "))
        if not 1 <= rows_input <= 3:
            print("Please enter a number between 1 and 3.")
            rows_input = None
    except ValueError:
        print("Invalid input. Please enter a whole number.")

cols_input = None
while cols_input is None:
    try:
        cols_input = int(input("Enter the number of columns (1-3): "))
        if not 1 <= cols_input <= 3:
            print("Please enter a number between 1 and 3.")
            cols_input = None
    except ValueError:
        print("Invalid input. Please enter a whole number.")

generate_ascii_art(rows_input, cols_input)
