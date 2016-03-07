# You can place the script of your game in this file.

init python:

    # Searches through all images in the images/ folder with the desired formats
    # Splits their names based on the underscore "_" separator and uses these as the descriptor
    def import_images(formats=(".png", ".jpg")):
        for filename in renpy.list_files():
            if not filename.startswith("images/"):
                continue
            if filename[-4:] not in formats:
                continue 

            # Split by directories. Ignore the directory structure, only take the last part (filename)
            img_name = filename.split("/")[-1]
            # Split by ".", discard the last part (file extension)
            img_name = "".join(img_name.split(".")[:-1])
            # Split by "_", this will be the descriptor name. Join the various parts by a space
            img_desc = " ".join(img_name.split("_"))
            # Registers it with Renpy
            renpy.image(img_desc, filename)

    # Gets the json file and loads it
    def import_init_data(pathname="init_data.json"):
        import json
        return json.load(renpy.file(pathname))     

    # Registers all images in the images folder
    import_images()

    # Imprts the json data file
    init_data = import_init_data()

    # Initialises the list of characters with their names and color
    char_list = init_data["chars"]
    for char in char_list: 
        exec("{0} = Character('{1}', color='{2}')".format(char["nick"], char["name"], char["color"]))

    # Initialises the list of attractions
    # Cannot use a dict/list because Renpy thinks that it is the same dictionary when we update it 
    # and so doesn't init it again (I think)
    attr_mel = 0
    attr_shg = 0


# The game starts here.
label start:

    call gen_day1
    if _return == "Mel":
        $ attr_mel += 1
    else:
        $ attr_shg += 1

    if attr_mel > 0:
        call gen_day2
    else:
        call gen_day3

    return
