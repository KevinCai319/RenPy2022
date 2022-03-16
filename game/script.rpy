# a bit too obvious that we are copying lol
define MC_str = "yumemi"
default MC = MC_str
define yumemi = Character(MC_str)
define david = Character("David Sigmund")
define lynx = Character("Lynx")
define chief = Character("chief")
define FAST_FADE = Fade(0.25,0.0,0.25)
define SLOW_FADE = Fade(0.75,0.0,0.75)
define enter_meta = Dissolve(1.0)


image chief_img = im.Scale("images/Chief/chief.PNG",600,800)
image lynx_img = im.Scale("images/Lynx/lynx.PNG",600,800)
image david_img = im.Scale("images/David/david.PNG",600,800)
image mc_img = im.Scale("images/MC/mc.PNG",500,800)


image irl_background = "Backgrounds/Post_apocalyptic_world.png"
image meta_room = "Backgrounds/mc_Room.png"
image chief_room = "Backgrounds/Chief_Room.png"
image classroom = "Backgrounds/Classroom.png"

image Generator_damaged = "Backgrounds/Generator_damaged.png"
image Generator_fixed = "Backgrounds/Generator_fixed.png"
image Water_Purifier_damaged = "Backgrounds/Water_Purifier_damaged.png"
image Water_Purifier_fixed = "Backgrounds/Water_Purifier_fixed.png"
image blank = "Backgrounds/black.jpg"
image WHITE = "Backgrounds/white.jpg"



image headset = "VR_Headset.png"
image headset_glowing = im.MatrixColor("VR_Headset.png",im.matrix.brightness(0.8) * im.matrix.tint(0.8, 0.8, 1.0))
image battery = "Battery.png"
define audio.irl = "audio/music/Strong-Wind-Blowing.ogg"
define audio.campus = "audio/music/Campus_Music.ogg"
define audio.fixing = "audio/music/Fixing.ogg"
# World Variables
default day = 1
#lose(0/1)/good(2)/best ending(3) (0/1/2/3)
default end_state = 0
#TODO: add a time where winter starts.
default WINTER_DAY = 12
# Generator Variables
default generator_success = False
default purifier_success = False
default weapons_success = False
default goal_generator = False
default goal_purifier = False
default goal_weapons = False
# Values stored in Meta device.
default started_before = False
default diary_unlock_level = 0
default actions_done_for_day = 0
default MAX_ACTIONS_PER_DAY = 4
default daily_summary = ""
default course = 0

#animations

#Variables for generator complete
default generatorCheck_pingPongClubChat = False
#default generatorCheck_youtubeVideoDiscovered = False #when you hear about it, but you don't know how to get it
   #some stuff that will tell you to take social media
default generatorCheck_youtubeVideoObtained = False #once you take course 5 of social media and marketing

#Variables for water purifier complete
#these variables are rather useless, but we'll keep them for consistency
default waterCheck_milestone1 = False #this is when he begins to feel like the course is useful. Course 1
default waterCheck_milestone2 = False #this and milestone 1 are checked for first attempt to fix. Course 6
default waterCheck_milestone3 = False #here, Lynx will be running out of patience as he searched for alternatives. Course 11
default waterCheck_milestone4 = False #Finally, he figures the replacement out. Course 16

#Variables for weapons complete
default weaponsCheck_posterBegin = False #course 4 of animal behavior
default weaponsCheck_3dModelFromPoster = False #course 5 of animal behavior
#default weaponsCheck_askChiefAbout3dModel = False #adventurer will receive information that he has to get a blueprint
default weaponsCheck_obtainBlueprint = False #from CAD course 3


#Course objects
default animalBehaviorAndWelfare = Course("Animal Behavior and Welfare","animal_course", 4, animal_course_content, True)
default englishPoetry = Course("English Poetry","english_course", 4,english_course_content, True)
default circuitsAndElectronics = Course("Circuits and Electronics","circuits_course",  9,circuits_course_content, True)
default electricEngeering = Course("Electric Engineering","ee_course", 16, ee_course_content, True, "Electrical engineering can be helpful for fixing things...")
default socialMediaMarketing = Course("Social Media Marketing","media_course", 5, media_course_content, False)
default cadAndDigital = Course("CAD And Digital", "cad_course", 10, cad_course_content, True)
default calc1 = Course("Calculus I", "math1_course", 10, math1_course_content, True)
default calc2 = Course("Calculus II", "math2_course", 10, math2_course_content, False)
default calc3 = Course("Calculus III", "math3_course", 10, math3_course_content, False)
default theoreticalPhysics = Course("Introduction to Theoretical Physics", "physics_course", 10, physics_course_content, True)
# default modernChem = Course("Modern Chemistry","chem_course", 8, chem_course_content, True)
default foodAndBeverage = Course("Food & Beverage Management","food_course", 7, food_course_content, True)

# The game starts here.
label start:
    call prologue
    if not started_before:
        "Unfortunately, you were not the chosen one."
        scene irl_background with SLOW_FADE
        "[WINTER_DAY] days later, winter arrives, and your tribe freezes to death."
        return
    call day_reset
    label .day_cycle:
        call day_start
        "Time to login"
        call meta_home
        scene irl_background with fade
        "I think it's time to report to chief."
        call end_day
        #scene transition
        call day_reset
        jump start.day_cycle
    return
#Day end, reset
label day_reset:
   scene blank with fade
   if day >= WINTER_DAY:
      #game ends.
      $day+=1
      "The sun rises again... DAY [day]"
      "Winter has arrived. The enemy tribe has come to attack."
      jump game_end
   else:
      #reset battery life of device.
      $actions_done_for_day = 0
      $daily_summary = ""
      $day+=1
   "The sun rises again... DAY [day]"
   return
label game_end:
   if end_state == 0:
      show irl_background with SLOW_FADE
      "After all the time spent in the Metaverse, nothing of value was gained. The tribe has collapsed."
   elif end_state == 1:
      show irl_background with SLOW_FADE
      if weapons_success:
         "Your tribemen are ill, the battle is very unsuccessful. Although your tribe eliminated the enemy, they destroied the facilities"
      else:
         "After all the time spent in the Metaverse, nothing of value was gained. The tribe has collapsed."
   elif end_state == 2:
      #Check if all 3 objectives are done, or only 2 of the 3.
      #TODO: edit dialogue
      if (weapons_success and purifier_success):
         "The damaged generator has stopped working."
         "Huge sacrifice was made. You lost your leg. But your tribe control the enemy tribe’s facilities"
         #chief "With weapons and the water purifier working, our tribe can still survive the winter."
      if (weapons_success and generator_success):
         "Huge sacrifice was made. You lost your leg. But your tribe control the enemy tribe’s facilities"
      if(purifier_success and generator_success):
         "Being greedy on your tribe’s winter reservation, the enemy tribe launched a raid. Your tribe hardly defended the besiege. People cannot get out for food. Many people might die during the winter"
         "OK ENDING"
   else:
      "You tribe has enough reservation for the winter and defend well against enemy tribe. You decide to slaughter the tribe or not"
      "GOOD ENDING"
   return
