import random
word_list = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward',
    'banjo', 'cycle', 'duplex', 'equip', 'galaxy', 'gizmo', 'injury',
    'jovial', 'kayak', 'luxury', 'oxygen', 'puppy', 'quiz', 'rhythm',
    'scratch', 'snazzy', 'syndrome', 'unzip', 'vortex', 'waltz',
    'wizard', 'xylophone', 'yummy', 'zephyr', 'zombie'
]
lives = 6
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
guessed_letters = []
print("🎮 Welcome to the Word Guessing Game!")
print("🔡 Guess the word, one letter at a time.")
print(f"💡 The word has {len(chosen_word)} letters.\n")
print(" ".join(display))
while lives > 0 and "_" in display:
    guess = input("\nEnter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single alphabet letter.")
        continue
    if guess in guessed_letters:
        print(f"⚠️ You've already guessed '{guess}'. Try a new letter.")
        continue
    guessed_letters.append(guess)
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Correct guess!")
    else:
        lives -= 1
        print(f"❌ '{guess}' is not in the word. Lives remaining: {lives}")
    print("Word: " + " ".join(display))
if "_" not in display:
    print("\n🎉 You guessed the word correctly! You win!")
else:
    print(f"\n💀 You lost! The correct word was: '{chosen_word}'")
