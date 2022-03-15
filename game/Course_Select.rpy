image course_select_background = "Backgrounds/Meta_University.png"
label course_select:
    "What would you like to do today, [MC] ?"
    show course_select_background
    call screen course_select_menu
    $course_select_choice = _return[1]
    if course_select_choice == "dating_prologue":
        call dating_prologue
        jump course_select.event_done
    if course_select_choice == "ping_pong":
        call ping_pong
        jump course_select.event_done
    $extras = _return[2]
    $tple = extras[course_select_choice]
    "[tple[1]]"
    hide course_select_background
    $course = Course.course_listing[course_select_choice]
    call courseIntro
    $renpy.call(tple[0])
    label .course_done:
        call courseOutro
        $course.progressClass()
        jump course_select.event_done
    label .event_done:
        $actions_done_for_day+=1
        return
#courses!!
#Use keyword 'course' to refer to the course variable!!
#TODO: replace placeholder text.
#ELECTRONICS
label animal_course:
    lynx "This class doesn't seem to be very interesting"
    return

label english_course:
    lynx "This class doesn't seem to be very interesting"
    return

label circuits_course:
    lynx "This class doesn't seem to be very interesting"
    return

label ee_course:
    call courseIntro
    if course.currentClass == 1:
        yumemi "This course seems to contain just the right information on how to fix the water purifier."
        yumemi "It does seem to be slightly lengthy, though."
        yumemi "Let's see where this goes."
        $waterCheck_milestone1 = True
    if course.currentClass == 6:
        yumemi "Hold on, this is exaclty what we need!"
        yumemi "All the sensors have been functioning properly, but the output devices were faulty."
        $waterCheck_milestone2 = True
        $daily_summary += "I think we can fix the purifier now"
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
        $daily_summary += "I have the solution to the water purifier!"
    return

label media_course:
    lynx "This class doesn't seem to be very interesting"
    return

label cad_course:
    lynx "This class doesn't seem to be very interesting"
    return

label math1_course:
    lynx "This class doesn't seem to be very interesting"
    return

label math2_course:
    lynx "This class doesn't seem to be very interesting"
    return

label math3_course:
    lynx "This class doesn't seem to be very interesting"
    return

label physics_course:
    lynx "This class doesn't seem to be very interesting"
    return

label chem_course:
    lynx "This class doesn't seem to be very interesting"
    return

label food_course:
    lynx "This class doesn't seem to be very interesting"
    return

label courseIntro:
    "Welcome to Meta University's [course.name]!"
    "This will be lecture [course.currentClass] out of [course.numClasses]."
    $content = course.lectureContent[course.currentClass-1]
    "Todays topic: [content]"
    return
label courseOutro:
    if(course.currentClass+1 >= course.numClasses):
        "Congratulations on finishing course [course.name]. I wish you all the best"
        #completed courses cannot be taken again.
        $course.unlocked = False
    else:
        "That is all for today. I hope to see you next class."
    return
