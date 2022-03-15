label meta_home:
    #scene bg meta_homescreen
    #check if running out of power..
    if actions_done_for_day >= MAX_ACTIONS_PER_DAY:
        "The battery is too low... cannot continue... shutting down"
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
        # TODO: add text here
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
            call course_select
            $started_before = True
            jump meta_home
            return
        "Read Diary":
            #check if diary is unlocked
            if diary_unlock_level == 0:
                "Due to security precautions, the diary is not available at this time."
            else:
                "<PLALCEHOLDER SCENE>"
                #call diary
            jump meta_home.select
            return
    return
    
