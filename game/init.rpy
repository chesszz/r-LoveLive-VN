#########################################################################################
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
    def import_init_data(pathname):
        import json
        return json.load(renpy.file(pathname))

    # Update the date by skip number of days
    def update_calendar_skip(curr_date, skip=1):
        new_date_int = int(curr_date) + skip
        new_date = str(new_date_int)
        new_day_name = day_name_dict[str(new_date_int % 7)]
        return (new_date, new_day_name)

    # Update the date by explicitly having the date
    def update_calendar_date(new_date):
        return (str(new_date), day_name_dict[str(new_date % 7)])

    # Registers all images in the images folder
    import_images()

    # Imports the json data file
    init_data = import_init_data("init_data.json")
    # Initialises the list of characters with their names and color
    # store is the default namespace in which we save variables
    char_list = init_data["chars"]
    for char in char_list: 
        setattr(store, char["nick"], Character(char["name"], color=char["color"], show_two_window=True))

    # Initialises the attraction variables
    # Cannot use a dict/list because Renpy thinks that it is the same dictionary when we update it 
    # and so doesn't init it again (I think)
    attr_mel = 0
    attr_shg = 0
    
    # Initialises the calendar
    date = "1"
    month = "April"
    day_name_dict = {"0":"SUN", "1":"MON", "2":"TUE", "3":"WED", "4":"THU", "5":"FRI", "6":"SAT"}
    day_name = day_name_dict[date]

    style.default.font = "fonts/MotoyaLMaru.ttf"

#########################################################################################


