import random

def play():
    print("""
    ****************************
    Welcome to the Guessing Game
    ****************************
    """)

    secret_number: random.randrange(1, 101)
    totalRounds = 3
    points = 1000

    print("What level of difficulty? ")
    print("(1) Easy (2) Moderate (3) Hard")

    difficulty = int(input("Define the level: "))

    if(difficulty == 1):
        totalRounds = 20
    elif(difficulty == 2):
        totalRounds = 10
    elif(difficulty == 5):
        totalRounds = 5

    for round in range(1, totalRounds + 1):
        print("Round {} of {}".format(round, totalRounds))

        number_user = input("Enter Your Number between 1 and 100: ")
        print("Your Typed: ", number_user)
        number_user = int(number_user)

        if(number_user < 1 or number_user > 100):
            print("You must enter a number between 1 and 100")
            continue
        correct = secret_number == number_user
        maior = number_user > secret_number
        menor = number_user < secret_number

        if (correct):
            print("Correct!! You scored: {} points".format(points))
            break
        else:
            if (maior):
                print("Incorrect! Your Number is Greater than the Secret Number")
            elif (menor):
                 print("Incorrect! Your number is Less than the Secret Number")
            lost_points = abs(secret_number - number_user) #40-60 = 20
            points = points - lost_points

if(__name__ == "__main__"):
    play()


