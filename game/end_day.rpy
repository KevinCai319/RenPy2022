default chief_neutral 5
default chief_happy 2
default chief_very_angry 7
label end_day:
    chief "So what happened today?"
    label .summary:
        lynx "Here's a summary of what happened:"
        lynx "[daily_summary]"
        lynx "That is all."
        #Chief cares about time since beginning of game, updates on one of the 3 objectives
        chief "..."
        if days <= chief_happy:
            chief "Good work today. I hope for the best tomorrow."
        else if days <= chief_neutral:
    return