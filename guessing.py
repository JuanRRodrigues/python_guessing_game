print("""
****************************
Welcome to the Guessing Game
****************************
""")

secret_number: int = 42

number_user = input("Enter Your Number: ")
number_user = int(number_user)

correct = secret_number == number_user
maior = number_user > secret_number
menor = number_user < secret_number

print("Your Typed: ", number_user)

if (correct):
    print("Correct")
else:
    if (maior):
        print("Incorrect! Your Number is Greater than the Secret Number")
    elif (menor):
        print("Incorrect! Your number is Less than the Secret Number")

print("End Game!!!")
