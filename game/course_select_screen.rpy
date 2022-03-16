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
        gridHeight = limit+2
    frame:
        xalign 1.0
        yalign 0.5
        background "#00000098"
        vpgrid:
            rows gridHeight
            cols 1
            scrollbars "vertical"
            spacing 20
            top_margin 200
            for i in options:
                button:
                    text i[0]:
                        xalign 0.5
                        yalign 0.5
                    style "choice_button"
                    xmaximum 600
                    action Return((i[0],i[1], extras))