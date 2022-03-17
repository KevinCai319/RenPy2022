default pingPongAttendance = 0
define tableTennisAI = Character("Club Member")
label ping_pong:
    $pingPongAttendance+=1;
    $playing = renpy.music.is_playing()
    if not playing:
        play music "audio/music/pong.ogg"
    $rand = renpy.random.randint(0,1) == 1
    if (pingPongAttendance == 1):
        call pingPongPrologue
    elif rand or (pingPongAttendance >= 3 and (not generatorCheck_pingPongClubChat)):
            call pingPongSessionSpecial
    else:
        call pingPongSessionNormal
    if daily_summary.find("Attended Table Tennis Club\n") == -1:
        $daily_summary += "Attended Table Tennis Club\n"
    return

label pingPongPrologue:
    play music "audio/music/pong.ogg"
    "You decide to check out the table tennis club... what's table tennis?"
    #scene gym?
    tableTennisAI "Heyyy look he showed up."
    "You see a student holding some tiny board in his right hand, identical to the one in yours."
    tableTennisAI "Let's rally."

    "Many questions fire up in your mind, but the so called \"table tennis\" must continue."
    "As you see him approach the blue table, you decide to do the same."

    tableTennisAI "Sooo how was your day?"
    yumemi "Not bad. How was yours?"
    "He throws a ball high in the air and gives it a swift kick with the board."
    yumemi "Woah!!"
    "You're startled by the speed the ball as it flies towards you. It reminded you so much of the projectiles tossed during combat with other tribes."
    tableTennisAI "Is there anything wrong?"
    yumemi "What was that for?"
    "You look across at the other tables and see the players casually returning the balls with their tiny boards in a rhythmic exchange"
    "Is this what table tennis is?"
    tableTennisAI "Did you forget how to play?"
    "After some consideration, you recollect yourself and respond."
    yumemi "No, let's do this again."
    tableTennisAI "I never remembered that you had such difficulty returning a simple serve."
    yumemi "Just give me some time to warm up."

    "The rest of the session didn't go much better, but eventually, you begin to get the hang of it."

    "You know what? Ping pong is actually pretty fun."
    #maybe add to the dialogue text and have talk to the chief about how ping pong was
    stop music
    return

label pingPongSessionNormal:
    play music "audio/music/pong.ogg"
    "That same AI is there again."
    tableTennisAI "Hey, let's rally."
    yumemi "Sure."
    if pingPongAttendance == 5:
        tableTennisAI "You're getting a lot better from that time you showed up"
        tableTennisAI "As they say, practice makes perfect."
        tableTennisAI "I'm just kidding, who are we in the grand scheme of ping pong professionals."

    "You and the club member continue to rally and proceed with the small talk as usual."
    stop music
    return

label pingPongSessionSpecial:
    play music "audio/music/pong.ogg"
    "That same AI is there again."
    tableTennisAI "Hey, let's rally."
    yumemi "Sure."

    "You proceed with your rally as usual."
    "Then..."
    tableTennisAI "Hey, have you heard of this very popular YouTuber who fixes complex machines?"
    yumemi "No, who? Also, what's YouTube?"
    tableTennisAI "DO YOU LIVE UNDER A ROCK?"
    yumemi "Perhaps I do."
    tableTennisAI "Bruh...Anyway, his name is RealEngineer. You should check him out."
    tableTennisAI "And if you seriously don't know what YouTube is, {color=#00ff00}consider taking Social Media Marketing.{/color}"
    tableTennisAI "It will catch you up real easily."

    "Social Media and Marketing. I should check that out."

    yumemi "Honestly, I haven't. I'll check the course out, though."
    "The club member looks at you with a gaze of amazement, but you proceed to rally as usual."
    $socialMediaMarketing.unlocked = True
    $generatorCheck_pingPongClubChat = True
    stop music
    return
