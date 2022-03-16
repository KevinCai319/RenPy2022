
label prologue:
    #scene bombing
    "The sound of the air raid sirens fill the air as an entire town scramble towards the nearest fallout shelter."
    "In a desolate corner, a child cries out to his parents. But no one hears him."
    "It's every man for himself now."
    show irl_background with SLOW_FADE
    play music "audio/music/Strong-Wind-Blowing.ogg"
    #scene now
    "AA (After Apocalypse) Year 22:"
    "The entire world is decimated."
    "The memories of the cataclysm remain vivid in your mind and the high pitch wails of the sirens linger in your ears."
    "Although the fires have long stopped, the sky is still filled with traces of smoke, as though a volcano has just erupted."
    "There are no more fish in the river, birds in the sky, or fruit on the trees."
    "Everything around you is a barren wasteland."
    #scene mainCharacter
    "As far as you know, your shelter group is the only one that has survived."
    "The harsh winter is just around the corner and to make matters worse, the shelter is on nearing the end of its food and supply."
    hide irl_background with fade
    "But there is hope."
    stop music fadeout 1.0
    #scene vrDevice
    show headset at truecenter
    "A relic of the ancient civilization."
    "Ever since it's discovery, numerous people have attempted to turn it on, but to no avail."
    "You are now called upon the chief -- it's your turn to try."
    hide headset
    #scene throneRoom
    show chief_room with SLOW_FADE
    show chief_img at center
    chief "What's your name?"
    menu:
        "Lynx":
            lynx "Lynx"

    chief "Lynx...ID 114 171 156 170"
    chief "Okay Lynx. Put the device on your head and say, \"Hello meta\". If your voice is a match, then the device shall turn on."
    
    "You pick up the device and examine it."
    #scene vrDevicePutOn

    menu:
        "Say the key word":
            jump onlyKeyWord #end program
        "You see a button on the side":
            call pressButton
    return

label onlyKeyWord:
    lynx "Hello Meta"
    "You wait in suspense, but the screen remains blank."
    chief "If it doesn't work, it doesn't work. Thanks for trying."
    "You leave and think to yourself:"
    "{i}There must be another way"
    hide chief_img
    return

label pressButton:
    "There seems to be a button on the side."
    menu:
        "Say the key word and press the button.":
            "You secrelty place your hand on the button. Fortunately, it's on the side facing away from the chief."
    "*click*"
    "You put on the headset. It is quite bulky."
    hide chief_room with FAST_FADE 
    hide chief_img
    lynx "Hello Meta"
    "You wait in suspense, but the screen doesn't respond."
    chief "If it doesn't work, it doesn't work."
    "You grudingly take the device off of your head...and"
    show chief_room
    show chief_img at right
    #scene vrDeviceOn
    "To everyone's surprise, the screen turns on."
    chief "Oh! So you are the one."
    chief "Tell me what you see."
    hide chief_img
    hide chief_room with FAST_FADE 
    call meta_home
    #since it is first run through, make fade a bit more slow.
    show chief_room with SLOW_FADE
    show chief_img at right
    #continue conversation with chief
    chief "Welcome back, [MC], what did you see?"
    call end_day.summary
    return
