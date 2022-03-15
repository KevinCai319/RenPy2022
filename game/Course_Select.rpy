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
        #$course = 0 Some errors with this, where the compiler thinks course is an integer.
        #probably cuz of the nature of python, it converts course to int before it can progress class

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
    jump course_select.course_done
    return

label english_course:
    call courseIntro
    jump course_select.course_done
    return

label circuits_course:
    call courseIntro
    jump course_select.course_done
    return

label ee_course:
    call courseIntro
    jump course_select.course_done
    return

label media_course:
    call courseIntro
    jump course_select.course_done
    return

label cad_course:
    call courseIntro
    jump course_select.course_done
    return

label math1_course:
    call courseIntro
    jump course_select.course_done
    return

label math2_course:
    call courseIntro
    jump course_select.course_done
    return

label math3_course:
    call courseIntro
    jump course_select.course_done
    return

label physics_course:
    call courseIntro
    jump course_select.course_done
    return

label chem_course:
    call courseIntro
    jump course_select.course_done
    return

label food_course:
    call courseIntro
    jump course_select.course_done
    return
    
label courseIntro:
    "Welcome to Meta University's [course.name]!"
    "This will be lecture [course.currentClass]."
    $content = course.lectureContent[course.currentClass-1]
    "Todays topic: [content]"
