from dice import Dice

def set_top_face_is_valid():
    # we create our dice object we want to test things on
    dice = Dice()
    # dice initialises with its top face value as 1 we want to check that the initial value of the top face is indeed 1
    assert dice.top_face == 1 

    # next we check if our set top face returns true, because we are giving our top face value a correct value, we expect for the function to return true
    assert dice.set_top_face(3) == True
    # now we want to check that our set top face function changed the top face from 1 to 3
    assert dice.top_face == 3 

def set_top_face_is_invalid():
    dice = Dice()
    assert dice.top_face == 1 

    # since we have an invalid input here, we want to check if the function returns false
    assert dice.set_top_face(7) == False
    # we also want to check if the function keeps the same top face as before 
    assert dice.top_face == 1

set_top_face_is_valid()
set_top_face_is_invalid()

