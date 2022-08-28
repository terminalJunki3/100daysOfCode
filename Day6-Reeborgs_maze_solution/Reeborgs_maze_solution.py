# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():
        if not wall_on_right():
            turn_right()
        move()

    elif not front_is_clear() and not wall_on_right():
        turn_right()
        move()

    elif not front_is_clear() and wall_on_right():
        turn_left()

    elif front_is_clear() and not wall_on_right():
        turn_right()

    elif front_is_clear():
        move()

    else:
        turn_left()