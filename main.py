import random

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
    "What comes once in a minute, twice in a moment, but never in a thousand years?": "m"
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
    print("3. Back to Main Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        change_difficulty()
    elif choice == "2":
        toggle_hints()
    elif choice == "3":
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

if __name__ == "__main__":
    main_menu()

# Extending the code with additional functions
def extra_functionality_31():
    prime_list = [2]
    for num in range(3, 101):
        is_prime = all(num % prime != 0 for prime in prime_list)
        if is_prime:
            prime_list.append(num)
    return prime_list

def extra_functionality_32():
    list_a = [random.randint(1, 100) for _ in range(50)]
    list_b = [random.randint(1, 100) for _ in range(50)]
    intersection = list(set(list_a) & set(list_b))
    union = list(set(list_a) | set(list_b))
    difference = list(set(list_a) - set(list_b))
    return intersection, union, difference

def extra_functionality_33():
    sentence = "Another test sentence for version five."
    word_lengths = {word: len(word) for word in sentence.split()}
    total_length = sum(word_lengths.values())
    avg_length = total_length / len(word_lengths)
    return word_lengths, total_length, avg_length

def extra_functionality_34():
    matrix_a = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    matrix_b = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    matrix_sum = [[matrix_a[i][j] + matrix_b[i][j] for j in range(3)] for i in range(3)]
    matrix_product = [[sum(a * b for a, b in zip(matrix_a_row, matrix_b_col)) for matrix_b_col in zip(*matrix_b)] for matrix_a_row in matrix_a]
    return matrix_sum, matrix_product

def extra_functionality_35():
    vowel_count = {vowel: random.randint(1, 20) for vowel in "aeiou"}
    consonant_count = {consonant: random.randint(1, 20) for consonant in "bcdfghjklmnpqrstvwxyz"}
    total_vowels = sum(vowel_count.values())
    total_consonants = sum(consonant_count.values())
    return vowel_count, consonant_count, total_vowels, total_consonants

def extra_functionality_36():
    angles = [random.randint(1, 180) for _ in range(50)]
    sin_values = [round(math.sin(math.radians(angle)), 2) for angle in angles]
    cos_values = [round(math.cos(math.radians(angle)), 2) for angle in angles]
    return angles, sin_values, cos_values

def extra_functionality_37():
    number = 987654321
    digit_sum = sum(int(digit) for digit in str(number))
    reversed_number = int(str(number)[::-1])
    return digit_sum, reversed_number

def extra_functionality_38():
    shopping_list = ["milk", "eggs", "bread", "butter"]
    prices = {item: random.uniform(1.0, 5.0) for item in shopping_list}
    total_cost = sum(prices.values())
    most_expensive = max(prices, key=prices.get)
    return prices, total_cost, most_expensive

def extra_functionality_39():
    temperatures = [random.uniform(-30.0, 50.0) for _ in range(365)]
    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    return avg_temp, max_temp, min_temp

def extra_functionality_40():
    binary_list = [bin(random.randint(0, 255))[2:].zfill(8) for _ in range(20)]
    ones_count = [binary.count('1') for binary in binary_list]
    zeros_count = [binary.count('0') for binary in binary_list]
    return binary_list, ones_count, zeros_count
