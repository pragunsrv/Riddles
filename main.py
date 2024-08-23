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
    "What gets wetter the more it dries?": "towel",
    "What is so fragile that saying its name breaks it?": "silence",
    "What has many keys but can’t open a single door?": "piano",
    "What is always coming but never arrives?": "tomorrow",
    "What can be cracked, made, told, and played?": "joke",
    "What has one eye but can’t see?": "needle",
    "What has teeth but cannot bite?": "comb",
    "What has a neck but no head?": "bottle",
    "What is so delicate that even mentioning it breaks it?": "silence",
    "What has a head, a tail, is brown, and has no legs?": "penny",
    "What can you catch but not throw?": "cold",
    "What has hands but can’t clap?": "clock",
    "What has many keys but can’t open a single door?": "piano",
    "What can travel around the world while staying in a corner?": "stamp"
}

high_scores = []
game_history = []

def play_game():
    score = 0
    for _ in range(7):
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
    print("Your final score is:", score, "/ 7")
    if score == 7:
        print("Congratulations! You got a perfect score!")
    elif score >= 5:
        print("Good job! You got most of them right.")
    else:
        print("Better luck next time!")
    high_scores.append(score)
    game_history.append({'score': score, 'timestamp': datetime.now()})

def view_scores():
    if high_scores:
        print("High Scores:")
        for i, score in enumerate(high_scores, start=1):
            print(f"{i}. {score}/7")
    else:
        print("No scores yet. Play the game to record your score!")

def reset_scores():
    global high_scores
    high_scores = []
    print("Scores have been reset.")

def view_game_history():
    if game_history:
        print("Game History:")
        for record in game_history:
            print(f"Score: {record['score']}, Date: {record['timestamp']}")
    else:
        print("No game history available.")

def main_menu():
    print("Welcome to the Riddles Game!")
    while True:
        print("1. Play Game")
        print("2. View Scores")
        print("3. Reset Scores")
        print("4. View Game History")
        print("5. Settings")
        print("6. Extra Features")
        print("7. Stats")
        print("8. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            reset_scores()
        elif choice == "4":
            view_game_history()
        elif choice == "5":
            settings_menu()
        elif choice == "6":
            extra_features_menu()
        elif choice == "7":
            stats_menu()
        elif choice == "8":
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
def generate_sudoku_():
    print("Generating Sudoku puzzle...")
    # Placeholder for Sudoku puzzle generation logic

def generate_crossword_():
    print("Generating Crossword puzzle...")
    # Placeholder for Crossword puzzle generation logic

def generate_logic_grid_():
    print("Generating Logic Grid puzzle...")
    # Placeholder for Logic Grid puzzle generation logic

def stats_menu_():
    print("Game Statistics:")
    print("1. Riddle Statistics")
    print("2. Game Performance")
    print("3. Game History")
    print("4. Back to Main Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        riddle_statistics()
    elif choice == "2":
        game_performance()
    elif choice == "3":
        view_game_history()
    elif choice == "4":
        return
    else:
        print("Invalid choice, please try again.")

def riddle_statistics_():
    print("Riddle Statistics:")
    total_riddles = len(riddles)
    print(f"Total Riddles: {total_riddles}")
    if total_riddles > 0:
        correct_answers = sum(1 for riddle in riddles.values() if riddle in riddles.values())
        print(f"Total Correct Answers: {correct_answers}")

def game_performance_():
    print("Game Performance:")
    if high_scores:
        average_score = sum(high_scores) / len(high_scores)
        print(f"Average Score: {average_score:.2f}")
    else:
        print("No performance data available.")
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
        print("Background color changed!")
    elif choice == "2":
        print("Text color changed!")
    elif choice == "3":
        print("Font size changed!")
    elif choice == "4":
        return
    else:
        print("Invalid choice, please try again.")

def extra_features_menu():
    print("Extra Features:")
    print("1. Advanced Riddle Analysis")
    print("2. Math and Number Games")
    print("3. Logic Puzzle Generators")
    print("4. Back to Main Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        advanced_riddle_analysis()
    elif choice == "2":
        math_number_games()
    elif choice == "3":
        logic_puzzle_generators()
    elif choice == "4":
        return
    else:
        print("Invalid choice, please try again.")

def advanced_riddle_analysis():
    print("Advanced Riddle Analysis:")
    analysis = {riddle: len(answer) for riddle, answer in riddles.items()}
    print("Riddle Analysis (length of answers):", analysis)

def math_number_games():
    print("Math and Number Games:")
    print("1. Random Math Quiz")
    print("2. Number Guessing Game")
    print("3. Prime Number Checker")
    print("4. Back to Extra Features Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        random_math_quiz()
    elif choice == "2":
        number_guessing_game()
    elif choice == "3":
        prime_number_checker()
    elif choice == "4":
        return
    else:
        print("Invalid choice, please try again.")

def random_math_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*', '/'])
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        correct_answer = num1 / num2
    print(f"Solve: {num1} {operation} {num2}")
    user_answer = float(input("Your answer: ").strip())
    if math.isclose(user_answer, correct_answer, rel_tol=1e-9):
        print("Correct!")
    else:
        print("Wrong! The correct answer was:", correct_answer)

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess the number (1-100): ").strip())
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! The number was {number}. It took you {attempts} attempts.")
            break

def prime_number_checker():
    num = int(input("Enter a number to check if it's prime: ").strip())
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

def logic_puzzle_generators():
    print("Logic Puzzle Generators:")
    print("1. Generate Sudoku Puzzle")
    print("2. Generate Crossword Puzzle")
    print("3. Generate Logic Grid Puzzle")
    print("4. Back to Extra Features Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        generate_sudoku()
    elif choice == "2":
        generate_crossword()
    elif choice == "3":
        generate_logic_grid()
    elif choice == "4":
        return
    else:
        print("Invalid choice, please try again.")

def generate_sudoku():
    print("Generating Sudoku puzzle...")
    # Placeholder for Sudoku puzzle generation logic

def generate_crossword():
    print("Generating Crossword puzzle...")
    # Placeholder for Crossword puzzle generation logic

def generate_logic_grid():
    print("Generating Logic Grid puzzle...")
    # Placeholder for Logic Grid puzzle generation logic

def stats_menu():
    print("Game Statistics:")
    print("1. Riddle Statistics")
    print("2. Game Performance")
    print("3. Game History")
    print("4. Back to Main Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        riddle_statistics()
    elif choice == "2":
        game_performance()
    elif choice == "3":
        view_game_history()
    elif choice == "4":
        return
    else:
        print("Invalid choice, please try again.")

def riddle_statistics():
    print("Riddle Statistics:")
    total_riddles = len(riddles)
    print(f"Total Riddles: {total_riddles}")
    if total_riddles > 0:
        correct_answers = sum(1 for riddle in riddles.values() if riddle in riddles.values())
        print(f"Total Correct Answers: {correct_answers}")

def game_performance():
    print("Game Performance:")
    if high_scores:
        average_score = sum(high_scores) / len(high_scores)
        print(f"Average Score: {average_score:.2f}")
    else:
        print("No performance data available.")

if __name__ == "__main__":
    main_menu()
