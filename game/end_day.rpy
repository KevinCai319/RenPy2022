default chief_neutral = 0.6
default chief_happy = 0.3
default chief_very_angry = 0.8

label end_day:
    scene chief_room
    show chief_img at right
    show lynx_img at left
    with fade
    play music "audio/music/Strong-Wind-Blowing.ogg"
    chief "So what happened today?"
    label .summary:
        $playing = renpy.music.is_playing()
        if not playing:
            play music "audio/music/Strong-Wind-Blowing.ogg"
        lynx "Here's a summary of what happened:"
        $penalty = 0
        if len(daily_summary) > 0:
            $summary_list = daily_summary.split('\n')
            $summary_length = len(summary_list)
            $counter = 0
            while counter < summary_length:
                $item = summary_list[counter]
                if not item.isspace() and len(item) != 0:
                    lynx "[item]"
                $counter+=1
            #adjust penalty based on certain key words in daily summary.
            #this is a special dialogue for when you acheive milestone 2 of water check
            if daily_summary.find("I think we can fix the purifier now") != -1:
                stop music fadeout 0.5
                call waterMilestone2FixAttemptFail
            #if, in case you finish multiple in a day
            if daily_summary.find("I have the solution to the water purifier!") != -1:
                stop music fadeout 0.5
                call waterMilestone4FixAttemptSuccess
            if daily_summary.find("I beleive I can fix the generator!") != -1:
                stop music fadeout 0.5
                call fixGenerator
            if daily_summary.find("We might be able to construct weapons.") != -1:
                stop music fadeout 0.5
                call weaponsModelFound
            if daily_summary.find("I have converted the 3D model to a blueprint.") != -1:
                stop music fadeout 0.5
                call weaponsComplete
            if cadAndDigital.currentClass >= 3 and goal_weapons and (not weaponsCheck_3dModelFromPoster) and (not weapons_success):
                stop music fadeout 0.5
                lynx "In addition, I also have some weapon blueprints that we can use."
                call weaponsComplete
        else:
            lynx "Nothing of note."
            #chief gets more pissed if nothing happened
            $penalty = 2
        $playing = renpy.music.is_playing()
        if not playing:
            play music "audio/music/Strong-Wind-Blowing.ogg"
        if(weapons_success and purifier_success and generator_success):
            lynx "Everything is fully operational!"
            return
        #Check of either of the 3 objectives are done.
        if generator_success:
            $penalty -=2
        if purifier_success:
            $penalty -=2
        if weapons_success:
            $penalty -=2

        #lynx "That is all."
        #Chief cares about time since beginning of game, updates on one of the 3 objectives
        $score = day+penalty
        #sentimment of chief is based on # days that are left, and if any notable things happen.
        if score <= WINTER_DAY * chief_happy or score >= 2:
            chief "Good work today! I hope for the best tomorrow."
            lynx "Thank you chief."
        elif score <= WINTER_DAY * chief_neutral:
            chief "Winter is drawing near, I hope you have spent your time well."
            lynx "I'll try my best."
        else:
            chief "Winter is quickly approaching, and the generator is losing energy, you better step it up!"
            lynx "Sorry chief, I will try harder tomorrow."
    label .end:
        return
