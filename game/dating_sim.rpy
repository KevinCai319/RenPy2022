default davidAffinity = 0
default davidKnows = False
default keyGiven = False
default conversationCount = 0
default animalSuggestionReceived = False

label dating_prologue:
    $askedWhoIsHe = False #just for some future dialogue in truth label, that's about it for this variable's usage
    show david_img at left with fade
    show mc_img at right

    david "Hey, [MC]! Over here!"
    "You see a boy smiling across the road, waving his hand."
    "He seems to be about your age, with a complexion that suggests a sense of maturity mixed with youthfulness."
    "You stare at him a litter longer."
    "Is he waving at me?"
    david "[MC]!"
    "You take the risk and cross the road to greet him"
    menu:
        "Greet him":
            call greetDavid
        "Who is he?":
            $askedWhoIsHe = True
            call whoIsDavid
    david "I'm doing phenomenal! Guess what?"
    yumemi "What?"
    david "I just aced my final for Calculus III. If only I remembered that +C, I would have gotten 100."
    "{i}What is he talking about? What's a final? Calculus III?"
    yumemi "That's great news!"
    david "Why don't we celebrate and head over to the pet store and check out some of the puppies?"
    "{i}What's a pet store?"

    "You received a teleport request to: \"Animal Central\""
    menu:
        "Accept the request":
            "Without any other choice, you choose to follow along"

    "As the surrounding materialize, you face light up with wonder."
    "Are these the animals from the ancient world that everyone from the tribe talk about?"

    david "Believe it or not, this is my favorite place to relax."
    david "Oh, there seems to be a new arival of Golden Retriever puppies!"

    "You follow along and soon enough, you approach a small enclosure of creatures."
    "They were like nothing you have seen before. On one hand, you felt an automatic need to protect them."
    "On the other, you knew that if these creatures were allowed to roam free in your current world, they wouldn't survive a minute before being hunted down as food."

    yumemi "This is amazing!"

    david "Right? Speaking of animals, have you heard of the new {color=#00ff00}\"Animal Behaviour and Welfare\" course{/color} being offered?"
    david "I think you would love it."

    "{i}That course is indeed in the catalog..."

    yumemi "I'll keep an eye out for that."
    $animalSuggestionReceived = True;
    "You eventually finish \"petting\" all the dogs in that area and decide to call it a day."
    "But right before you were about to leave..."
    david "Hey, why don't we watch the new Marvel movie that just came out tonight? I heard so much hype about it from all my friends."

    "A \"movie\"? Once again, another unfamiliar term"
    "If you were going to go, it would cost you power, a resource that you couldn't afford to waste."
    "You begin to question the feasiability of the pretense you've been keeping up."

    menu:
        "Tell him the truth about your origin":
            call truth
        "Go along with the dialogue (this will cost you one energy)" if actions_done_for_day == 0:
            call playAlong
        "Decline the invitation":
            call decline
    hide david_img
    hide mc_img

    $conversationCount += 1
    return

label greetDavid:
    yumemi "Hey, how has your day been?"
    return
label whoIsDavid:
    $davidAffinity -= 1

    yumemi "Hi, have we met before?"
    david "Yumemi, don't scare me like that."
    "You inspect his profile: "
    "Name: David \n Manufacture date: 2049, March 17"
    "You look farther into his profile"
    "Relationship status: dating [MC]"
    yumemi "{i}Oh, no wonder..."
    yumemi "I'm just kidding, who has your day been?"
    return

label truth:
    yumemi "David, before I go any further, I want to establish something."
    "His jovial face suddenly grew stern as he sensed a shift in attitude."
    yumemi "I'm not [MC]. My name is actually Lynx."
    david "What are you talking about? Was I being catfished the whole time?"
    "You don't know that he means by \"catfished\", but you decide to ignore that comment."
    "I'm from the future, in a world that has been consumed by nuclear war. I'm communicating to you through what we consider to be an \"artifact of the ancient world,\" or, this VR device that I'm communicating to you with."
    david "No, that's crazy. How can I trust that you're from the future?"
    if askedWhoIsHe:
        david "Wait, that's why you asked who I was when you first saw me?"
    else:
        yumemi "You'll have to take my word for it."

    david "So where's Yumemi then?"
    yumemi "I don't know."
    david "Okay, I need a moment to take this in. We'll talk about this next time."
    "David leaves, and you begin to wonder: {i}did I do the right thing?"

    $davidAffinity -= 4
    $davidKnows = True
    #so if you do both, you will have -5
    return

label playAlong:
    $actions_done_for_day+=1
    yumemi "Oooh that sounds like fun"
    david "I know right? Cool I'll see you tonight!"

    "That night, you head to BND and watched the debut of Gray Puma."
    "You manage to keep your disguise without David knowing."

    $davidAffinity += 3
    #You will either have 2 or 3 affinity at this point
    return
label decline:
    yumemi "I have had to deal with too much homework recently. I actually have to finish up two papers before tomorrow..."
    david "Oh, I never knew you had such intense course work."
    david "Okay, I'll leave you to it and we can watch the movie together some other time!"
    yumemi "I'll see you tomorrow then!"
    david "Alright, bye!"

    $davidAffinity -= 1
    #You will either have 0 or -1 by this point
    return

label whenDavidKnows: 
    scene cafe_room 
    show david_img at left
    show mc_img at right
    with fade
    david "Okay, though there isn't much that I would want to discuss."
    yumemi "I suppose you can tell a little about who Yumemi was."
    david "She was a very sweet person who knew how to appreciate the little things in life."
    "{i}totally not generic**"
    david "Well if you want to know to know more about Yumemi, I think it would be worth checking out her diary."
    yumemi "The Diary! I recall seeing that."
    david "After we began talking for several months, she told me: \"If I were to die, please don't feel sad for me. Take this:\""
    david "And she gave me a unique passcode to her diary."
    david "Now, I will hand it to you. All I want is to know if she mentions anything about her parents."
    "You copy the code."
    yumemi "I won't let you down."
    "David lifts his eyes halfway to your gaze, sighs, and proceeds to stare at the ground."
    $diary_unlock_level = 1
    $keyGiven = True
    $conversationCount += 1
    return

label ordinaryDaydKnows:
    scene cafe_room 
    show david_img at left
    show mc_img at right
    with FAST_FADE

    david "Okay, though there isn't much that I would want to discuss."
    david "I just want to know where Yumemi went."
    $conversationCount += 1

    return


label ordinaryDay:
    scene cafe_room 
    show david_img at left
    show mc_img at right
    with FAST_FADE

    david "Sure, is there anything on your mind?"
    yumemi "Hey, I wanted to hear what you had to say..."
    $theme = renpy.random.randint(0,1);
    $title = renpy.random.randint(0,2);
    $headline = headlines[theme][title]
    david "Oh okay. In that case, have you read of: \"[headline]\"?"
    if theme == 0:
        yumemi "Wow, that's interesting. That man must be crazy."
        david "Right? Imagine if that was me!"
        yumemi "Well I don't even have to imagine."
        david "Heyyy that's not nice."
    if theme == 1:
        yumemi "That's pretty funny."
        yumemi "I know right? Where do you even find this?"
        david "That's a secret."
        yumemi "Come on! I want to know..."
    $conversationCount += 1
    return

default headlines = [
    [
        "Florida man tries to rob a bank wearing a 'Sonic The Hedgehog' mask",
        "Florida man blames Putin for why he was speeding during traffic stop",
        "Florida Man Accidentally Buys City Water Tower"
    ],
    #the onion OGN
    [
        "Apple announces the release of the Iphone 22 Max Pro SE Lite Pro Red Max Pro Red Pro Plus. Newest leaks suggest a back panel covered with an array of twenty state of the art cameras.",
        "Be Cool, For Once, Gamers: Mrs. Thompson Said We Might Get to Play 'Minecraft' If We Finish The Quiz By 11:45",
        "Airbnb Tests New Feature That Allows Black Guests"
    ],
    [
        
    ]  #cute headlines 
]

default floridaHeadlines = [
    "Florida man accused of stealing 18 turtles worth $30,000 from breeder while fixing his fridge",
    "Florida man calls police to verify his meth is authentic, cops claim",
    "Two Florida Women Attack Man With Glitter, Face Felony Charges",
    "South Florida man allegedly bites off hospital security guard's finger",
    "Florida Man Has Growing God Complex",
    "Florida Man Guilty of Using Twin's ID for Veterans Benefits",
    "Florida man wins $1M from scratch-off ticket, plans to surprise spouse: 'I haven't even told my wife yet'",
    "Catch of the day: Florida man, grandson reel in sniper rifles while magnet fishing near Miami",
    "Florida man steals car; train sends it crashing into house",
    "Florida man tries to rob a bank wearing a 'Sonic The Hedgehog' mask",
    "Florida man told police he was 'high and happy'",
    "Florida man stuffs stolen crossbow down his pants",
    "Florida Man Unwillingly Faces Drawbrige, Barely Makes It Out",
    "Florida man blames Putin for why he was speeding during traffic stop",
    "Florida man breaks beer bottle over his head",
    "Florida Man Gets Prison For Illegally Shipping Turtles And Snakes",
    "South Florida man frustrated with plastic pollution along our beaches",
    "Lawn police trim $30,000 from Florida man who violates the 10-inch rule",
    "UFO sightings on the rise: Florida man describes orbs he caught on camera",
    "Florida man wrestles alligator to save his dog",
    "Florida Woman Won't Be Outdone by Florida Man, Leads Cops in Nearly Naked High-Speed Chase",
    "Florida man buys TV ads in attempt to reopen U.S.-Canada border",
    "Florida Man Accidentally Buys City Water Tower"
]