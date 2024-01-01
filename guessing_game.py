import random

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing

print(f"Please guess the number between 1 and {highest}: ")
guess = 0

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it.")
        break
    else:
        if guess < answer:
            print("Please guess higher.")
        else:
            print("Please guess lower.")

# if guess == answer:
#     print("You got it first time.")
# else:
#     if guess < answer:
#         print("Please guess higher.")
#     else:
#         print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it.")
#     else:
#         print("Sorry you have not guessed correctly.")

