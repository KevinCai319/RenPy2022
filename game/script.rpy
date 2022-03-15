

# a bit too obvious that we are copying lol

define MC_str = "yumemi"
default MC = MC_str
define yumemi = Character(MC_str)
define david = Character("David Sigmund")
define lynx = Character("Lynx")
define chief = Character("chief")


# World Variables
default day = 0
#lose(0/1)/good(2)/best ending(3) (0/1/2/3)
default end_state = 0
#TODO: add a time where winter starts.
default WINTER_DAY = 16
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

#Course objects
default animalBehaviorAndWelfare = Course("Animal Behavior and Welfare","animal_course", 5, 4, animal_course_content, True, "Not sure how much I'll get out of this...")
default englishPoetry = Course("English Poetry","english_course", english_course_content, 8, 4, True)
default circuitsAndElectronics = Course("Circuits and Electronics","circuits_course", circuits_course_content, 10, 9, True)
default electricEngeering = Course("Electric Engineering","ee_course", 16, 14, ee_course_content, True, "Electrical engineering can be helpful for fixing things...")
default socialMediaMarketing = Course("Social Media Marketing","media_course", 12, 1, media_course_content, True)
default cadAndDigital = Course("CAD And Digital", "cad_course", 12, 10, cad_course_content, True)
default calc1 = Course("Calculus I", "math1_course",10, 10, math1_course_content, True)
default calc2 = Course("Calculus II", "math2_course",10, 10, math2_course_content, False)
default calc3 = Course("Calculus III", "math3_course",10, 10, math3_course_content, False)
default theoreticalPhysics = Course("Introduction to Theoretical Physics", "physics_course",10, 10, physics_course_content, True)
default modernChem = Course("Modern Chemistry","chem_course", 8, 8, chem_course_content, True)
default foodAndBeverage = Course("Food & Beverage Management","food_course", 9, 7, food_course_content, True)

# The game starts here.
label start:
    call prologue
    call day_reset
    label .day_cycle:
        call day_start
        "Time to login"
        call meta_home
        "I think it's time to report to chief."
        call end_day
        #scene transition
        call day_reset
        jump start.day_cycle
    return
#Day end, reset
label day_reset:
    $power_left-=1
    if power_left <= 0:
        #game over!
        "<GAME OVER SCENE>"
        return
    else:
        #reset battery life of device.
        $actions_done_for_day = 0
        $daily_summary = ""
        $day+=1
    "The sun rises again... DAY [day]"
    return
label game_end:
    if end_state < 2:
        "DEAD"
    elif end_state == 2:
        "OK ENDING"
    else:
        "GOOD ENDING, GOOD JOB"
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
