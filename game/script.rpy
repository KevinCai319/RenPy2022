

# a bit too obvious that we are copying lol

define MC_str = "yumemi"
default MC = MC_str
define yumemi = Character(MC_str)
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
default daily_summary = ""
default course = 0

#Course variables
default animalBehaviorAndWelfare = Course("Animal Behavior and Welfare","animal_course", 5, 4, True)
default englishPoetry = Course("English Poetry","english_course", 8, 4, True)
default circuitsAndElectronics = Course("Circuits and Electronics","ee_course", 20, 18, True, "Electrical Engineering seems pretty useful...")
default socialMediaMarketing = Course("Social Media Marketing","media_course", 12, 1, True)
default cadAndDigital = Course("cadAndDigital","CAD_course", 20, 18, True)


# The game starts here.
label start:
    jump course_select
    return
#Day end, reset 
label day_end:
    $power_left-=1
    if power_left <= 0:
        #game over!
        "<GAME OVER SCENE>"
        return
    else:
        #reset battery life of device.
        $actions_done_for_day = 0
        $daily_summary = ""
    "The sun rises again... DAY [day]"
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
