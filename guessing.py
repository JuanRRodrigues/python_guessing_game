print("""
****************************
Welcome to the Guessing Game
****************************
""")

secret_number: int = 42
totalRounds = 3

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
        print("Correct")
        break
    else:
        if (maior):
            print("Incorrect! Your Number is Greater than the Secret Number")
        elif (menor):
             print("Incorrect! Your number is Less than the Secret Number")


