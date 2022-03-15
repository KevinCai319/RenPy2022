label day_start:
    lynx "It's a start of a new day. Better go visit Chief again."

    "{i} You make your daily trip to the chief's place.{\i}"

    if WINTER_DAY-day < 3:
        lynx "Brrrr... It's pretty chilly today, I'm not sure how things will turn out..."
    elif WINTER_DAY-day <= 5:
        lynx "... It's a bit colder than usual"
    else:
        lynx "..."
    
    #<Lynx arrives at the Chief's place>
    lynx "Hello chief, how are you today?"

    #Chief gives additional text based on the day.
    if day == 1:
        chief "It gets colder and colder, but the only generator the tribe relies on doesn't sound good"
    elif day == 2:
        chief "Our tribe has lost people due to a conflict with another tribe"
    elif day == 4:
        chief "Our water purifer has broken down. People were sent to find other water sources, but they were ambushed."
    elif day == 6:
        chief "Not good. We are running out of food"
    else: 
        # if 0 out of 3 are done
        #end state is how many of the goals you finished
        #all this text you can change since I am not good writer
        if end_state == 0 :
            if day < ((WINTER_DAY-day) * 0.8):
                chief "Doing fine."
            else:
                chief "How have you not gotten anything done!?"
        elif end_state == 1:
            if day < ((WINTER_DAY-day) * 0.75):
                chief "Doing well"
            else:
                chief "Doing fine"
        else:
            # in this case already done 2/3, so you technically already won
            chief "Doing great, hope you're doing well."
        
    chief "Time to enter the Metaverse."
    #scene vrDevice
    lynx "Hello Meta"
    "*click*"
    return