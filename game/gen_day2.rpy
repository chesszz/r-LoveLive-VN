# Remember that at the start of every day, we need to update the date! 
# And then re-show the calendar to update the visuals! 

label gen_day2:
    $ date, day_name = update_calendar_date(new_date=2)
    show screen calendar(date, month, day_name)
    
    Mel "I hate you!"
    "Attraction to Melodii: [attr_mel]\nAttraction to Shigure: [attr_shg]"