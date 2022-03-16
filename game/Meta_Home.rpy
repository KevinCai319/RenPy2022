label meta_home:
    #scene bg meta_homescreen
    #check if running out of power..
    show meta_room with fade
    if actions_done_for_day >= MAX_ACTIONS_PER_DAY:
        "The battery is too low... cannot continue... shutting down"
        hide meta_room with fade
        if not started_before:
            $started_before = True
        return

    if started_before:
        "Welcome back to the Metaverse, [MC] !"
    else:
        "Welcome back to the Metaverse, It has been a long time since you last logged in ..."
        "..."
        "......"
        "........."
        "...[MC] !"
        "Small pixels on the screen materialize ot life, and you make out a bright enclosed space."
        "What am I seeing?"
        "Standing in front of you are three animals in front you in the purest of white."
        "The elephant in the room catches your attention; {i}but why is it so small?" # a pun 
        "An unfamiliar feeling of peace and rest falls upon you as you take in the room further."
        "Is this what they call heaven?"
        "No, this can't be."
        "You feel for the head straps and take the headset off."
        #switch scene to chief for and then on next click, switch back to the VR room
        show 

        # He's a girl now, am I in heaven? How do I
    label .select:
        "What would you like to do?"
    menu:
        "Exit":
            if started_before:
                "Hey! Your time here is {i}precious{/i}, don't waste it!"
            else:
                "You should probably check out what the device does before leaving."
            jump meta_home.select
            return
        "Course Select":
            #Go to course select screen.
            hide meta_room with fade
            call course_select
            $started_before = True
            jump meta_home
            return
        "Read Diary":
            #check if diary is unlocked
            if diary_unlock_level == 0:
                "Due to security precautions, the diary is not available at this time."
                jump meta_home.select
            else:
                hide meta_room with fade
                "<PLALCEHOLDER SCENE>"
                #call diary
            jump meta_home
            return
    return
