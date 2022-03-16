label meta_home:
    #check if first time launching or not.
    if not started_before:
        #special case, so we can easily have the character remove helemet without much code.
        if actions_done_for_day == 0:
            window hide
            play sound "audio/VR_startup.ogg"
            show blank
            show WHITE with Dissolve(2.0)
            show blank with Dissolve(1.5)
        show meta_room with fade
    else:
        scene meta_room with fade

    #check if running out of power..
    if actions_done_for_day >= MAX_ACTIONS_PER_DAY:
        "The battery is too low... cannot continue... shutting down"
        if not started_before:
            $started_before = True
        return
    stop sound
    play music "audio/music/Yumemi_Room.ogg"
    if started_before:
        "Welcome back to the Metaverse, [MC] !"
    else:
        "Welcome back to the Metaverse, It has been a long time since you last logged in ..."
        "..."
        "......"
        "........."
        "...[MC] !"
        yumemi "Huh? Who's [MC]?"

        "Small pixels on the screen materialize, and you make out a brightly open space."
        "Standing in front of you are three animals in the purest of white."
        "The elephant in the room catches your attention; {i}but why is it so small?" # a pun 
        "An unfamiliar feeling of peace and freedom falls upon you as you take in the serene atmosphere of the room."
        yumemi "Is this what they call heaven?"
        yumemi "No, this can't be."
        "You feel for the head straps and take the headset off."
        $renpy.music.set_pause(True)
        hide meta_room
        hide WHITE
        pause 0.75
        show blank at screen_top
        with moveinbottom
        pause 1.25
        show blank at truecenter
        with moveintop
        scene meta_room with enter_meta
        $renpy.music.set_pause(False)
        yumemi "{i}Okay, I'm still alive."
        "You decide to walk around a bit and investigate the room further."
        yumemi "Everything is so pink and jovial."
        "The bookshelf seems intriguing. You approach it with anticipation."
        "..."
        "Most of the books seem standard, but you pick up one up anyway."
        "Opening the cover, you see the name again:."
        show mc_img at center
        with fade
        "{b}{i}[MC]"
        hide mc_img
        with fade
        yumemi "[MC]. So this is [MC]'s VR headset. This is [MC]'s world. This is [MC]'s room."
        yumemi "I {i}am{/i} [MC]! And this must be the metaverse."

        "You turn your head towards the right and see an odd reflection in the mirror."
        "Who is that?"
        "As you approach mirror, you see a girl wearing a bowtie staring back at you."
        show mirror with fade
        yumemi "Is that me?"
        yumemi "Hold on, I am a girl?"
        yumemi "I HAVE TO PRETEND TO BE A GIRL?"
        "{i}**well Lynx, you are the chosen one"

        yumemi "Okay...then."
        "You scrutinize yourself for a bit longer."
        yumemi "You know what? I can live with this."
        hide mirror with fade

        "You shift your gaze to the two doors at the end of the room"
        "Where do they lead to?"
        "You open the one on the left"
        "..."
        "It's an empty closet."
        yumemi "{i}That's weird."
        "You close it and go through the other door."
        "..."

    label .select:
        "What would you like to do?"
        if not started_before:
            yumemi "Oh?"
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
        # "Read Diary":
        #     #check if diary is unlocked
        #     if diary_unlock_level == 0:
        #         "Due to security precautions, the diary is not available at this time."
        #         jump meta_home.select
        #     else:
        #         hide meta_room with fade
        #         "<PLALCEHOLDER SCENE>"
        #         #call diary
        #     jump meta_home
        #     return
    return
