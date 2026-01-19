from random import choice
words = ["python", "developer", "code", "challenge", "function", "variable"]
word = choice(words)
temp_word = ['_' for _ in word]
print(f"\033[5m {'*' * 20}  Welcome to the Guess the Word game!  {'*' * 20}\033[0m")
print(" ".join(temp_word))
attempts = 5
correct_inputs = set()

while attempts > 0 and '_' in temp_word:
    guess = input("Enter a letter: ").lower()
    if not guess or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue
    if guess in correct_inputs:
        print("You've already guessed that letter.")
        continue
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                temp_word[i] = guess
                correct_inputs.add(guess)
        print("Good guess!", ' '.join(temp_word))
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

if temp_word.count('_') == 0:
    print(f"\033[5mCongratulations! You've guessed the word: {word}\033[0m")
if attempts == 0:
    print("No attempts left!, Try your luck next time.")