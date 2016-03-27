# We will use this "start.rpy" file as the main controller of logic and sequences
# Refer to "imachine.rpy" for a template

# It will call scenes, and once they return here, we may use the return value to dictate game logic
# We can store variables (e.g. attraction values) using python statements starting with $ 
# Afterwards, we can then use if/else statements  (don't need to use $ to indicate Python code!)

# Each scene will be of the format "ROUTE_dayX_scY"
# So "gen_day1_sc2" means the 2nd scene of the 1st day of the generic route
# All scenes of the same route and day will be stored in the same rpy file.
# Typically scenes are separated at convenient plot transitions, or whenever there is a menu


# The game starts here.
label start:
    
    call gen_day1_sc1
    if _return == "Mel":
        $ attr_mel += 1
    else:
        $ attr_shg += 1

    if attr_mel > 0:
        call gen_day2
    else:
        call gen_day3

    return