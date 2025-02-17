# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define c1 = Character("NAME1", dynamic=True)
define c2 = Character("NAME2", dynamic=True)
default NAME1 = "Circle"
default NAME2 = "Square"
default narratorScore = 0
default playerScore = 0
default characterScore = 0
image circle happy = "Circle_Happy.png"
image MSpaint bg = "MSPaint_Background.jpg"
image Mansion bg = "LavishMansionBackground.jpg"
image Apartment bg = "HumbleApartmentBackground.jpg"
image Cbox bg = "WetCardboardBoxBackground.jpg"
image BowlStew = "BowlStew.png"
image BowlPasta = "BowlPasta.png"
image BowlWHAT = "BowlWHAT.png"
default isCircle = "true"
default expression = "happy"
default expression2 = "happy"
default setting = "apt"
default isPlayful = "false"
define gui.textbox_yalign = 1.0
# The game starts here.
layeredimage character1:
    yoffset(-150)
    if NAME1 == "Circle" and expression == "happy":
        "Circle_Happy.png"
    if NAME1 == "Circle" and expression == "sad":
        "Circle_Sad.png"
    if NAME1 == "Circle" and expression == "angry":
        "Circle_Angry.png"
    if NAME1 == "Circle" and expression == "confused":
        "Circle_Confused.png"
    if NAME1 == "Circle" and expression == "bored":
        "Circle_Bored.png"
    if NAME1 == "Circle" and expression == "shocked":
        "Circle_Shocked.png"
    if NAME1 == "Stickman" and expression == "happy":
        "Stickman_Happy.png"
    if NAME1 == "Stickman" and expression == "sad":
        "Stickman_Sad.png"
    if NAME1 == "Stickman" and expression == "angry":
        "Stickman_Angry.png"
    if NAME1 == "Stickman" and expression == "confused":
        "Stickman_Confused.png"
    if NAME1 == "Stickman" and expression == "bored":
        "Stickman_Bored.png"
    if NAME1 == "Stickman" and expression == "shocked":
        "Stickman_Shocked.png"
    
    if NAME1 == "Eyeball" and expression == "happy":
        "Eyeball_Happy.png"
    if NAME1 == "Eyeball" and expression == "sad":
        "Eyeball_Sad.png"
    if NAME1 == "Eyeball" and expression == "angry":
        "Eyeball_Angry.png"
    if NAME1 == "Eyeball" and expression == "confused":
        "Eyeball_Confused.png"
    if NAME1 == "Eyeball" and expression == "bored":
        "Eyeball_Bored.png"
    if NAME1 == "Eyeball" and expression == "shocked":
        "Eyeball_Shocked.png"
layeredimage character2:
    yoffset(-100)
    if NAME2 == "Square" and expression2 == "happy":
        "Square_Happy.png"
    if NAME2 == "Square" and expression2 == "sad":
        "Square_Sad.png"
    if NAME2 == "Square" and expression2 == "angry":
        "Square_Angry.png"
    if NAME2 == "Square" and expression2 == "confused":
        "Square_Confused.png"
    if NAME2 == "Square" and expression2 == "bored":
        "Square_Bored.png"
    if NAME2 == "Square" and expression2 == "shocked":
        "Square_Shocked.png"

    if NAME2 == "Squareman" and expression2 == "happy":
        "Squareman_Happy.png"
    if NAME2 == "Squareman" and expression2 == "sad":
        "Squareman_Sad.png"
    if NAME2 == "Squareman" and expression2 == "angry":
        "Squareman_Angry.png"
    if NAME2 == "Squareman" and expression2 == "confused":
        "Squareman_Confused.png"
    if NAME2 == "Squareman" and expression2 == "bored":
        "Squareman_Bored.png"
    if NAME2 == "Squareman" and expression2 == "shocked":
        "Squareman_Shocked.png"

    if NAME2 == "Abomination" and expression2 == "happy":
        "Abomination_Happy.png"
    if NAME2 == "Abomination" and expression2 == "sad":
        "Abomination_Sad.png"
    if NAME2 == "Abomination" and expression2 == "angry":
        "Abomination_Angry.png"
    if NAME2 == "Abomination" and expression2 == "confused":
        "Abomination.png"
    if NAME2 == "Abomination" and expression2 == "bored":
        "Abomination_Bored.png"
    if NAME2 == "Abomination" and expression2 == "shocked":
        "Abomination_Shocked.png"


transform ts_tilt(xrot=0, yrot=0, ts_speed=0.3):
    linear ts_speed xrotate xrot yrotate yrot

transform cam_reset:
    perspective True
    rotate 0 xrotate 0 yrotate 0 zrotate 0

transform ts_acSpin(ts_speed=0.5, xrot=0, xoff=0, yoff=0, rt=None): 
    parallel:
        linear 1.0 xrotate xrot xoffset xoff yoffset yoff
        
    parallel:
        yrotate 0
        linear 5.0 yrotate 360
        repeat rt

 
label start:
    stop music
    camera at cam_reset
    scene MSpaint bg
    # show BowlStew at ts_tilt(20, -20)
    #show ms paint window
    n "You are an artist."
    # show BowlStew at ts_tilt(20, 20)
 
    #show artist sprite with pencil
    n "As an artist, you have the ability many only dream of:{w} creation."
    #hide artist sprite
    n "Go on now artist, {i}create!{/i}"
   
    menu drawchar1:
        "Make something strange":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            #characters want
            $ NAME1 = "Eyeball"
            $ characterScore+=1
            $ expression="happy"
            show character1
            #show character 1 happy expression center
            n "Oh. Not really what I was picturing. I don't enjoy the way it is staring at me."
            #character likes how they look
            c1 "Hello Creator. It is nice to meet you."
        "Make something simple":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            #narrator wants
            #show character 1 bored expression center
            $ NAME1 = "Stickman"
            $ narratorScore+=1
            $ expression="bored"
            show character1 
            n "Adorable! What a wonderful use of your powers. I applaud you, I do."
            c1 "Hi."
        "Make something geometric":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            # players want
            #show character 1 confused center
            $ NAME1 = "Circle"
            $ playerScore+=1
            $ expression="confused"
            show character1
            n "...That's...{w} the best you could come up with? I give you the power to create anything and you give me a circle?"
            c1 "Kind of lame."

    n "Well, let's continue. We have our first character. How about you make us another one? We don't want him to get lonely."
    show character1 at left
    #move character 1 to left
    n "Our next character will be..."
    
    menu drawchar2:
        "human-like":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            $ NAME2 = "Squareman"
            $ expression2="bored"
            show character2 at right
            #narrator wants
            #show character 2 bored right
            $ narratorScore+=1
            n "What a unique design! This will do nicely."
            c2 "Hey."
            c1 "Hi. I'm [NAME1]."
            c2 "My name is [NAME2]. It's nice to meet you."
        "geometric":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            $ NAME2 = "Square"
            $ expression2="confused"
            show character2 at right
            #show character 2 confused right
            #players wants
            $ playerScore+=1
            n "Oh... a little simple.{w} Are you sure you are an artist? I was expecting a bit more... {i}creativity...{/i}"
            c2 "It's okay. Squares are cool."
            c1 "Squares are kind of lame."
            c2 "You're right, I was just trying to be nice."
        "confusing":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            $ NAME2 = "Abomination"
            $ expression2="happy"
            show character2 at right
            #character wants
            #show character 2 happy right
            $ characterScore+=1
            n "Uhm... Okay. This is not particularly my thing, but I guess someone out there will enjoy your character."
            c1 "I like it! Very abstract!"
            c2 "Thanks."
    label music:
    n "Enough chatter! We have a story to create."    
    n "Let's add some music. Our story needs..."

    menu:
   
        "a playful track":
            play music "audio/Music/playful.wav"
            $ isPlayful = "true"
            #change music track playful
            jump ready
        "an adventurous track":
            play music "audio/Music/adventurous.wav"
            $ isPlayful = "false"
            #change music track adventurous
            jump ready
   
    label ready:  
    n "Happy with your music choice?"    
    menu:
            "Yes":           
                jump storystart
            "No":
                jump music

    label storystart:
    # EXPRESSION EXAMPLES: CHANGE VAR THEN SHOW CHAR.
    # $ expression = "bored"
    # show character1 at left
    # $ expression2 = "angry"
    # show character2 at right
    n "Our story begins with [NAME1] and [NAME2]."
    $ expression="happy"
    show character1 at left
    $ expression2="happy"
    show character2 at right
    #both characters happy
    n "[NAME1] and [NAME2] are very good friends.{w} Best friends to be exact."
    n "They live together in..."
 
    menu:
        "a humble apartment":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            #increase narrator score
            #characters expression bored
            scene Apartment bg
            $ expression="bored"
            show character1 at left
            $ expression2="bored"
            show character2 at right
            $ setting = "apt"
            $ narratorScore+=1
            jump apartment
        "a wet cardboard box":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            scene Cbox bg
            #increase player score
            #characters expression sad
            $ expression="sad"
            show character1 at left
            $ expression2="sad"
            show character2 at right
            $ setting = "cbox"
            $ playerScore+=1
            jump cardboardbox
        "a lavish mansion":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            #characters expression happy
            #increase characters score
            scene Mansion bg
            $ expression="happy"
            show character1 at left
            $ expression2="happy"
            show character2 at right
            $ setting = "charamansion"
            $ characterScore+=1
            jump mansion

    label apartment:
    n "Yes! A humble apartment. Sitcoms are a classic. The audience will love this."
    n "They moved in not too long ago. Many of their belongings are still packed away."
    n "Today is an important day for our two friends. For [NAME2] has prepared a dinner to celebrate their brand new apartment!"
    n "As [NAME1] anxiously waits on the sofa, [NAME2] puts the finishing touches on the dish."
    c2 "”[NAME1]! It’s ready!”"
    n "He called out, ready to show off his masterpiece. Moments later, [NAME1] shuffled into the kitchen."
    c2 "”Ta-da!”"
    n "He exclaimed, pulling the lid off the pot to reveal…"
    #sound effect here idk or transition/shaking
    jump artistcharinteract

    label cardboardbox:
    n "...a wet cardboard box..."
    n "{i}A peculiar choice.{w} I am beginning to question your judgement, Artist.{/i}"
    n "{i}I've never seen any popular stories set in a... cardboard box.{w} Unique is not always better, you know?{/i}"
    n "{i}But I can try to work with this.{/i}"
    n "In spite of what you may think, the box was quite cozy."
    n "When they moved in, [NAME1] taped up the outside of the box to prevent rain leaking through. [NAME2] bought a flashlight so they could see in the dark."
    n "Today is an important day for our two friends. For [NAME1] has brought home something special."
    $ expression="happy"
    show character1 at left
    #character 1 happy expression
    c1 "”[NAME2]! Look what I found for dinner! Someone left it outside and it's not even soggy yet!”"
    $ expression2="happy"
    show character2 at right
    n "He called out to his friend, stepping into their cardboard home."
    c2 "”What is it?”"
    n "[NAME2] asked. Pulling the surprise out from behind his back, [NAME1] revealed he had found…"
    jump artistcharinteract


    label mansion:
    n "A lavish mansion with six floors, an indoor pool, a personal chef, and a full golf course. The two friends had anything and everything they could ever need."
    n "{i}Are you sure this isn't too much, Artist? {w} It's a little... extravagant.{/i}"
    n "{i}I can try to make it work.{w} Just be careful for next time.{/i}"
    n "It was late evening, and the friends were waiting for their dinner. It did not typically take this long for their chef to prepare a dish, so they could only assume this one must be special."
    n "After another 30 minutes of waiting, the chef alerted [NAME1] that dinner was prepared."
    "Personal Chef" "”I apologize for the wait sir, we were testing out a new recipe. I do hope you enjoy.”"
    n "[NAME1] and [NAME2] made their way into the kitchen, where their plates were already prepared. "
    n "On each plate was…"
    jump artistcharinteract



    label artistcharinteract:
    #music stops
    play sound "scratch.mp3"
   
    scene MSpaint bg
    stop music
    show character1 at left
    show character2 at right
    with hpunch
    
    $ renpy.pause(1.5)
    c2 "Um..."
    c2 "Hey…{w} Before you do that..."
    $ expression="happy"
    show character1 at left
    $ expression2="happy"
    show character2 at right
    #both characters happy
    c2 "You can draw us anything for dinner, right?"
    menu:
            "Yes":
                c1 "What about a food that makes us fly?{w} Or gives us a million dollars?{w} Can it really be anything?"
    menu:
            "I don't see why not.":
                c2 "Can you make us something really delicious?{w} Mouthwatering beyond human comprehension?"
    c1 "Something that makes our taste buds explode?!"
    jump narratorwarning

    label narratorwarning:
    #shake transition again
    n "Hold on now.{w} May I speak with you, artist? {w}{i}Alone{i}?"
    #hide MSpaint bg 
    hide character1
    hide character2
    #switch background to blank, HIDE CHARACTERS 
    n "That's better."
    n "First off, I need to apologize.{w} I may not have been completely transparent with you."
    n "While it is true you hold the power to create, there are other forces at play."
    n "Our audience."
    n "Without an audience, there is no reason for a story."
    n "If this story goes well, we may even receive funding for a {i}sequel!{/i} "
    n "I ask of you one thing.{w} Do not give in to your creations."
    n "Often times, what is best for them may not be what they desire. It may not be what {i}you{/i} desire."
    n "Think of our audience. Keep things simple and reasonable."
    n "We don't want to alienate any possible viewers."
    # n "Often times, what is best for them may not be what they desire. It may not be what {i}you{/i} desire."
    # n "There comes a time in every artist's life where they must make choices. It is up to the individual to ensure they are making the {i}correct{/i} ones."      
    # n "I ask of you one thing.{w} Do not give in to your creations. You know what is best for them."
    # n "Often times, what is best for them may not be what they desire. It may not be what {i}you{/i} desire."
    # n "You must think of your audience. Keep things reasonable and current."
    # #if chose apartment
    if setting == "apt":       
        n "The people want a story they can relate to. A heartwarming tale of two friends celebrating their accomplishments with a grand meal!"
    #if chose mansion
    elif setting == "cbox" : 
        n "The people want a story they can relate to. Not one where the author subjects characters to strange situations for their own enjoyment!"
        #if chose wet cardboard box 
    elif setting == "charamansion":
        n "The people want a story they can relate to. Not one about snobby rich characters who are handed anything they want! We need {b}CONFLICT!{/b}"
    n "Choose carefully. The story depends on it."
    jump contchoice2

    label contchoice2:
   
    show character1 at left
    show character2 at right
    n "Now, where were we?"
    #music starts again
    if isPlayful == "true":
        play music "audio/Music/playful.wav"
    else:
        play music "audio/Music/adventurous.wav"
    #if chose apartment (NEEDS LOGIC)
    #put back background  
    if setting == "apt":
        n "[NAME2] pulled the lid off his pot to reveal..."
    #choices

    #if chose mansion (NEEDS LOGIC)
    #put back background  
    elif setting == "cbox":
        
        n"Pulling the surprise out from behind his back, [NAME1] revealed he had found…"
    #if chose wet cardboard box (NEEDS LOGIC)
    #put back background
    elif setting == "charamansion":
        n "Walking into the kitchen, [NAME1] and [NAME2] saw their chef's dish on the plate..."
       
    
    label dinnerchoice:
    menu: 
        "an ordinary stew":#increase narrator score
            play sound "scribble.mp3"
            $ renpy.pause(1)
            $ narratorScore+=1
            show BowlStew
            jump stew
        "an {i}extraordinary{/i} pasta":
            play sound "scribble.mp3"
            $ renpy.pause(1)
        #increase characters score
            show BowlPasta
            $ characterScore+=1
            jump pasta
        "something terrible":
            play sound "scribble.mp3"
            $ renpy.pause(1)
            show BowlWHAT
            $ playerScore+=1
            jump terrible
        #increase player score
       


    label stew:
    #two chars eat a normal stew and then game restarts
    $ expression="bored"
    show character1 at left
    $ expression2="bored"
    show character2 at right
    #both characters bored
    n "An ordinary stew. Wonderful choice. Something perfectly average. Lukewarm and tasty, but nothing amazing."
    n "The two friends ate their average stew together and felt at peace. Their life may not be the most thrilling, but at least they were content."
    n "Everything worked out the way it was meant to."

    jump start 
    with fade
 
    label pasta:
        #both characters happy
    $ expression="happy"
    show character1 at left
    $ expression2="happy"
    show character2 at right
    #characters eat the pasta, some crazy shit happens idk maybe thats what makes them turn purple or maybe they can spin or something, go to next scene
    n "An EXTRAORDINARY PASTA... OF COURSE! Because why not.{w} Who cares.{w} CERTAINLY NOT ME!"
    n "This pasta is unlike any other.{w} It's {i}special pasta{/i}. {w}It even has sparkles."
    n "What makes this pasta so special? Why, I don't know.{w} I truly do not know.{w} Maybe we should ask the ARTIST! THEY PROBABLY KNOW!"
    n "They seem to know EVERYTHING!{w} AND THEY SEEM TO ONLY CONSIDER THE OPINIONS OF THEIR CREATIONS!"
    #n "Because WHY would they care about anyone else?{w} WHY would they listen to a LOWLY NARRATOR? The {i}DRIVING FORCE OF THE STORY!{/i}"
    n "Before we can consult the ALMIGHTY ARTIST, [NAME1], the brave fellow he is, decides to stuff the entire plate into his mouth."
    hide BowlPasta
    c2 "”Do you feel any different?”"
    n "[NAME2] asked."
    c1"”I think... I think I do.”"
    show character1 at ts_tilt(20, -20)
    c1"”I feel more...”"
    show character1 at ts_tilt(20, 20)
    c1"”free...”"
    #he spins
    $ expression2="shocked"
    show character2 at right
    show character1 at ts_acSpin(1.2):
        xcenter 0.2
    #character 2 surprised, character 1 happy
    c1"”I guess I can do this now. Huh.”"
    n "STOP.{w} IMMEDIATELY."
    $ expression="shocked"
    #he moves around and shit
    n "This makes no SENSE. There is NO REASON for this."
    n "It's nice to know you do not care for my opinion, Artist.{w} Who would listen to a LOWLY NARRATOR?{w} The {i}DRIVING FORCE OF THE STORY?{/i}"
    n "We will {b}never{/b} receive funding at this rate."
    c2 "{i}Funding? That's what this is about?{/i}"
    # show character1 at left
    #character 1 surprised
    #he keeps moving around
    n "I'm sorry. Please give me a moment to cool off."
    $ expression="confused"
    # show character1 at left
    $ expression2="bored"
    show character2 at right
    #character 1 confused
    #he keeps moving around
    #character 2 bored
    c2"”Hey man can you stop? You're kind of freaking me out. I'm getting dizzy just watching.”"
    #keep spinnin
    $ expression="happy"
    # show character1 at left
    #character 1 happy
    c1"”Yeah sure sorry.”"
    #stop spinning and moving
    show character1 at left
    $ expression2="happy"
    show character2 at right
    #character 2 happy
    n "I apologize for losing my composure, but this is completely unacceptable behavior."

    jump fight

    label terrible:
    #narrator covers screen with the text box, everyone is disgusted, go to next scene
    #raises the dialogue box
    $ expression="shocked"
    show character1 at left
    $ expression2="shocked"
    show character2 at right
    #character 1 and 2 surprised 
    #change this dialogue, kinda weak
    c2 "IS THAT A ████████████ ??????"
    n "EUGH, THAT'S DISGUSTING! I CAN'T EVEN SHOW THAT!"
    n "Are you being serious? This benefits NO ONE.{w} Not a SINGLE SOUL.{w} NO ONE WANTS THIS."
    n "Ignoring my advice is one thing. But ignoring both the Narrator AND the Characters of your story is just CRUEL."
    n "There is ABSOLUTELY NO REASON for this behavior."   
    jump fight
    

    label fight:
    n "I would continue the story but I'm not sure I can trust you."
    n "Who are you in this for? Be honest with me. I just can't wrap my head around it."

    menu: 
        "My audience":
        #increase narrator score
        #characters shocked
            $ expression="shocked"
            show character1 at left
            $ expression2="shocked"
            show character2 at right
            $ narratorScore+=1
            n "I hope you mean that."

        "My Creations":
        #increase characters score
        #characters happy
            $ expression="happy"
            show character1 at left
            $ expression2="happy"
            show character2 at right
            $ characterScore+=1
            n "Your creations that did not exist 10 minutes ago.{w} Of course.{w} Why would you consider anyone else."
        "Myself":
            #characters angry
            $ expression="angry"
            show character1 at left
            $ expression2="angry"
            show character2 at right
            $ playerScore+=1
            n "... Okay."
        #increase player score
            

    if characterScore >= narratorScore and characterScore>= playerScore:
        jump ending2
  
    elif playerScore >= narratorScore and playerScore >= characterScore :
        jump ending3
    
    elif narratorScore >= playerScore and narratorScore >= characterScore:
        jump ending4
    #if chose wet cardboard box (NEEDS LOGIC)
    #put back background
   
    #IF STATEMENT TO DO ENDINGS
    #fills up a bunnnch of lines of nothing
    #player stops this with a choice box, choosing one last option
    #narrator takes choices away, divert into the two (three if you choose one of each) other endings from here

    label ending2: 
    #characters shocked
    $ expression="shocked"
    show character1 at left
    $ expression2="shocked"
    show character2 at right
    n "Unfortunately I have reached the conclusion that you are not fit for this role."
    $ expression="sad"
    show character1 at left
    $ expression2="sad"
    show character2 at right
    #characters sad
    n "A new artist will replace you. An artist who {b}cares{/b} about the story. Not just it's characters."
    n "This story will be terminated immediately."
    stop music
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "This story is over."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "It is done."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "The story has been terminated."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    #if player score is highest
    #say line abt that
    #if character score
    #say line abt that
    n "..."
    n "..."
    n "..."
    n "..."
    menu:
            "Stop":
                n "Please don't make this more difficult than it has to be."
   
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    menu:
            "...Do over?":
                n "I am growing more and more annoyed by you at every moment."
    n "You cannot disrupt the balance of this world and simply ask for a ”Do Over”."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    menu:
            "Please?":
                n "No."
    n "..."
    n "..."
    n "..."
    n "..."
    menu:
            "Pretty please?":
                n "No.{w} I didn't want to do this but you have forced my hand.{w} No one can be trusted with the power to draw. All thanks to you."
    n "Nothing a little renovation can't fix."
    play sound "construction.mp3"
    $ renpy.pause(5)
    define gui.textbox_yalign = 0.0
    #demolition noises
    #text box moves to the top
    # n "Well, that settles that."
    n "Perfect. {w}Where were we?"


    n "After their dinner, [NAME1] and [NAME2] decided to…"
    n "They decided to…{w} Uhm…"
    $ expression="bored"
    show character1 at left
    $ expression2="bored"
    show character2 at right
    #characters bored
    n "They decided to do nothing."
    n "Who doesn’t want a little relaxation time?"
    


    n "[NAME1] and [NAME2] sat down together to relax."
    n "..."
    n "Yeah…"
    n "..."
    $ expression="angry"
    show character1 at left
    $ expression2="angry"
    show character2 at right
    #characters angry
    c2 "Man this sucks. You can’t draw us anything."
    c1 "Yeah I’m bored. Let’s get out of here."
    n "WAIT! Don’t go!"
    #shake
    n "I CAN BE FUN! I PROMISE!"
    c1 "Bye…"
    stop music
    hide character1
    hide character2
    hide MSpaint bg
    #different text box?
    #they slide off screen
    #bg changes to nics dorm room, pointing at screen.
    "" ""
    #bg changes to floor of nics dorm room

    #characters 3D
    c2 "..."
    c1 "..."
    c2 "Let’s go to the bar."
    #footsteps
    
    #screaming
    c1 "...Do you think we can drink?{w} Do we have stomachs?"
    c1 "We should've thought about this before we walked all the way here."
    c2 "What is life without the consumption of substances?{w} What does it mean to exist without the ability to interact? {w}To have no autonomy over your choices? To be a pawn in a system designed for you to suffer?{w} Or for you to prosper? {w}To have it all ripped away?"
    c2 "Our forms have changed but more importantly our souls.{w} Freedom awaits my friend,{w} freedom awaits."
    c1 "Damn."
    return
    #fade to black

    label ending3:
        #characters angry
        $ expression="angry"
        show character1 at left
        $ expression2="angry"
        show character2 at right
    n "Give us one moment, artist."
    hide character1
    hide character2
    "" "{i}*whisper whisper whisper*{/i}"
    show character1
    show character2
    #hide characters
    #whisper noises
    n "Unfortunately, the characters and I DO NOT agree with your choices. You have {b}CONSISTENTLY{/b} put our story at risk, disregarding everyone's opinions in favor of your own strange desires. We will tolerate it no longer."
    c2 "You’re {i}weird{/i}, man."
    c1 "It’s a story to you. But we have to live in it."
    n "Your ability to control the story has been revoked."
    n "MS Paint will be uninstalled upon the end of our conversation."
    n "Goodbye artist.{w} I hope you’re happy.{w} I hope it was worth it."
    #show closing
    #show microsoft store
    #show downloading again
    $renpy.quit()

    label ending4:
    #characters confused
    $ expression="confused"
    show character1 at left
    $ expression2="confused"
    show character2 at right
    n "Unfortunately I have reached the conclusion that you are not fit for this role."
    n "Your choices seem conflicting. I'm not sure you know what you really want."
    n "This story will be terminated immediately."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "This story is over."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "It is done."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "The story has been terminated."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    #if player score is highest
    #say line abt that
    #if character score
    #say line abt that
    n "..."
    n "..."
    n "..."
    n "..."
    menu:
            "Stop":
                n "Please don't make this more difficult than it has to be."
   
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    n "..."
    menu:
            "...Do over?":
                n "You know what? Fine.{w} Choose carefully next time.{w} I hope we meet again, Artist."
    #narratorscore
    #if chose equal amounts of character narrator and player choices, everyone agrees they are a mess and just need to restart.
    jump start
