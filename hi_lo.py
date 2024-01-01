low = 1
high = 1000

print(f"Pleas think of a number between {low} and {high}")
input("Press ENTER to start")

guesses = 1
while low != high:
    # print(f"\tGuessing in the range of {low} to {high}.")
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess is correct. "
                     .format(guess).casefold())

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses.")
        break
    else:
        print("Please enter h, l or c!")

    guesses = guesses + 1

else:
    print(f"You thought of the number {low}")
    print(f"I got in {guesses} guesses.")