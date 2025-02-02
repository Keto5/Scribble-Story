# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define c1 = Character("NAME1", dynamic=True)
define c2 = Character("NAME2", dynamic=True)
default NAME1 = "Guy"
default NAME2 = "Guy2"

# The game starts here.


label start:

    n "This is you.{w} You are an artist."
    #show artist sprite with pencil
    n "As an artist, you have the ability many only dream of:{w} creation."
    #hide artist sprite
    n "Go on now artist, {i}create!{/i}"
   
#menus are just choices.
    menu drawchar1:
        "Make something ugly":
            n "Oh. I guess that works. Not really what I was picturing."
            c1 "Hello Creator. It is nice to meet you."
        "Make something cute":
            n "Adorable! What a wonderful use of your powers. I applaud you, I do."
            c1 "Hi."
        "Make something geometric":
            n "...That's...{w} the best you could come up with? I give you the power to create anything and you give me a circle?"
            c1 "Kind of lame."

    n "Well, let's continue. We have our first character. How about you make us another one? We don't want him to get lonely."
   
    n "Our next character will be..."
    
    menu drawchar2:
        "colorful":
            n "placeholder"
        "geometric":
            n "placeholder"
        "confusing":
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

    n "Our story begins with [NAME1] and [NAME2]"
    n "[NAME1] and [NAME2] are very good friends.{w} Best friends to be exact."
    n "They live together in..."
 
    menu:
        "a humble apartment":
            #increase narrator score
            jump apartment
        "a wet cardboard box":
            #increase player score
            jump cardboardbox
        "a lavish mansion":
            #increase characters view
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
    n "placeholder where characters will ask for something"
    
    # c2 "Hey… Sorry to interrupt."
    # c2 "You can draw us anything for dinner, right?"
    # menu:
    #         "Yes":
    #             n "placeholdertext"
    #character asks for something not sure what yet
    jump narratorwarning

    label narratorwarning:
    n "Hold on now.{w} May I speak with you, artist? {w}{i}Alone{i}?"
    #switch background? remove characters, 
    n "That's better."
    n "There comes a time in every artist's life where they must make choices. It is up to the individual to ensure they are making the {i}correct{/i} ones."      
    n "I ask of you one simple thing.{w} Do not give in to your creations. You know what is best for them."
    n "Often times, what is best for them may not be what they desire. It may not be what {i}you{/i} desire."
    n "You must think of your audience. Keep things reasonable and current."
    #if chose apartment (NEEDS LOGIC)
    n "The people want a story they can relate to. A heartwarming tale of two friends celebrating their accomplishments with a grand meal!"
    #if chose mansion (NEEDS LOGIC)
    n "The people want a story they can relate to. Not one about snobby rich characters who are handed anything they want! We need {b}CONFLICT!{/b}"
    #if chose wet cardboard box (NEEDS LOGIC)
    n "The people want a story they can relate to. Not one where the author subjects characters to strange situations for their own enjoyment!"
    n "Heed this warning. The story depends on it."
    jump contchoice2

    label contchoice2:
   
    n "Now, where were we?"
    #music starts again

    #if chose apartment (NEEDS LOGIC)
    #put back background  
    n "[NAME2] pulled the lid off his pot to reveal..."
    #choices

    #if chose mansion (NEEDS LOGIC)
    #put back background  
    n "Walking into the kitchen, [NAME1] and [NAME2] saw their chef's dish on the plate..."

    #if chose wet cardboard box (NEEDS LOGIC)
    #put back background
    n"Pulling the surprise out from behind his back, [NAME1] revealed he had found…"
    
    label dinnerchoice:
    #need to ask group about dinner options :)

    return
