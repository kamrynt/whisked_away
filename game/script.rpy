# The script of the game goes in this file.

style white_text is text:
    color "#ffffff"

style example_button is default:
    xpadding 10
    ypadding 5
    ymargin 7
    hover_sound ""
    activate_sound ""

style example_button_text:
    xalign 0.5
    idle_color "#ffffff"
    hover_color "#c0c0c0"

style example_bar is default:
    left_bar Frame ("bar full idle.png", 4,0)
    hover_left_bar Frame ("bar full hover.png", 4,0)
    right_bar Frame ("bar empty idle.png", 4,0)
    hover_right_bar Frame ("bar empty hover.png", 4,0)
    ysize 30

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define s = Character("Sister", color="#ffffff")

transform farright:
    xalign 1.0
    yalign 1.0

define startgame = Dissolve(1.0)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    
    pause .5
    #you need to add this
    play music "starting-music.mp3" fadeout 1

    scene bg kitchen
    with vpunch

    "{font=DejaVuSans-Bold.ttf}BANG{/font}"

    "{i}What the-{/i}"

    show sister happy at farright
    with Dissolve(.5)

    s"Come on Rookie let's get a move on"

    s"Instead of dazing off into space and catching flying ladles lets get our head in the game"

    "{i}We're so nervous about this exam, it's like the day i've been waiting for has finally arrived{/i}"

    "I'm so scared"

    s"Anxious"

    s"You're nervous about the unknown, you don't even know what it actually is that you're afraid of'"
    
    "I guess you're right"

    s"I've never been wrong"

    "I'm recalling a time when you were so convinced that you should store hot sauce in pantry"

    s"I don't give a fuck what the bottle says, I'm not having cold hot sauce."

    s"Jokes aside, you got this ..."

    s"Your journey is just beginning and I'm gonna do everything in my power to see you flourish.
"
    

    menu:

        s"How do you feel about the test"

        "I was born ready!":
            jump choice1_one
        "I need more time.":
            jump choice1_two
        "How exactly are you gonna help":
            jump choice1_three

    label choice1_one:

    $ menu_flag = True

    s "That’s the spirit. Let’s start simple"

    jump choice1_done

    label choice1_two:

    $ menu_flag = False

    s "All good, take a second to gather yourself and come see me when you are ready. Don’t take too long though"

    scene bg bathroom

    "I need to get it together"
    "It's a little shocking that I am feeling so nervous. Perhaps that's how I've always been."
    "I'm scared to fail"

    "{i}It's a picture of us. We were so little{/i}"

    scene bg kitchen
    "What are we working on first"
    jump choice1_done

    label choice1_three:

    $ menu_flag = False

    s "Don't you know who you're talking to? I'm not new to this, I'm true to this."

    "{i}I know she blossomed from a single rose into a whole bush full of them but she's never told me everything. I never could get her to tell me why{/i}"

    #play a movie of her using her phone and scrolling through pictures

    s "I remember my dys aat the academy like it was yesterday"

    "Hasn't it been almost 4 years?"

    s "Yeah yeah. Four years ago changed my whole life"

    s "The academy is going to unlock your untapped potential. The first thing that you need to do is pass."

    s"So I'm going to make sure you pass by practicing a dish with you that you can use for the entrance exam"

    jump choice1_done

label choice1_done:

    hide sister

    s"I can chill here while you clean the kitchen"

label tutorial:

    "{color=#0080c0}Drag{/color} the items to their appropriate position"

label tutorial__done:

    image sister animated:
        "sister vhappy"
        pause .5
        "sister happy"
        pause .5
        repeat 2

    show sister animated

    # This ends the game.

    return
