
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
        options.append(("Dating Simulator", "dating_prologue"))
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
    frame:
        xalign 0.0
        yalign 0.7
        background "#00000098"
        vbox:
            $time_left = WINTER_DAY-day
            text "{u}Days Until\nWinter{/u}:[time_left]":
                color "#7df0ff"
                bold True
                size 60 
            null height 30
            text "{u}Goals{/u}":
                color "#7df0ff"
                bold True
                size 60
            $gen_text =  "-Generator successfully restored.\n" if generator_success else "-Find a way to restore generator.\n"
            if goal_generator:
                text gen_text:
                    xalign 0.0
                    yalign 0.75
                    if generator_success:
                        color "#00ff00"
                    else:
                        color "#7df0ff"
                    size 50
            $pur_text =  "-Purifier is up and running.\n" if purifier_success else  "-Find a way to restore the purifier.\n"
            if goal_purifier:
                text pur_text:
                    xalign 0.0
                    yalign 0.75
                    if purifier_success:
                        color "#00ff00"
                    else:
                        color "#7df0ff"
                    size 50
            $wea_text =  "-Your tribe has enough weapons.\n" if weapons_success else "-Find a way to help produce weapons.\n"
            if goal_weapons:
                text wea_text:
                    xalign 0.0
                    yalign 0.75
                    if weapons_success:
                        color "#00ff00"
                    else:
                        color "#7df0ff"
                    size 50
            if not (goal_weapons or goal_generator or goal_purifier):
                text "-None for now.\n":
                    xalign 0.0
                    yalign 0.75
                    color "#7df0ff"
                    size 50
            

        
