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
    $renpy.call(extras[choice][0])
    label .course_done:
        $course.progressClass()
        jump course_select.event_done
    label .event_done:
        $actions_done_for_day+=1
        return
#courses!!
#Use keyword 'course' to refer to the course variable!!
#
#ELECTRONICS
label animal_course:
    call courseIntro

    return

label english_course:
    call courseIntro

    return

label circuits_course:
    call courseIntro

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
    call courseIntro

    return

label cad_course:
    call courseIntro

    return

label math1_course:
    call courseIntro
    return

label math2_course:
    call courseIntro

    return

label math3_course:
    call courseIntro

    return

label physics_course:
    call courseIntro

    return

label chem_course:
    call courseIntro

    return

label food_course:
    call courseIntro

    return

label courseIntro:
    "Welcome to Meta University's [course.name]!"
    "This will be lecture [course.currentClass] out of [course.numClasses]."
    $content = course.lectureContent[course.currentClass-1]
    "Todays topic: [content]"
    "..."
    return
