# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("sylvie")

define g = Character("eileen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sylvie blue normal:
        xalign 0.75
        yalign 1.0

    show eileen happy:
        xalign 0.0
        yalign 1.0

    # Start by playing some music.
    play music "illurock.opus"

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    g "interjecting into convo"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    g "talk talk talk"

    e " This is a testing point for new dialogue options"

    # This ends the game.

    return
