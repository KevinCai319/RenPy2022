default chief_neutral = 5
default chief_happy = 2
default chief_very_angry = 7
label end_day:
    chief "So what happened today?"
    label .summary:
        lynx "Here's a summary of what happened:"
        $penalty = 0
        if len(daily_summary) > 0:
            lynx "[daily_summary]"
            #adjust penalty based on certain key words in daily summary.
            $daily_summary.find("")
        else:
            lynx "Nothing of note."
            $penalty = 2
        
        if(weapons_success and purifier_success and generator_success):
            lynx "Everything is fully operational!"
            chief "<YOU WIN GAME>"
            return
        #Check if all 3 objectives are done, or only 2 of the 3.
        if (weapons_success and purifier_success):
            chief "Wow, that is amazing news!."
            chief "With weapons and the water purifier working, our tribe can still survive the winter."
            chief "Do you want to continue?"
            return
        if (weapons_success and generator_success):
            chief "Wow, that is amazing news!. Do you want to continue?"
            return
        if(purifier_success and generator_success):
            chief "Wow, that is amazing news!. Do you want to continue?"
            return
        #Check of either of the 3 objectives are done.
        if generator_success:
            lynx "The generator is curerently working."
            $penalty -=2
        if purifier_success:
            lynx "The water purifer is operational."
            $penalty -=2
        if weapons_success:
            lynx "We currently have weapons"
            $penalty -=2
        lynx "That is all."
        #Chief cares about time since beginning of game, updates on one of the 3 objectives
        chief "..."
        $score = day+penalty
        if score <= chief_happy:
            chief "Good work today! I hope for the best tomorrow."
            lynx "Thank you chief."
        elif score <= chief_neutral:
            chief "Winter is drawing near, I hope you have spent your time well."
            lynx "I'll try my best."
        else:
            chief "Winter is quickly approaching, and the generator is losing energy, you better step it up!"
            lynx "Sorry chief, I will try harder tomorrow."
    return
label good_success:
    menu:
        "I willl continue":
            lynx "I will continue"

        "I have had enough. I want to relax":
            lynx "I have had enough. I want to relax"
