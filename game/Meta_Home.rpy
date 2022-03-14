label meta_home:
    #scene bg meta_homescreen
    #check if running out of power..
    if started_before:
        "Welcome back to the Metaverse! What would you like to do?"
    else:
        "Welcome back to the Metaverse!"
        "It has been a long time since you last logged in ..."
        "What would you like to do?"
    menu:
        "Exit":
            "See you later..."
            return
        "Course Select":
            if action_done_for_day < MAX_ACTIONS_PER_DAY:
                #call course_select
                "<PLALCEHOLDER SCENE>"
            else:
                "You are feeling too tried for the day."
                "Maybe it is time to stop using the device."
            jump meta_home
        "Dating":
            if action_done_for_day < MAX_ACTIONS_PER_DAY:
                #call dating_sim
                "<PLALCEHOLDER SCENE>"
            else:
                "You are feeling too tried for dating."
                "Maybe it is time to stop using the device."
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
    