# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define c1 = Character("NAME1", dynamic=True)
define c2 = Character("NAME2", dynamic=True)
default NAME1 = "Circle"
default NAME2 = "Square"
default NAME3 = "Squareman"
default NAME4 = "Stickman"
default narratorScore = 0
default playerScore = 0
default characterScore = 0
image chappy = "Circle_Happy.png"
default isCircle = "true"
default expression = "happy"
default setting = "apt"

# The game starts here.
layeredimage character1:

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

layeredimage character2:

    if NAME2 == "Square" and expression == "happy":
        "Square_Happy.png"
    if NAME2 == "Square" and expression == "sad":
        "Square_Sad.png"
    if NAME2 == "Square" and expression == "angry":
        "Square_Angry.png"
    if NAME2 == "Square" and expression == "confused":
        "Square_Confused.png"
    if NAME2 == "Square" and expression == "bored":
        "Square_Bored.png"
    if NAME2 == "Square" and expression == "shocked":
        "Square_Shocked.png"

layeredimage character3:

    if NAME3 == "Squareman" and expression == "happy":
        "Squareman_Happy.png"
    if NAME3 == "Squareman" and expression == "sad":
        "Squareman_Sad.png"
    if NAME3 == "Squareman" and expression == "angry":
        "Squareman_Angry.png"
    if NAME3 == "Squareman" and expression == "confused":
        "Squareman_Confused.png"
    if NAME3 == "Squareman" and expression == "bored":
        "Squareman_Bored.png"
    if NAME3 == "Squareman" and expression == "shocked":
        "Squareman_Shocked.png"


layeredimage character4:

    if NAME4 == "stickman" and expression == "happy":
        "Stickman_Happy.png"
    if NAME4 == "stickman" and expression == "sad":
        "Stickman_Sad.png"
    if NAME4 == "stickman" and expression == "angry":
        "Stickman_Angry.png"
    if NAME4 == "stickman" and expression == "confused":
        "Squareman_Confused.png"
    if NAME4 == "stickman" and expression == "bored":
        "Stickman_Bored.png"
    if NAME4 == "stickman" and expression == "shocked":
        "Squareman_Shocked.png"
label start:
    show character1
    n "This is you.{w} You are an artist."
    #show artist sprite with pencil
    n "As an artist, you have the ability many only dream of:{w} creation."
    #hide artist sprite
    n "Go on now artist, {i}create!{/i}"
   

    menu drawchar1:
        "Make something ugly":
            #characters want
            $ characterScore+=1
            n "Oh. I guess that works. Not really what I was picturing."
            #character likes how they look
            c1 "Hello Creator. It is nice to meet you."
        "Make something simple":
            #narrator wants
            $ narratorScore+=1
            n "Adorable! What a wonderful use of your powers. I applaud you, I do."
            c1 "Hi."
        "Make something geometric":
            # players want
            $ playerScore+=1
            n "...That's...{w} the best you could come up with? I give you the power to create anything and you give me a circle?"
            c1 "Kind of lame."

    n "Well, let's continue. We have our first character. How about you make us another one? We don't want him to get lonely."
   
    n "Our next character will be..."
    
    menu drawchar2:
        "colorful":
            #narrator wants
            $ narratorScore+=1
            n "placeholder"
        "geometric":
            #players wants
            $ playerScore+=1
            n "placeholder"
        "confusing":
            #character wants
            $ characterScore+=1
            n "placeholder"

    label music:
    n "Let's add some music. Our story needs a..."

    menu:
   
        "playful track":
            #change music track
            jump ready
        "adventurous track":
            #change music track
            jump ready
   
    label ready:  
    n "Happy with your music choice?"    
    menu:
            "Yes":           
                jump storystart
            "No":
                jump music

    label storystart:
#[NAME1] and [NAME2] are placeholders, eventually they need to be replaced with variables 
#based on the character the player chooses

    n "Our story begins with [NAME1] and [NAME2]."
    n "[NAME1] and [NAME2] are very good friends.{w} Best friends to be exact."
    n "They live together in..."
 
    menu:
        "a humble apartment":
            #increase narrator score
            $ setting = "apt"
            $ narratorScore+=1
            jump apartment
        "a wet cardboard box":
            #increase player score
            $ setting = "cbox"
            $ playerScore+=1
            jump cardboardbox
        "a lavish mansion":
            #increase characters score
            $ setting = "charamansion"
            $ characterScore+=1
            jump mansion

    label apartment:
    n "Yes! A humble apartment. They moved in not too long ago. Many of their belongings are still packed away."
    n "Today is an important day for our two friends. For [NAME2] has prepared a dinner to celebrate their brand new apartment!"
    n "As [NAME1] anxiously waits on the sofa, [NAME2] puts the finishing touches on the dish."
    c2 "”[NAME1]! It’s ready!”"
    n "He called out, ready to show off his masterpiece. Moments later, [NAME1] shuffled into the kitchen."
    c2 "”Ta-da!”"
    n "He exclaimed, pulling the lid off the pot to reveal…"
    #sound effect here idk or transition/shaking
    jump artistcharinteract

    label cardboardbox:
    n "...a wet cardboard box...{w} Of course.{w}"
    n "In spite of what you may think, the box was quite cozy."
    n "When they moved in, [NAME1] taped up the outside of the box to prevent rain leaking through. [NAME2] bought a flashlight so they could see in the dark."
    n "Today is an important day for our two friends. For [NAME1] has brought home something special."
    c1 "”[NAME2]! Look what I found for dinner in the garbage can!”"
    n "He called out to his friend, stepping into their cardboard home."
    c2 "”What is it?”"
    n "[NAME2] asked. Pulling the surprise out from behind his back, [NAME1] revealed he had found…"
    jump artistcharinteract


    label mansion:
    n "A lavish mansion with six floors, an indoor pool, a personal chef, and a full golf course. The two friends had anything and everything they could ever need."
    n "It was late evening, and the friends were waiting for their dinner. It did not typically take this long for their chef to prepare a dish, so they could only assume this one must be special."
    n "After another 30 minutes of waiting, the chef alerted [NAME1] that dinner was prepared."
    "Personal Chef" "I apologize for the wait sir, we were testing out a new recipe. I do hope you enjoy."
    n "[NAME1] and [NAME2] made their way into the kitchen, where their plates were already prepared. "
    n "On each plate was…"
    jump artistcharinteract



    label artistcharinteract:
    #music stops
    c2 "Hey… Sorry to interrupt."
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
    #switch background? remove characters, 
    n "That's better."
    n "There comes a time in every artist's life where they must make choices. It is up to the individual to ensure they are making the {i}correct{/i} ones."      
    n "I ask of you one simple thing.{w} Do not give in to your creations. You know what is best for them."
    n "Often times, what is best for them may not be what they desire. It may not be what {i}you{/i} desire."
    n "You must think of your audience. Keep things reasonable and current."
    # #if chose apartment (NEEDS LOGIC)
    if setting == "apt":       
        n "The people want a story they can relate to. A heartwarming tale of two friends celebrating their accomplishments with a grand meal!"
    #if chose mansion (NEEDS LOGIC)
    elif setting == "cbox" : 
        n "The people want a story they can relate to. Not one where the author subjects characters to strange situations for their own enjoyment!"
        #if chose wet cardboard box (NEEDS LOGIC)
    elif setting == "charamansion":
        n "The people want a story they can relate to. Not one about snobby rich characters who are handed anything they want! We need {b}CONFLICT!{/b}"
    n "Heed this warning. The story depends on it."
    jump contchoice2

    label contchoice2:
   
    n "Now, where were we?"
    #music starts again

    #if chose apartment (NEEDS LOGIC)
    #put back background  
    if setting == "apt":
        n "[NAME2] pulled the lid off his pot to reveal..."
    #choices

    #if chose mansion (NEEDS LOGIC)
    #put back background  
    elif setting == "cbox":
        n "Walking into the kitchen, [NAME1] and [NAME2] saw their chef's dish on the plate..."

    #if chose wet cardboard box (NEEDS LOGIC)
    #put back background
    elif setting == "charamansion":
        n"Pulling the surprise out from behind his back, [NAME1] revealed he had found…"
    
    label dinnerchoice:
    menu: 
        "an ordinary stew":#increase narrator score
            $ narratorScore+=1
            jump stew
        "an {i}extraordinary{/i} pasta":
        #increase characters score
            $ characterScore+=1
            jump pasta
        "something terrible":
            $ playerScore+=1
            jump terrible
        #increase player score
       


    label stew:
    #two chars eat a normal stew and then game restarts
    n "An ordinary stew. Something perfectly average. Lukewarm and tasty, but nothing amazing."
    n "The two friends ate their average stew together and felt at peace. Their life may not be the most thrilling, but at least they were content."
    n " Everything worked out the way it was meant to."
    return
 
    label pasta:
    #characters eat the pasta, some crazy shit happens idk maybe thats what makes them turn purple or maybe they can spin or something, go to next scene
    n "An EXTRAORDINARY PASTA... OF COURSE. Because why not. This pasta is unlike any other.{w} It's {i}special pasta{/i}. {w}It even has sparkles."
    n "What makes this pasta so special? Why, I don't know.{w} I truly do not know.{w}{b}MAYBE WE SHOULD ASK THE ARTIST.{/b}"
    n "Before we can do that, [NAME1], the brave fellow he is, decides to stuff the entire plate into his mouth."
    c2 "”Do you feel any different?”"
    n "[NAME2] asked."
    c1"”I think... I think I do.”"
    c1"”I feel more... free...”"
    #he spins
    c1"”I guess I can do this now. Huh.”"
    n "STOP THIS.{w} IMMEDIATELY."
    #he moves around and shit
    n "This makes no SENSE! There is no REASON behind these decisions!"
    #he keeps moving around
    c2"”Hey man can you stop? You're kind of freaking me out. I'm getting dizzy just watching.”"
    #keep spinnin
    c1"”Yeah sure sorry.”"
    n "This is completely unacceptable behavior."
    #stop spinning and moving
    jump fight

    label terrible:
    #narrator covers screen with the text box, everyone is disgusted, go to next scene
    #raises the dialogue box
    n "EUGH, THAT'S DISGUSTING! I CAN'T EVEN SHOW THAT!"
    n "Are you being serious? This benefits NO ONE.{w} Not a SINGLE SOUL.{w} NO ONE WANTS THIS."
   
    jump fight
    

    label fight:
    n "I would continue the story but I'm not sure I can trust you."
    n "Who are you in this for? Be honest with me. I just can't wrap my head around it."

    menu: 
        "My audience":
        #increase narrator score
            $ narratorScore+=1
            n "I hope you mean that."

        "My Creations":
        #increase characters score
            $ characterScore+=1
            n "Your creations that did not exist 10 minutes ago.{w} Of course.{w} Why would you consider anyone else."
        "Myself":
            $ playerScore+=1
            n "... Okay."
        #increase player score
            

    
    #IF STATEMENT TO DO ENDINGS
    #fills up a bunnnch of lines of nothing
    #player stops this with a choice box, choosing one last option
    #narrator takes choices away, divert into the two (three if you choose one of each) other endings from here

    label ending2: 
    n "Unfortunately I have reached the conclusion that you are not fit for this role."
    n "A new artist will replace you."
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
                n "No.{w} I didn't want to do this but you have forced my hand."
    #demolition noises
    #text box moves to the top
    n "Well, that settles that."
    n "Where were we?"


    n "After their dinner, [NAME1] and [NAME2] decided to…"
    n "They decided to…{w} Uhm…"
    n "They decided to do nothing."
    n "Who doesn’t want a little relaxation time?"
    


    n "[NAME1] and [NAME2] sat down together to relax."
    n "..."
    n "Yeah…"
    n "..."
    # n "They’ve got a one way ticket to the relaxation station baby…{w}Haha…"
    c2 "Man this sucks. You can’t draw us anything."
    c1 "Yeah I’m bored. Let’s get out of here."
    n "WAIT! Don’t go!"
    #shake
    n "I CAN BE FUN! I PROMISE!"
    c1 "Bye…"
    #different text box
    #they slide off screen
    #bg changes to nics dorm room, pointing at screen.
    "" ""
    #bg changes to floor of nics dorm room

    c2 "..."
    c1 "..."
    c2 "Let’s go to the bar."
    #footsteps
    #screaming
    c1 "...Do you think we can drink?{w} Do we have stomachs?"
    c1 "We should've thought about this before we walked all the way here."
    c2 "What is life without the consumption of substances? What does it mean to exist without the ability to interact? To have no autonomy over your choices? To be a pawn in a system designed for you to suffer? Or for you to prosper? To have it all ripped away? Our forms have changed but more importantly our souls. Freedom awaits my friend, freedom awaits."
    c1 "Damn."
    return
    #fade to black

    label ending3:
    n "Give us one moment, artist."
    #characters leave the screen
    #whisper noises
    n "Unfortunately, the characters and I have decided that we DO NOT agree with your choices. You have {b}CONSISTENTLY{/b} put our story at risk, and we will tolerate it no longer."
    c2 "You’re {i}weird{/i}, man."
    c1 "It’s a story to you. But we have to live in it."
    n "Your ability to control the story has been revoked."
    n "MS Paint will be uninstalled upon the end of our conversation."
    n "Goodbye artist.{w} I hope you’re happy.{w} I hope it was worth it."
    #show closing
    #show microsoft store
    #show downloading again
    return

    label ending4:
    n "placeholder"
    #narratorscore
    #if chose equal amounts of character narrator and player choices, everyone agrees they are a mess and just need to restart.
    return
