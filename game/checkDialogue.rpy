label waterMilestone2FixAttemptFail:
    chief "That is exceptional news! Why don't you go and give it a try."
    "With a toolkit in hand, you and the chief approach the purifier"
    scene Water_Purifier_damaged
    show chief_img at right
    show lynx_img at left
    with fade
    play music fixing
    lynx "There seems to be a wiring issue that is causing the outputs to not register correctly within the computer."
    "After reconfiguring the wires, you find that the problem was much simpler."
    "Due to the nature of the machinery progressing through new updates, the CPU was no longer able to handle the stress."
    lynx "Chief, the problem is not what I had anticipated. The current computer handeling the processes is no longer fit for the work."
    lynx "We will need a stronger CPU."
    "But where do you find one?"
    "The CPU currently fitted to this purifier is already the most advanced one to exist."
    chief "I'm confident that you will come up with a solution."
    "More courses it is..."
    "You head back to the throne room."
    stop music
    scene chief_room
    show chief_img at right
    show lynx_img at left
    with fade
    return

label waterMilestone4FixAttemptSuccess:
    chief "Now this is truly some exceptional news. We shall take another shot at the purifier."
    scene Water_Purifier_damaged
    show chief_img at right
    show lynx_img at left
    with fade
    play music fixing
    "With a toolkit, and a newly configured CPUs constructed with the original one used by the purifier and spares laying around, you and the chief approach the purifier."
    #Scene purifier
    "The CPU fits in."
    lynx "And now, the moment of truth..."
    scene Water_Purifier_fixed
    show chief_img at right
    show lynx_img at left
    with fade
    "The system slowly comes back to life as it takes in water from the nearby river."
    "Before you knew it, the output tank begins to fill with crystal clear water."
    "You did it."
    chief "Congratulations lynx. I might have doubted you for a single moment, but in the end, you did well."
    if not purifier_success:
        $end_state+=1
    $purifier_success = True
    stop music
    scene chief_room
    show chief_img at right
    show lynx_img at left
    with fade
    return

label fixGenerator:
    chief "That's atronomical news!"
    lynx "I just so happened to come across the video in my social media marketing class on how to fix a generator."
    chief "Let's see if you got any value out of it then."

    "You and the chief head over to the generator."
    scene Generator_damaged 
    show chief_img at right
    show lynx_img at left
    with fade
    play music fixing
    "The generator that used to churn with life now lays silent."
    "Time to repair!"
    "You recall the steps from the YouTube video: Coolant, Fuel Levels, Oil Levels, Shutoff Valve, and Air Filter."
    "You check and repair each of the components."
    scene Generator_fixed
    show chief_img at right
    show lynx_img at left
    with fade
    "After some additional simple wiring, the generator sputters back to life."
    chief "Now, we will have energy for years to come. We all owe you one, Lynx."
    if not generator_success:
        $end_state+=1
    $generator_success = True
    stop music
    scene chief_room
    show chief_img at right
    show lynx_img at left
    with fade
    return

label weaponsModelFound:
    chief "That's good news, but there is nothing we can do with a 3D model."
    chief "Do you know what would be usefull? A blueprint."
    if cadAndDigital.currentClass >= 3:
        "That I can do, thanks to the blueprint lecture from CAD and Digital! Give me a moment"
        "..."
        $weaponsCheck_obtainBlueprint = True
        call weaponsComplete #directly call this if you already can make the blue print
    else:
        "{i}In what class would I find information about a blueprint?"
    return

label weaponsComplete:
    show blueprint at truecenter
    "You hand the blueprints over to the chief"
    hide blueprint
    chief "Perfect. With this new design, we will be able to protect our tribe from neighboring agressors."
    chief "Your contributions are truly invaluable."
    if not weapons_success:
        $end_state+=1
    $weapons_success = True
    return
