import random

lowest_num = 1
highest_num = 10 

random_number = random.randint(lowest_num, highest_num)
attempt = 0
max_attempt = 5
correct_guess = False 

print(f"guess the number between {lowest_num}, and the {highest_num}")
print(f"you have {max_attempt} attempts to guess the correct number")

while attempt < max_attempt and not correct_guess:
    guess = int(input("guess the correct number:"))
    if guess < 1 or guess > 10:
        print("out of range, your guess must be between 1 and 10")
        continue
    attempt += 1
#     if guess == random_number:
#         print(f"congratulations, you guessed the correct number: {random_number} in {attempt}")
#         correct_guess = True
#     elif guess < random_number:
#         print(f"too low, try again")
#     elif guess > random_number:
#         print(f"too high, try again")
# if not correct_guess:
#     print(f"sorry you have used all your {attempt}, the correct ncsumber was {random_number}")

match guess:
    case _ if guess < random_number:
        print("too low")
    case _ if guess > random_number:
        print("too high")
    case _:
        print("congratulation")
if not correct_guess:
   print(f"sorry you have used all your {attempt}, the correct number was {random_number}")