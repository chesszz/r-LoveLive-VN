# Remember that at the start of every day, we need to update the date! 
# And then re-show the calendar to update the visuals! 

label gen_day1_sc1:
    $ date, day_name = update_calendar_date(new_date=2)
    show screen calendar(date, month, day_name)

    show classroom
    show shigure draw normal
    
    Ins "Lorem ipsum dolor sit amet, consectetur adipiscing elit.  congue urna. Quisque sit amet ante a 
    enim consectetur eleifend. Etiam vel augue vitae nisi condimentum faucibus eu vel magna. Etiam libero ipsum, 
    imperdiet vel viverra a, placerat blandit"

    menu:
        "Do you like Melodii or Shigure?"

        "Melodii":
            return "Mel"
        "Shigure":
            return "Shg"

label gen_day1_sc2:
    Ins "Ah , whatever"