# Remember that at the start of every day, we need to update the date! 
# And then re-show the calendar to update the visuals! 

label gen_day3:
    $ date, day_name = update_calendar_date(new_date=3)
    show screen calendar(date, month, day_name)

    Shg "I love you back!"
    "Attraction to Melodii: [attr_mel]\nAttraction to Shigure: [attr_shg]"