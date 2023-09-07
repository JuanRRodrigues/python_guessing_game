print("""
****************************
Welcome to the Guessing Game
****************************
""")

secret_number: int = 42
totalRounds = 3
round = 1

while(round <= totalRounds):
    print("Round {} of {}".format(round, totalRounds))
    number_user = input("Enter Your Number: ")
    print("Your Typed: ", number_user)
    number_user = int(number_user)

    correct = secret_number == number_user
    maior = number_user > secret_number
    menor = number_user < secret_number

    if (correct):
        print("Correct")
        round = 4
    else:
        if (maior):
            print("Incorrect! Your Number is Greater than the Secret Number")
        elif (menor):
             print("Incorrect! Your number is Less than the Secret Number")

        round = round + 1
