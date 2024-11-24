import random
print("Welcome to the color Guessing Game")
color = ["red", "Blue", "Black", "pink", "White", "Purple"]
random_color = random.choice(color)
score = 0
game_on = True
guess = 0
while game_on:
    user_guess = input("Pick any color any secondary color: ").lower()
    if random_color == user_guess:
        score += 1
        print(f"You are right. The right color is {random_color}")
        print(f"Your score is {score}")
    else:
        print(f"You are wrong. The right color is {random_color}")
        print(f"Your score is {score}")
    guess += 1
    if guess == 5:
        game_on = False
        print("Game over")


