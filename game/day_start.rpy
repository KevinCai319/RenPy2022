label day_start:
    lynx "It's a start of a new day. Better go visit Chief again."

    "{i} You make your daily trip to the chief's place.{\i}"

    if WINTER_DAY-day < 3:
        lynx "Brrrr... It's pretty chilly today, I'm not sure how things will turn out..."
    elif WINTER_DAY-day <= 5:
        lynx "... "
    else:
        ""
    
    #<Lynx arrives at the Chief's place>
    lynx "Hello chief, how are you today?"
    if end_state == 0:
        if (WINTER_DAY-end_state)/3
    return