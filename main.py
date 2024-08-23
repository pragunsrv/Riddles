import random
import math

riddles = {
    "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": "echo",
    "I’m tall when I’m young, and I’m short when I’m old. What am I?": "candle",
    "What has keys but can't open locks?": "piano",
    "What can travel around the world while staying in a corner?": "stamp",
    "What has a heart that doesn’t beat?": "artichoke",
    "The more of this there is, the less you see. What is it?": "darkness",
    "What has many teeth, but can’t bite?": "comb",
    "What is always in front of you but can’t be seen?": "future",
    "What can fill a room but takes up no space?": "light",
    "What goes up but never comes down?": "age",
    "I shave every day, but my beard stays the same. What am I?": "barber",
    "You see me once in June, twice in November, but not at all in May. What am I?": "e",
    "I’m not alive, but I can grow; I don’t have lungs, but I need air. What am I?": "fire",
    "The more you take, the more you leave behind. What am I?": "footsteps",
    "What has one eye but can’t see?": "needle",
    "What has a head, a tail, is brown, and has no legs?": "penny",
    "What comes once in a minute, twice in a moment, but never in a thousand years?": "m",
    "What is full of holes but still holds water?": "sponge",
    "What has to be broken before you can use it?": "egg",
    "What has cities, but no houses; forests, but no trees; and rivers, but no water?": "map",
    "What is always in front of you but can’t be seen?": "future",
    "What gets wetter the more it dries?": "towel",
    "What is so fragile that saying its name breaks it?": "silence",
    "What has one eye but can’t see?": "needle",
    "The more you have of it, the less you see. What is it?": "darkness",
    "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?": "river",
    "What has a head, a tail, is brown, and has no legs?": "penny",
    "What comes once in a minute, twice in a moment, but never in a thousand years?": "m",
    "What can you catch but not throw?": "cold",
    "What has hands but can’t clap?": "clock"
}

high_scores = []

def play_game():
    score = 0
    for _ in range(5):
        riddle, answer = random.choice(list(riddles.items()))
        print("Riddle: " + riddle)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The answer was: " + answer)
        if hints_enabled:
            hint = get_hint(answer)
            print(hint)
    print("Your final score is:", score, "/ 5")
    if score == 5:
        print("Congratulations! You got a perfect score!")
    elif score >= 3:
        print("Good job! You got most of them right.")
    else:
        print("Better luck next time!")
    high_scores.append(score)

def view_scores():
    if high_scores:
        print("High Scores:")
        for i, score in enumerate(high_scores, start=1):
            print(f"{i}. {score}/5")
    else:
        print("No scores yet. Play the game to record your score!")

def reset_scores():
    global high_scores
    high_scores = []
    print("Scores have been reset.")

def main_menu():
    print("Welcome to the Riddles Game!")
    while True:
        print("1. Play Game")
        print("2. View Scores")
        print("3. Reset Scores")
        print("4. Settings")
        print("5. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            reset_scores()
        elif choice == "4":
            settings_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def settings_menu():
    print("Settings:")
    print("1. Change Difficulty")
    print("2. Toggle Hints")
    print("3. Customize Game")
    print("4. Back to Main Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        change_difficulty()
    elif choice == "2":
        toggle_hints()
    elif choice == "3":
        customize_game()
    elif choice == "4":
        return
    else:
        print("Invalid choice, please try again.")

def change_difficulty():
    print("Change Difficulty:")
    print("1. Easy (3 Rounds)")
    print("2. Medium (5 Rounds)")
    print("3. Hard (7 Rounds)")
    choice = input("Choose a difficulty: ").strip()
    if choice == "1":
        rounds = 3
    elif choice == "2":
        rounds = 5
    elif choice == "3":
        rounds = 7
    else:
        print("Invalid choice, setting to Medium (5 Rounds)")
        rounds = 5
    print(f"Difficulty set to {rounds} Rounds")

def toggle_hints():
    global hints_enabled
    hints_enabled = not hints_enabled
    status = "enabled" if hints_enabled else "disabled"
    print(f"Hints have been {status}")

hints_enabled = False

def get_hint(answer):
    if hints_enabled:
        return f"Hint: The answer starts with '{answer[0]}' and ends with '{answer[-1]}'"
    return "Hints are disabled."

def customize_game():
    print("Customize Game:")
    print("1. Add Riddles")
    print("2. Remove Riddles")
    print("3. Modify Riddles")
    print("4. Change Appearance")
    print("5. Back to Settings")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        add_riddles()
    elif choice == "2":
        remove_riddles()
    elif choice == "3":
        modify_riddles()
    elif choice == "4":
        change_appearance()
    elif choice == "5":
        return
    else:
        print("Invalid choice, please try again.")

def add_riddles():
    while True:
        riddle = input("Enter the new riddle (or type 'done' to finish): ").strip()
        if riddle.lower() == 'done':
            break
        answer = input("Enter the answer to the riddle: ").strip().lower()
        riddles[riddle] = answer
        print("Riddle added!")

def remove_riddles():
    while True:
        riddle = input("Enter the riddle to remove (or type 'done' to finish): ").strip()
        if riddle.lower() == 'done':
            break
        if riddle in riddles:
            del riddles[riddle]
            print("Riddle removed!")
        else:
            print("Riddle not found!")

def modify_riddles():
    while True:
        riddle = input("Enter the riddle to modify (or type 'done' to finish): ").strip()
        if riddle.lower() == 'done':
            break
        if riddle in riddles:
            new_riddle = input("Enter the new riddle text: ").strip()
            new_answer = input("Enter the new answer: ").strip().lower()
            del riddles[riddle]
            riddles[new_riddle] = new_answer
            print("Riddle modified!")
        else:
            print("Riddle not found!")

def change_appearance():
    print("Change Appearance:")
    print("1. Change Background Color")
    print("2. Change Text Color")
    print("3. Change Font Size")
    print("4. Back to Customize Game")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        print("Changing background color...")
    elif choice == "2":
        print("Changing text color...")
    elif choice == "3":
        print("Changing font size...")
    elif choice == "4":
        return
    else:
        print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

# Extending the code with additional functions
def extra_functionality_41():
    list_c = [random.randint(1, 200) for _ in range(100)]
    even_numbers = [num for num in list_c if num % 2 == 0]
    odd_numbers = [num for num in list_c if num % 2 != 0]
    print("Extra functionality: even and odd numbers separated.")

def extra_functionality_42():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print(f"Extra functionality: The product of {x} and {y} is {x * y}.")

def extra_functionality_43():
    text = "This is a sentence for analysis."
    word_count = len(text.split())
    letter_count = len([char for char in text if char.isalpha()])
    print(f"Extra functionality: {word_count} words and {letter_count} letters in the sentence.")

def extra_functionality_44():
    words = ["alpha", "beta", "gamma", "delta"]
    capitalized_words = [word.upper() for word in words]
    print("Extra functionality: Words capitalized -", capitalized_words)

def extra_functionality_45():
    sequence = [random.randint(1, 10) for _ in range(10)]
    doubled_sequence = [num * 2 for num in sequence]
    print("Extra functionality: Sequence doubled -", doubled_sequence)

def extra_functionality_46():
    square_roots = [math.sqrt(i) for i in range(1, 21)]
    print("Extra functionality: Square roots calculated -", square_roots)

def extra_functionality_47():
    even_numbers = [num for num in range(1, 100) if num % 2 == 0]
    print("Extra functionality: Even numbers from 1 to 100 -", even_numbers)

def extra_functionality_48():
    matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("Extra functionality: Matrix transposed -", transposed)

def extra_functionality_49():
    factors = {num: [i for i in range(1, num + 1) if num % i == 0] for num in range(1, 21)}
    print("Extra functionality: Factors calculated -", factors)

def extra_functionality_50():
    factorial_values = {num: math.factorial(num) for num in range(1, 11)}
    print("Extra functionality: Factorials calculated -", factorial_values)
