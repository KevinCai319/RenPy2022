
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
                options.append((Course.course_listing[count].name + " " + str(Course.course_listing[count].currentClass-1) + "/" + str(Course.course_listing[count].numClasses),count))
            count+=1
        options.append(("Dating", "dating_prologue"))
        options.append(("Ping Pong", "ping_pong"))
        gridHeight = (limit+2)*2
    $batt_left = int((float(MAX_ACTIONS_PER_DAY-actions_done_for_day)/MAX_ACTIONS_PER_DAY)*100)
    frame:
        xalign 1.0
        yalign 0.5
        background "#00000098"
        frame:
            top_margin 200
            background "#00000000"
            vpgrid:
                rows gridHeight
                cols 1
                scrollbars "vertical"
                spacing 20
                for i in options:
                    button:
                        text i[0]:
                            xalign 0.5
                            yalign 0.5
                        style "choice_button"
                        xmaximum 600
                        action Return((i[0],i[1], extras))
    add "Battery.png" xalign 0.83 yalign 0.05 xysize (300,150)
    text "[batt_left]%":
        yalign 0.075
        xalign 0.99
        size 80
        bold True
    $goals = ""
    if goal_generator and (not generator_success):
        $goals += "-Find a way to restore generator.\n"
    if goal_purifier and (not purifier_success):
        $goals += "-Find a way to restore the purifier.\n"
    if goal_weapons and (not weapons_success):
        $goals += "-Find a way to help produce weapons.\n"
    if goals == "":
        $goals += "-None for Now"
    frame:
        xalign 0.0
        yalign 0.8
        background "#00000098"
        vbox:
            text "{u}Goals{/u}":
                color "#7df0ff"
                bold True
                size 60 
            text goals:
                xalign 0.0
                yalign 0.75
                color "#7df0ff"
                size 50

        
