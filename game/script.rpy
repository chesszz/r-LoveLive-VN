# You can place the script of your game in this file.

# DECLARE BACKGROUNDS
image bg classroom = "classroom.png"
image bg courtyard = "courtyard.png"
image bg darkroom = "darkroom.png"
image bg niceboat = "niceboat.jpg"

# DECLARE CHARACTERS
image rin uniform bag = im.FactorScale("rin.png", 0.5)

image shigure uniform = im.FactorScale("shigure.png", 0.3)

image shigure draw normal = im.FactorScale("shigure2.png", 1.5)
image shigure draw sad = im.FactorScale("shigure2_sad.png", 1.5)
image shigure draw yandere = im.FactorScale("shigure2_yandere.png", 1.5)
image shigure draw yandere nohand = im.FactorScale("shigure2_yandere_nohand.png", 1.5)
image shigure draw yandere blood = im.FactorScale("shigure2_yandere_blood.png", 1.5)

# Declare characters used by this game.
define Ahri = Character('Ahrigateaux', color='#00ff00')
define Ame = Character('Amelia')
define Cap = Character('Capsairin')
define Chz = Character('Chezz')
define Chun = Character('chun')
define Corn = Character('cornsplosion')
define Dal = Character('Dalliance')
define Esp = Character('Espoir')
define Zer = Character('headphonezero')
define Mig = Character('HeyMiggy', color='#ff2222')
define Rin = Character('HoshiRin-chan', color='#00ff00')
define Ins = Character('Insti', color="#2222ff")
define Katz = Character('-KatZayY-')
define Lake = Character('lakepower')
define Lnk = Character('link2110', color='#ff2222')
define MP = Character('MarcoPolo', color='#00ff33')
define MM = Character('MasterMirage', color='#00ff00')
define Mel = Character('-melodii-')
define Moc = Character('mochaw1ngz')
define Oxd = Character('Oxide')
define Phi = Character('PhiPhi')
define Shg = Character('Shigure')
define Dan = Character('-trueDan-')
define UEF = Character('UltimateEpicFailz', color='#ff2222')
define Xaf = Character('Xaftz', color='#ff8800')

# The game starts here.
label start:

    play music "Snow Halation (Off Vocal).mp3"
    scene classroom
    show rin uniform bag

    Ins "Hi! I am Insti."
    Ins "I live in Malaysia."

    hide rin 
    #show shigure uniform
    show shigure draw normal

    Ins "o7 Morning shigure"
    Shg ":heyguys: omg insti why are you here :pogchamp:"

    menu:
        "I..I..I was just revising my homework!":
            jump bad_end
        "I was waiting for you to come find me, Shigure-chan!":
            jump good_end

    label bad_end:
        show shigure draw sad
        Shg "Ah...I thought you were waiting for me... T_T"
        Ins "D..d..don't get the wrong idea! I just happened to be here doing stuff! Not like I was waiting for you or anything."

        show shigure draw normal
        Shg "In any case, shall we walk back home together?"
        Ins "Nah...I'm walking home with Melodii today, I'm going to ask melodii out tomorrow! I'm so excited :DDD"
        Ins "See ya o7"

        stop music 
        show shigure draw sad 
        Shg "..."

        scene darkroom
        with fade
        "Later that night, in Insti's room..."
        Ins "zzzz"
        Ins "melodii-chan....I wanna see your..."
        Ins "virgin..."
        Ins "poo-"

        show shigure draw yandere nohand
        play music "Cold Iron.mp3"
        Ins "WOAHHHHHHHHHHH WHAT THE FUCK SHIGURE WHY ARE YOU HERE IT'S 3AM??"
        Shg "Insti...I missed you so much....I followed you all the way home..."
        Ins "Wait WHAT. You followed me home?"
        Shg "I saw you and melodii...what the two of you did..."
        Shg "Unforgivable....."
        

        show shigure draw yandere blood
        with dissolve
        Shg "So I killed melodii before coming here..."
        Ins "Wha-"
        Shg "And now I'll kill you Insti, so that we'll be together forever... <3"
        Ins "Noooooooooooooooooooooooo"

        scene niceboat 
        play music "Lullaby of Open Eyes.mp3"
        with Fade(2.0, 1.0, 2.0)
        Shg "Insti....we'll be together forever now.."
        Shg "I'll never let you leave my side <3"
        "- BAD END - "

    return
