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
    $options.append(("Dating Sim", "dating_sim"))
    $choice = renpy.display_menu(options)
    if choice == "dating_sim":
        call dating_sim
        jump course_select.event_done
    $tple = extras[choice][1]
    "[tple]"
    $course = Course.course_listing[choice]
    $renpy.call(extras[choice][0])
    label .course_done:
        $course.progressClass()
        $course = 0
        jump course_select.event_done
    label .event_done:
        $actions_done_for_day+=1
        return
#courses!!
#Use keyword 'course' to refer to the course variable!!
#
#ELECTRONICS
label ee_course:
    "[course.name]"
    "Welcome to Meta University's introduction to EE course!"
    "This will be lecture [course.currentClass]."
    return



label media_course:

    return
