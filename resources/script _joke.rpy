# You can place the script of your game in this file.

init python:
    def import_images():
        for filename in renpy.list_files():
            if not filename.startswith("images/"):
                continue
            if filename[-4:] not in (".png", ".jpg"):
                continue 

            # Split by directories. Ignore the directory structure, only take the last part (filename)
            img_name = filename.split("/")[-1]
            # Split by ".", discard the last part (file extension)
            img_name = "".join(img_name.split(".")[:-1])
            # Split by "_", this will be the descriptor name. Join the various parts by a space
            img_desc = " ".join(img_name.split("_"))
            renpy.image(img_desc, filename)     

    import_images()
    

# The game starts here.
label start:

    # Initialises the list of characters with their names and color
    python:
        import json
        init_data = json.load(renpy.file("init_data.json"))
        for char in init_data["chars"]:
            exec("{0} = Character('{1}', color='{2}')".format(char["nick"], char["name"], char["color"]))

    play music "bgm/Snow Halation (Off Vocal).mp3"
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
        play music "bgm/Cold Iron.mp3"
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
        play music "bgm/Lullaby of Open Eyes.mp3"
        with Fade(2.0, 1.0, 2.0)
        Shg "Insti....we'll be together forever now.."
        Shg "I'll never let you leave my side <3"
        "- BAD END - "

    return
