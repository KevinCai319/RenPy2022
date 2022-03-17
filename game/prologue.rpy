
transform screen_top:
    xpos 960
    ypos -1080
label prologue:
    #scene bombing
    #"The sound of the air raid sirens fill the air as an entire town scramble towards the nearest fallout shelter."
    #"In a desolate corner, a child cries out to his parents. But no one hears him."
    #"It's every man for himself now."
    # show irl_background with SLOW_FADE
    # play music "audio/music/Strong-Wind-Blowing.ogg" volume 1.0
    ##scene now
    #"AA (After Apocalypse) Year 52:"
    #"The entire world is decimated."
    #"The memories of the cataclysm remain vivid in your mind and the high pitch wails of the sirens linger in your ears."
    #"Although the fires have long stopped, the sky is still filled with traces of smoke, as though a volcano has just erupted."
    #"There are no more fish in the river, birds in the sky, or fruit on the trees."
    #"Everything around you is a barren wasteland."
    ##scene mainCharacter
    #"As far as you know, your shelter group is the only one that has survived."
    #"The harsh winter is just around the corner and to make matters worse, the shelter is on nearing the end of its food and supply."
    #hide irl_background with fade
    #"But there is hope."

    play music "<from 3>audio/music/prologue.ogg"
    "The fight finally ended."
    "Before the winter, the battle on the wasteland become more and more severe."
    "Food shortage followed by the expanding corruption. Machines people relied on break down one by one, but no one knows how ancient people made it. Let alone fixing it."
    "The only way to survive is to fight each other for the remaining resources."
    "It's every man for himself now."
    stop music fadeout 0.5
    pause 0.5


    scene irl_background with SLOW_FADE
    play music "audio/music/Strong-Wind-Blowing.ogg"
    "AA (After Apocalypse) Year 52:"
    "The food-collecting team was ambushed by the enemy clan."
    show lynx_img at right with fade
    "As the youngest fighter, you killed two enemies and defeated the raid."
    "But there's no glory. All the food was ruined during the fight. Another effortless day."
    "The harsh winter is just around the corner, however, the shelter is on nearing the end of its food and supply."
    "To make matters worse is the condition of the generator. The clan relies on its heat for the freezing climate."
    "As you approached your shelter, the clan chief appeared and called you."

    
    #scene vrDevice
    #show headset at truecenter
    #"A relic of the ancient civilization."
    #"Ever since it's discovery, numerous people have attempted to turn it on, but to no avail."
    #"You are now called upon the chief -- it's your turn to try."
    #hide headset
    #scene throneRoom
    #show chief_room with SLOW_FADE
    #show chief_img at center
    #chief "What's your name?"
    #menu:
    #    "Lynx":
    #        lynx "Lynx"
    #
    #chief "Okay Lynx. Put the device on your head and say, \"Hello meta\". If your voice is a match, then the device shall turn on."
    #
    #"You pick up the device and examine it."
    ##scene vrDevicePutOn
    #
    #menu:
    #    "Say the key word":
    #        jump onlyKeyWord #end program
    #    "You see a button on the side":
    #        call pressButton
    #return

#label onlyKeyWord:
#    lynx "Hello Meta"
#    "You wait in suspense, but the screen remains blank."
#    chief "If it doesn't work, it doesn't work. Thanks for trying."
#    "You leave and think to yourself:"
#    "{i}There must be another way"
#    hide chief_img
#    return
#
#label pressButton:
#    "There seems to be a button on the side."
#    menu:
#        "Say the key word and press the button.":
#            "You secrelty place your hand on the button. Fortunately, it's on the side facing away from the chief."
#    "*click*"
#    "You put on the headset. It is quite bulky."
#    hide chief_room with FAST_FADE 
#    hide chief_img
#    lynx "Hello Meta"
#    "You wait in suspense, but the screen doesn't respond."
#    chief "If it doesn't work, it doesn't work."
#    "You grudingly take the device off of your head...and"
#    show chief_room
#    show chief_img at right"
#    #scene vrDeviceOn
#    show headset_glowing at truecenter
#    "To everyone's surprise, the screen turns on."
#    chief "Oh! So you are the one."
#    chief "Tell me what you see."
#    hide headset_glowing
#    hide chief_img
#    hide chief_room with FAST_FADE 
#    "You put the device back on."
#    call meta_home
#    #since it is first run through, make fade a bit more slow.
#    show chief_room with SLOW_FADE
#    show chief_img at right
#    #continue conversation with chief
#    chief "Welcome back, [MC], what did you see?"
#    call end_day.summary
#    return
    scene chief_room
    show chief_img at center
    with SLOW_FADE
    chief "What's your name?"
    menu:
        "Lynx":
            pass
    chief "Lynx...Now you are 18. It's time to see if you will be the one chosen by metaverse"
    show lynx_img at right with moveinright
    lynx "Metaverse. What is that?"
    chief "It's a place worshiped by ancient people."
    chief "It's a place where they create."
    chief "It's where they create food that cannot be eaten."
    chief "It's where they create weapons that cannot harm enemies."
    chief "It's where they create shelters that cannot keep you warm through the winter."
    menu:
        "Then it's totally useless. I don't want to go to the metaverse.":
            chief "No, you don't understand ancient people."
            chief "Their power comes from creation."
        "So that's the purpose of metaverse?":
            chief "Creation"
    chief "Lynx, listen. Deep inside the metaverse lies knowledge of how ancient technologies are created."
    lynx "Does it means we can know how to fix the generator and make ancient firearms?"
    chief "Yes. Lynx, you are always so quick to learn."
    menu:
        "Then what's to wait? Let's go to the metaverse.":
            pass
        "Has anyone explored the metaverse yet?":
            pass
    chief "No one has been to that place yet."
    chief "The metaverse chose people by their voice. Only with the chosen voice can one activate the metaverse."
    show chief_img at left
    with easeinright
    chief "Lynx, follow my instructions. Put the device on your head and say, \"Hello meta\"."
    hide lynx_img
    show headset:
        xalign 0.5 yalign 0.6
    "You pick up the device and examine it."
    "The finish on the device is as smooth as silk, there are no visible stitches. Perfect, just like other the other ancient artifacts.\n But at the right side of the device, there is a small bulge."
label meta_activation:
    chief "Don't touch anything. Just say the word."
    menu:
        "Say the keyword":
            show blank at truecenter
            with moveintop
            "You put the device onto your head. It's dark inside."
            lynx "Hello Meta"
            "..."
            ".."
            "."
            "Nothing happens. You wonder if the machine is broken. Wait. If it is just a machine, like other machines such as the generator, then there must be a ..."
            chief "It seems you are not the chosen one. Thank you for trying."
            menu:
                "Give up":
                    return
                "Wait, let me try again.":
                    show blank at screen_top
                    with moveinbottom
                    
                    jump meta_activation
        "Touch the button":
            jump meta_activation_success
label meta_activation_success:
    show blank at truecenter
    with moveintop
    "You put the device onto your head. It's dark inside."
    lynx "Hello Meta"
    "At the same time, you secretly place your hand on the button. Fortunately, it's on the side facing away from the chief."
    "*click*"
    call meta_home
    jump first_end_day
            
label first_end_day:
    #since it is first run through, make fade a bit more slow.
    scene chief_room
    show chief_img at right
    show lynx_img at left
    with SLOW_FADE
    #continue conversation with chief
    chief "Welcome back, [MC], what did you see?"
    call end_day.summary
    return 
