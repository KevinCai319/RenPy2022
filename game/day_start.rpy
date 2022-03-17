label day_start:
    scene irl_background 
    
    show lynx_img at left
    with fade
    play music "audio/music/Strong-Wind-Blowing.ogg"
    lynx "A new day starts. Better go visit Chief again."

    "{i}You make your daily trip to the chief's place.{\i}"

    if WINTER_DAY-day < 3:
        lynx "Brrrr... It's pretty chilly today, I hope we will be prepared soon."
    elif WINTER_DAY-day <= 5:
        lynx "... It's a bit colder than usual"
    else:
        lynx "..."

    #<Lynx arrives at the Chief's place>
    scene chief_room
    show chief_img at left
    show lynx_img at right
    with fade
    lynx "Hello chief, how are you today?"

    #Chief gives additional text based on the day.
    if day == 2:
        chief "The days are growing colder but the only generator the tribe relies on doesn't sound good."
        chief "Find a way to fix it, or our tribe might not last much longer."
        $goal_generator = True
    elif day == 4:
        chief "We have been invaded by a neighboring tribe and have lost many people."
        chief "We mustn't let our tribe fall into the hands of the enemy the next time an invasion occurs."
        chief "Find a way to construct more potent weapons so that we may better defend ourselves."
        $goal_weapons = True
    elif day == 6:
        chief "I have just receieved news that our water purifier has broken down."
        chief "I therefore sent out a reconnaissance team to evaluate the extent of the issue, but they have been ambushed."
        chief "Thankfully, one of the members made it back and he told us that there is an issue with the circuitry."
        chief "As you may know, clean water is absoultely essential to our survival. Find a way to repair the purifier."
        $goal_purifier = True
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
    show headset_glowing at truecenter with fade
    chief "It's time to enter the Metaverse."
    hide headset_glowing
    stop music
    show blank at truecenter with moveintop
    #scene vrDevice
    lynx "Hello Meta"
    hide headset_glowing
    "*click*"
    return