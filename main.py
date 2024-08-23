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
    "I’m not alive, but I can grow; I don’t have lungs, but I need air. What am I?": "fire"
}

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

def main_menu():
    print("Welcome to the Riddles Game!")
    while True:
        print("1. Play Game")
        print("2. View Scores")
        print("3. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def view_scores():
    print("This feature will be available in the next version.")

if __name__ == "__main__":
    main_menu()

# Extending the code with additional functions
def extra_functionality_11():
    number_list = [random.randint(1, 1000) for _ in range(500)]
    even_numbers = [num for num in number_list if num % 2 == 0]
    odd_numbers = [num for num in number_list if num % 2 != 0]
    even_sum = sum(even_numbers)
    odd_sum = sum(odd_numbers)
    return even_numbers, odd_numbers, even_sum, odd_sum

def extra_functionality_12():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    words_with_vowels = [word for word in words if set("aeiou").intersection(word)]
    words_with_consonants = [word for word in words if set("bcdfghjklmnpqrstvwxyz").intersection(word)]
    return words_with_vowels, words_with_consonants

def extra_functionality_13():
    numbers = list(range(1, 101))
    factorials = [1]
    for i in range(2, len(numbers) + 1):
        factorials.append(factorials[-1] * i)
    return factorials

def extra_functionality_14():
    matrix = [[random.randint(0, 50) for _ in range(10)] for _ in range(10)]
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    return row_sums, col_sums

def extra_functionality_15():
    sequence = [random.randint(1, 100) for _ in range(50)]
    unique_numbers = set(sequence)
    duplicated_numbers = [num for num in sequence if sequence.count(num) > 1]
    return unique_numbers, duplicated_numbers

def extra_functionality_16():
    sentence = "This is another sample sentence for more testing."
    word_freq = {word: sentence.split().count(word) for word in sentence.split()}
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

def extra_functionality_17():
    prime_factors = {}
    for num in range(2, 101):
        i = 2
        factors = []
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        prime_factors[num] = factors
    return prime_factors

def extra_functionality_18():
    data = [random.random() for _ in range(100)]
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val
    return max_val, min_val, range_val

def extra_functionality_19():
    string = "riddlesgameversionthree"
    reversed_string = string[::-1]
    unique_characters = set(string)
    return reversed_string, unique_characters

def extra_functionality_20():
    squares = [x ** 2 for x in range(1, 101)]
    cubes = [x ** 3 for x in range(1, 101)]
    square_sum = sum(squares)
    cube_sum = sum(cubes)
    return square_sum, cube_sum
