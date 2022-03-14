

# a bit too obvious that we are copying lol
define yumemi = Character("yumemi")
define david = Character("David Sigmund")
define lynx = Character("Lynx")
define chief = Character("chief")


# World Variables
default day = 0
#TODO: add a time where winter starts.
default WINTER_DAY = 10
# Generator Variables
default power_left = 100
default generator_success = False
default purifier_success = False
default weapons_success = False
# Values stored in Meta device.
default started_before = False
default diary_unlock_level = 0
default actions_done_for_day = 0
default MAX_ACTIONS_PER_DAY = 2

#Course objects
default animalBehaviorAndWelfare = Course("Animal Behavior and Welfare", 5, 4, True)
default englishPoetry = Course("English Poetry", 8, 4, True)
default circuitsAndElectronics = Course("Circuits and Electronics", 20, 18, True)
default socialMediaMarketing = Course("Social Media Marketing", 12, 1, True)
default cadAndDigital = Course("CAD And Digital", 20, 18, True)
default calc1 = Course("Calculus I", 100, 100)
default calc2 = Course("Calculus II", 100, 100)
default calc3 = Course("Calculus III", 100, 100)
default theoreticalPhysics = Course("Introduction to Theoretical Physics", 10, 10)
default modernChem = Course("Modern Chemistry", 10, 9)
default foodAndBeverage = Course("Food & Beverage Management", 9, 7)
default diplomacy = Course("Diplomacy in the Modern World", 12, 9)
default romanArch = Course("Roman Architecture", 4, 4)


# The game starts here.
label start:
    $ animalBehaviorAndWelfare.progressClass(3)
    "[animalBehaviorAndWelfare.currentClass]"
    jump prologue
    return
#Day end, reset
label day_end:
    $power_left-=1
    if power_left <= 0:
        #game over!
        "<GAME OVER SCENE>"
    else:
        #reset battery life of device.
        actions_done_for_day = 0;
    return
    #rest of this is demo code for future reference.
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # # This shows a character sprite. A placeholder is used, but you can
    # # replace it by adding a file named "eileen happy.png" to the images
    # # directory.

    # show Hoshino Yumemi happy at left

    # # These display lines of dialogue.

    # Yumemi "Hey, this is a test for branching in the game. "

    # Lynx "Cool. So what should I do?"
    # #local jump.
    # label .loop:
    # Yumemi "If you want to exit the game right now, feel free to. Just select 1, otherwise choose 2."

    # menu:
    #     "1":#note:call does a jump(pushes function choose_end onto stack, and once it is done, go back here.)
    #         call choose_end
    #     "2":
    #         jump choose_continue
    # show Hoshino Yumemi at center
    # Yumemi "Bye."
    # return

#implies local scope.
# label choose_end:
#     Yumemi "Hey, you eneded the game! You pressed the button [value] times!"
#     return

# label choose_continue:
#     show Hoshino Yumemi happy at right with dissolve
#     Yumemi "You have chosen to continue... value has increased by 1.."
#     $value += 1
#     #loop is within the scope of start, so use start.loop
#     jump start.loop
#     return
