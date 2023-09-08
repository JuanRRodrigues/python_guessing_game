import guessing
import forca

def select_game():

    print("""
    ****************************
    ******Select your game******
    ****************************
    """)

    print("(1) Hangman (2) Guessing")

    game = int(input("Which game? ?"))

    if(game == 1):
        print("playing a Hangman Game.")
        forca.jogar()
    elif(game == 2):
        print("Playing a guessing Game.")
        guessing.jogar()

if(__name__ == "__main__"):
    select_game()
