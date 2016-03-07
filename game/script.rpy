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

    $ day = 0

    call gen_day1
    $ day += _return

    if day == 2:
        call gen_day2
    else:
        call gen_day3

    return
