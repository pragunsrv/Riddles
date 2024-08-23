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
    "What has one eye but can’t see?": "needle"
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

def main_menu():
    print("Welcome to the Riddles Game!")
    while True:
        print("1. Play Game")
        print("2. View Scores")
        print("3. Reset Scores")
        print("4. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            reset_scores()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def reset_scores():
    global high_scores
    high_scores = []
    print("Scores have been reset.")

if __name__ == "__main__":
    main_menu()

# Extending the code with additional functions
def extra_functionality_21():
    squares = {x: x ** 2 for x in range(1, 51)}
    cubes = {x: x ** 3 for x in range(1, 51)}
    return squares, cubes

def extra_functionality_22():
    phrase = "to be or not to be"
    word_freq = {word: phrase.split().count(word) for word in phrase.split()}
    most_common = max(word_freq, key=word_freq.get)
    return word_freq, most_common

def extra_functionality_23():
    coordinates = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(100)]
    distances = [((x ** 2 + y ** 2) ** 0.5) for x, y in coordinates]
    max_distance = max(distances)
    min_distance = min(distances)
    return max_distance, min_distance

def extra_functionality_24():
    fib_sequence = [0, 1]
    for i in range(2, 101):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    sum_fibs = sum(fib_sequence)
    max_fib = max(fib_sequence)
    return sum_fibs, max_fib

def extra_functionality_25():
    letters = "abcdefghijklmnopqrstuvwxyz"
    random_string = ''.join(random.choice(letters) for _ in range(100))
    letter_freq = {letter: random_string.count(letter) for letter in letters}
    most_freq_letter = max(letter_freq, key=letter_freq.get)
    return random_string, letter_freq, most_freq_letter

def extra_functionality_26():
    matrix = [[random.randint(0, 100) for _ in range(5)] for _ in range(5)]
    transpose = [[matrix[j][i] for j in range(5)] for i in range(5)]
    diagonal_sum = sum(matrix[i][i] for i in range(5))
    return transpose, diagonal_sum

def extra_functionality_27():
    num_list = [random.randint(1, 200) for _ in range(200)]
    num_list.sort()
    median = num_list[len(num_list) // 2]
    average = sum(num_list) / len(num_list)
    return median, average

def extra_functionality_28():
    string = "versionfourtesting"
    reversed_string = string[::-1]
    uppercase_string = string.upper()
    return reversed_string, uppercase_string

def extra_functionality_29():
    prices = [random.uniform(1.0, 100.0) for _ in range(50)]
    total_cost = sum(prices)
    avg_price = total_cost / len(prices)
    return total_cost, avg_price

def extra_functionality_30():
    x_vals = list(range(1, 101))
    y_vals = [x ** 2 + 3 * x + 5 for x in x_vals]
    return x_vals, y_vals
