# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# a bit too obvious that we are copying lol
define Yumemi = Character("Hoshino Yumemi")

define David = Character("David Sigmund")
define Lynx = Character("Lynx")
default value = 0
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Hoshino Yumemi happy at left

    # These display lines of dialogue.

    Yumemi "Hey, this is a test for branching in the game. "

    Lynx "Cool. So what should I do?"
    #local jump.
    label .loop:
    Yumemi "If you want to exit the game right now, feel free to. Just select 1, otherwise choose 2."

    menu:
        "1":#note:call does a jump(pushes function choose_end onto stack, and once it is done, go back here.)
            call choose_end
        "2":
            jump choose_continue
    show Hoshino Yumemi at center
    Yumemi "Bye."
    return
    
#implies local scope.
label choose_end:
    Yumemi "Hey, you eneded the game! You pressed the button [value] times!"
    return 

label choose_continue:
    show Hoshino Yumemi happy at right with dissolve
    Yumemi "You have chosen to continue... value has increased by 1.."
    $value += 1
    #loop is within the scope of start, so use start.loop
    jump start.loop
    return