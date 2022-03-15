default chief_neutral = 0.6
default chief_happy = 0.3
default chief_very_angry = 0.8
label end_day:
    chief "So what happened today?"
    label .summary:
        lynx "Here's a summary of what happened:"
        $penalty = 0
        if len(daily_summary) > 0:
            lynx "[daily_summary]"
            #adjust penalty based on certain key words in daily summary.
            $daily_summary.find("<KEYWORD>")
            #TODO: change chief response based on keywords that are found.
        else:
            lynx "Nothing of note."
            #chief gets more pissed if nothing happened
            $penalty = 2
        
        if(weapons_success and purifier_success and generator_success):
            lynx "Everything is fully operational!"
            chief "<YOU WIN GAME>"
            return
        #Check if all 3 objectives are done, or only 2 of the 3.
        if (weapons_success and purifier_success):
            chief "Wow, that is amazing news!."
            chief "With weapons and the water purifier working, our tribe can still survive the winter."
            jump good_success
        if (weapons_success and generator_success):
            chief "Wow, that is amazing news!. Do you want to continue?"
            jump good_success
        if(purifier_success and generator_success):
            chief "Wow, that is amazing news!. Do you want to continue?"
            jump good_success
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

#When you have reached 2/3 good, this is the prompt that occurs when chief asks if you want to continue.
label good_success:
    menu:
        "I will continue":
            lynx "I will continue"
            chief "Alright. I wish you the best. See you tomorrow"
        "I have had enough. I want to relax":
            lynx "I have had enough. I want to relax"
            chief "Alright. We should have enough to continue our tribe for quite a while."
    jump game_end
            
