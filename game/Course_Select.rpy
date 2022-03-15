label course_select:
    "What would you like to do today, [MC] ?"
    $limit = len(Course.course_listing)
    $count = 0
    $options = []
    $extras = []
    while count < limit:
        $canPrint = Course.course_listing[count].unlocked
        $extras.append((Course.course_listing[count].label,Course.course_listing[count].extra))
        if canPrint:
            $options.append((Course.course_listing[count].name,count))
        $count+=1
    $options.append(("Dating", "dating_sim"))
    $options.append(("Ping Pong", "ping_pong"))
    $choice = renpy.display_menu(options)
    if choice == "dating_sim":
        call dating_sim
        jump course_select.event_done
    if choice == "ping_pong":
        call ping_pong
        jump course_select.event_done 
    $tple = extras[choice][1]
    "[tple]"
    $course = Course.course_listing[choice]
    call courseIntro
    $renpy.call(extras[choice][0])
    label .course_done:
        call coruseOutro
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
    lynx "This class doesn't seem to be very interesting"
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
    "This will be lecture [course.currentClass]."
    $content = course.lectureContent[course.currentClass-1]
    "Todays topic: [content]"
    return
label coruseOutro:
    if(course.currentClass+1 >= course.numClasses):
        "Congratulations on finishing course [course.name]. I wish you all the best"
        #completed courses cannot be taken again.
        $course.unlocked = False
    else:
        "That is all for today. I hope to see you next class."
    return


