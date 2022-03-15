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
        else:
            lynx "Nothing of note."
            $penalty = 2
        #TODO: Check of either of the 3 objectives are done.
        lynx "That is all."
        #Chief cares about time since beginning of game, updates on one of the 3 objectives
        chief "..."
        $score = days+penalty
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
    