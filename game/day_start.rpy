label day_start:
    show irl_background 
    show lynx_img at left with fade
    play music "audio/music/Strong-Wind-Blowing.ogg"
    lynx "It's a start of a new day. Better go visit Chief again."

    "{i} You make your daily trip to the chief's place.{\i}"

    if WINTER_DAY-day < 3:
        lynx "Brrrr... It's pretty chilly today, I'm not sure how things will turn out..."
    elif WINTER_DAY-day <= 5:
        lynx "... It's a bit colder than usual"
    else:
        lynx "..."
    stop music
    hide lynx_img
    hide irl_background
    show chief_room
    show chief_img at left
    #<Lynx arrives at the Chief's place>
    show lynx_img at right with fade
    lynx "Hello chief, how are you today?"

    #Chief gives additional text based on the day.
    if day == 2:
        chief "It gets colder and colder, but the only generator the tribe relies on doesn't sound good. Please find a way to fix this, or else our tribe might not last much longer."
        $goal_generator = True
    elif day == 3:
        chief "Our tribe has lost people due to a conflict with another tribe. Things are starting to look grim."
    elif day == 4:
        chief "Our water purifer has broken down. People were sent to find other water sources, but they were ambushed. We do not know how to fix the purifier."
        $goal_purifier = True
    elif day == 5:
        chief "Not good. We are running out of food. We need weapons to hunt for food, and defend our tribe."
        $goal_weapons = True
    else: 
        # if 0 out of 3 are done
        #end state is how many of the goals you finished
        #all this text you can change since I am not good writer
        if end_state == 0 :
            if day < ((WINTER_DAY-day) * 0.8):
                chief "Doing fine. keep up the good work."
            else:
                chief "How have you not gotten anything done!?"
        elif end_state == 1:
            if day < ((WINTER_DAY-day) * 0.75):
                chief "Doing well"
            else:
                chief "Doing alright, keep up the good work."
        else:
            # in this case already done 2/3, so you technically already won something.
            chief "Doing great, hope you're doing well."
        
    chief "It's time to enter the Metaverse."
    hide lynx_img 
    hide chief_img
    hide chief_room
    show headset_glowing at truecenter with fade
    #scene vrDevice
    lynx "Hello Meta"
    hide headset_glowing
    "*click*"
    return