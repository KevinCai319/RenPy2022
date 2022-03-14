label meta_home:
    #scene bg meta_homescreen
    #check if running out of power..
    if actions_done_for_day >= MAX_ACTIONS_PER_DAY:
        "The battery is too low... cannot continue... shutting down"
        if started_before:
            $started_before = True
        return
    
    if started_before:
        "Welcome back to the Metaverse! What would you like to do?"
    else:
        "Welcome back to the Metaverse, "
        "It has been a long time since you last logged in ..."
        "What would you like to do?"
    label .select:
    menu:
        "Exit":
            if started_before:
                "Hey! Time is precious, don't waste it!"
            else:
                "You should probably check out what the device does."
            jump select
        "Course Select":
            call course_select
            jump meta_home
        "Read Diary":
            #check if diary is unlocked
            if diary_unlock_level == 0:
                "Due to security precautions, the diary is not available at this time."
            else:
                "<PLALCEHOLDER SCENE>"
                #call diary
            jump meta_home
    return
    