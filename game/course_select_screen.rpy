screen course_select_menu():
    $limit = len(Course.course_listing)
    $count = 0
    $options = []
    $extras = []
    python:
        while count < limit:
            canPrint = Course.course_listing[count].unlocked
            extras.append((Course.course_listing[count].label,Course.course_listing[count].extra))
            if canPrint:
                options.append((Course.course_listing[count].name,count))
            count+=1
        options.append(("Dating", "dating_prologue"))
        options.append(("Ping Pong", "ping_pong"))
        gridHeight = (limit/3)+1
    frame:
        xalign 0.5
        yalign 0.5
        vpgrid:
            rows 10
            cols 3
            scrollbars "vertical"
            spacing 20
            xalign 0.25
            yalign 0.1
            for i in options:
                button:
                    style "choice_button"
                    text i[0]
                    action Return((i[0],i[1], extras))
    # $choice = renpy.display_menu(options)
    # if choice == "dating_prologue":
    #     call dating_prologue
    #     jump course_select.event_done
    # if choice == "ping_pong":
    #     call ping_pong
    #     jump course_select.event_done 
    # $tple = extras[choice][1]
    # "[tple]"
    # $course = Course.course_listing[choice]
    # call courseIntro
    # $renpy.call(extras[choice][0])
    # label .course_done:
    #     call coruseOutro
    #     $course.progressClass()
    #     jump course_select.event_done
    # label .event_done:
    #     $actions_done_for_day+=1
    #     return