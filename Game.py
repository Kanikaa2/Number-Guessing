import random

player_name = input("Hello! What's your name? ")
ques_1 = input("Would you like to play a game? (Yes/No): ")

if ques_1 == "Yes":
    print("Let's begin.")
    print("Please note that you have only 3 tries to guess the number.")
    print("Okay, " + player_name + ", I am thinking of a number between 1 to 10. What do you think it is?")

    number_of_guesses = 0
    number_to_guess = random.randint(1, 10)

    while number_of_guesses < 3:
        try:
            guess = int(input("Enter your guess: "))
            number_of_guesses += 1

            if guess < number_to_guess:
                print("Your guess is too low. Try again.")
            elif guess > number_to_guess:
                print("Your guess is too high. Try again.")
            else:
                print("Congratulations, " + player_name + "! You guessed the number in " + str(number_of_guesses) + " tries!")
                break
        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Sorry, " + player_name + ", you did not guess the number. The number was " + str(number_to_guess) + ".")

elif ques_1 == "No":
    print("Too bad! Come back next time.")

else:
    print("Invalid response.")
