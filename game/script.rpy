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

    def update_calendar(day, skip):
        new_day_int = int(day) + skip
        new_day = str(new_day_int)
        new_day_name = day_name_dict[str(new_day_int % 7)]

        return (new_day, new_day_name)

    # Registers all images in the images folder
    import_images()

    # Imprts the json data file
    init_data = import_init_data()

    # Initialises the list of characters with their names and color
    char_list = init_data["chars"]
    for char in char_list: 
        setattr(store, char["nick"], Character(char["name"], color=char["color"], show_two_window=True))

    # Initialises the list of attractions
    # Cannot use a dict/list because Renpy thinks that it is the same dictionary when we update it 
    # and so doesn't init it again (I think)
    attr_mel = 0
    attr_shg = 0
    
    # Initialises the calendar
    day = "1"
    month = "April"
    day_name_dict = {"0":"SUN", "1":"MON", "2":"TUE", "3":"WED", "4":"THU", "5":"FRI", "6":"SAT"}
    day_name = day_name_dict[day]

# The game starts here.
label start:
    show screen calendar(day, month, day_name)
    show classroom

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
