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
image cafe_room = "Backgrounds/Cafe.png"

image Generator_damaged = "Backgrounds/Generator_damaged.png"
image Generator_fixed = "Backgrounds/Generator_fixed.png"
image Water_Purifier_damaged = "Backgrounds/Water_Purifier_damaged.png"
image Water_Purifier_fixed = "Backgrounds/Water_Purifier_fixed.png"
image blank = "Backgrounds/black.jpg"
image WHITE = "Backgrounds/white.jpg"



image headset = "VR_Headset.png"
image headset_glowing = im.MatrixColor("VR_Headset.png",im.matrix.brightness(0.8) * im.matrix.tint(0.8, 0.8, 1.0))
image battery = "Battery.png"
image mirror = "Backgrounds/mirrorCG.png"
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

default game_end = False
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
default electricEngeering = Course("Electrical Engineering","ee_course", 16, ee_course_content, True, "Electrical engineering can be helpful for fixing things...")
default socialMediaMarketing = Course("Social Media Marketing","media_course", 5, media_course_content, True)
default cadAndDigital = Course("CAD And Digital", "cad_course", 10, cad_course_content, True)
default calc1 = Course("Calculus I", "math1_course", 10, math1_course_content, True)
default calc2 = Course("Calculus II", "math2_course", 10, math2_course_content, False)
default calc3 = Course("Calculus III", "math3_course", 10, math3_course_content, False)
default theoreticalPhysics = Course("Physics", "physics_course", 10, physics_course_content, True)
default modernChem = Course("Modern Chemistry","chem_course", 8, chem_course_content, True)
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
      if game_end:
         return
      call day_start
      "Time to login"
      call meta_home
      "I think it's time to report to chief."
      call end_day
      #scene transition
      call day_reset
      jump start.day_cycle
   return
#Day end, reset
label day_reset:
   scene blank
   if day >= WINTER_DAY:
      #game ends.
      # $day+=1
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
      chief "I am very disappointed in you."
      chief "We all had our hopes out for you, but not once did you repay them."
      chief "Now, we have no choice but to let our tribe be conquered and vanquish into the sands of time."
      "After all the time in the metaverse, you weren't able to gain anything of value."
      "How could you have spent so much effort with no return?"
   elif end_state == 1:
      show irl_background with SLOW_FADE
      if weapons_success: #purifier and energy don't worked
         "Although the your tribe has gained the ability to produce war-ready weapons, it wasn't enough to keep your tribe in good health."
         chief "A tribe's success does not depend on armaments alone. You should know that."
         chief "We have no energy to heat our shelters, nor clean water to use for agriculture or ourselves."
         chief "We may be safe from our enemies, but not from the winter."
         "Better luck next time"
      elif purifier_success #weapons and energy don't work
         "Your tribe has clean water. That'll be essential for maintaining good health and planting crops."
         "But what are you to do without energy or water."
         chief "I appreciate having a nice bath by the end of the day. But do you expect me to bathe in cold water by winter?"
         chief "We are also still in danger of being attacked from other tribes. Water alone won't help us any bit."
         chief "I expect more from you, Lynx"
         "Mastering the arduous course of Electrical Engineering, was simply not enough."
         "Unfortunate."
      else #only energy
         "Your tribe has energy to light up the their shelters and heat to survive through the winter."
         "Nevertheless, the welfare of your tribe is compromised."
         chief "Without weapons and clean water, our soldeirs' health will suffer significantly in war."
         chief "They deserve better than that."
         "Despite the miracle of the YouTube video, your fortune ended there."
   elif end_state == 2:
      if (weapons_success and purifier_success):
         "You have successfully found the blueprint to the weapons and fixed the water purifier."
         chief "With weapons and clean water, our troops should fare well against tribes in the winter."
         chief "Even though we have no generator to keep us warm, we are safe from invasions."
         chief "Whoever survives through the winter will survive. Who ever doesn't doesn't."
         chief "That's the hard truth."
         chief "But at the very least, our tribe will continue."
         chief "Thank you Lynx, your efforts are commendable."
      if (weapons_success and generator_success):
         "You have succesfully recovered the blue print and returned electricity to your tribe."
         chief "Not bad, Lynx. We will have heat for the winter and weapons to fare off the enemies."
         chief "In fact, we may be able to commandeer our neighboring tribes water purifier."
         chief "How does that sound?"
         "The chief seems to be in happy spirits."
         "While you are not entirely sure of that prospect, at least you have helped your tribe avert a major crisis."
      if(purifier_success and generator_success):
         "Choosing to prioritize on your tribe's well being over the winter, you also risk a possible invasion from the enemy tribe."
         chief "Our tribe will have enough resources to comfortably survive through the winter."
         chief "While we won't be able to fend off enemy tribes, it is unlucky that they will launch an attack during such harsh conditions."
         chief "In the mean time, we will focus on strengthening ourselves internally."
         chief "We appreciate your contributions."
   else:
      "You have managed to complete all the tasks."
      chief "What can I say Lynx?"
      chief "Where would our tribe be without you? Where would I be?"
      "The chief takes a moment to gather his thoughts."
      chief "This is a momentous occasion. Our tribe shall henceforth flourish!"
      chief "No more enemies to make fools of ourselves, no more diseases to ravage our populations, no more unbearable nights in the cold."
      chief "Today, We shall celebrate!"
      "Walking out of the throne room, he holds your hand."
      "Together, you proudly raise them up in triumph."

   return
