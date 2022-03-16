image course_select_background = "Backgrounds/Meta_University.png"
label course_select:
    play music campus
    scene course_select_background with fade
    call screen course_select_menu
    $course_select_choice = _return[1]
    if course_select_choice == "dating_prologue":
        stop music fadeout 0.5
        call dating_prologue
        jump course_select.event_done
    if course_select_choice == "ping_pong":
        stop music fadeout 0.5
        call ping_pong
        jump course_select.event_done
    $extras = _return[2]
    $tple = extras[course_select_choice]
    $course = Course.course_listing[course_select_choice]
    if course.currentClass <= 1:
        "[tple[1]]"
    call courseIntro
    $renpy.call(tple[0])
    label .course_done:
        call courseOutro
        stop music fadeout 0.5
        $course.progressClass()
    label .event_done:
        $actions_done_for_day+=1
        return
#courses!!
#Use keyword 'course' to refer to the course variable!!
#TODO: replace placeholder text.
#ELECTRONICS
label animal_course:
    if course.currentClass == 1:
        if animalSuggestionReceived:
            "Taking David's advice, you chose to begin the course."

    if course.currentClass == 4:
        "Now that you have gained significant insight into behavior of animals and their interactions with humans, you will be put into pairs to complete a poster on any subject that we covered in class."
        $weaponsCheck_posterBegin = True;
    if course.currentClass == 5:
        "You should all have a fresh draft of the poster. You will continue while receiving peer feedback."
        yumemi "{i}The poster that my partner has worked on so far seems to have a 3D model of a gun of some sorts..."
        yumemi "{i}I will report this back to the chief"
        $daily_summary += "We might be able to construct weapons.\n"
        $weaponsCheck_3dModelFromPoster = True;

    return

label english_course:
    if course.currentClass == 1:
        yumemi "How much do you want to bet we'll read Romeo and Juliet?"
    if course.currentClass == 1:
        yumemi "HMmmmmmmm?"
    return

label circuits_course:
    return

label ee_course:
    if course.currentClass == 1:
        yumemi "This course seems to contain just the right information on how to fix the water purifier."
        yumemi "It does seem to be slightly lengthy, though."
        yumemi "Let's see where this goes."
        $waterCheck_milestone1 = True
    if course.currentClass == 6:
        yumemi "Hold on, this is exaclty what we need!"
        yumemi "All the sensors have been functioning properly, but the output devices were faulty."
        $waterCheck_milestone2 = True
        $daily_summary += "I think we can fix the purifier now\n"
    if course.currentClass == 11:
        yumemi "Wow, this course has costed me an equivalent of 11 days worth of studying."
        yumemi "{i}That's pretty fast if you ask me{/i}, but time is of the essence."
        yumemi "Is it worth pursueing this track even further?"
        yumemi "Well, there's only 5 more classes remaining..."
        $waterCheck_milestone3 = True
    if course.currentClass == 15:
        yumemi "This is some useful stuff."
    if course.currentClass == 16:
        yumemi "Eureka! To increase the power of the CPU, I could chain them together, since the property of their computational power follows an additive relation if done correctly."
        $waterCheck_milestone4 = True
        $daily_summary += "I have the solution to the water purifier!\n"
    return

label media_course:
    if course.currentClass == 1:
        "{i}How do I access the YouTube files though?"
    if course.currentClass == 2:
        "Our focus will be specifically on Twitter, Facebook, Reddit, and YouTube."
        "Today, we will examine the archives belonging in Twitter"
    elif course.currentClass == 3:
        "As an adendum to the prior class, we will also be examining the archives belonging in Facebook"
    elif course.currentClass ==4:
        "As an adendum to the our 2nd lecture, we will also be examining the archives belonging to Reddit"
    if course.currentClass == 5:
        "As an adendum to the our 2nd lecture, we will also be examining the archives belonging to YouTube"
        "Due to the popularity of Real Engineering in recent weeks, we will be analyzing the techniques he utilizes in his video: \"Repairing a Generator SIMPLIFIED\""
        "{i}No way this is true. All I have to do is remember the steps and report back to the chief."
        "This concludes our mini unit on specific social media platforms."
        $daily_summary += "I beleive I can fix the generator!"
        $generatorCheck_youtubeVideoObtained = True
    return

label cad_course:
    if course.currentClass == 3:
        if weaponsCheck_3dModelFromPoster:
            "{i}Blueprints! This is what the chief needs!"
            $daily_summary += "I have converted the 3D model to a blueprint.\n"
        else:
            "{i}Those Blueprints might be helpful."
    return

label math1_course:

    return
label math2_course:

    return
label math3_course:

    return

label physics_course:
    if course.currentClass == 5:
        yumemi "Is this course in English?"
    if course.currentClass == 8:
        yumemi "This can not be English."
    if course.currentClass == 10:
        yumemi "Sprichst du Deutsch?"
    return

label chem_course:
    return

label food_course:
    return

label courseIntro:
    scene classroom with FAST_FADE
    "Welcome to Meta University's [course.name]!"
    "This will be lecture [course.currentClass] out of [course.numClasses]."
    $content = course.lectureContent[course.currentClass-1]
    "Todays topic: [content]"

    $summaryAddOn = "I attended the " + course.name + " lecture and learned about " + content + ".\n"
    $daily_summary += summaryAddOn

    return
label courseOutro:
    if(course.currentClass == course.numClasses):
        "Congratulations on finishing course [course.name]. I wish you all the best"
        #completed courses cannot be taken again.
        $course.unlocked = False
    else:
        "That is all for today. I hope to see you next class."
    return
