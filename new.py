import random

print("                                                                         =====================")
print("                                                                         |     Guess My      |")
print("                                                                         |      Number       |")
print("                                                                         =====================")
print("")
name = input ("What is your name?")
print(f"Hi {name}, I am thinking of a integer between 0 and 100. Can you guess it?")
the_number = random.randint(0,100)

guess = -1

while guess != the_number:
    guess_text= input("what is your guess? ")
    guess = int(guess_text)

    if guess < the_number:
        print(f"sorry, {name}, but your guess is too LOW. Try again.")
    elif guess > the_number:
        print(f"sorry, {name}, but your answer is too HIGH. Try again.")
    else:
        print(f"YES!!!,your got it {name}")
print("Thanks For Playing!!!")