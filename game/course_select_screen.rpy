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