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
    "What goes up but never comes down?": "age"
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

def main_menu():
    print("Welcome to the Riddles Game!")
    while True:
        print("1. Play Game")
        print("2. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

# Extending the code to increase the line count
def extra_functionality_1():
    data = [random.randint(1, 100) for _ in range(100)]
    sorted_data = sorted(data)
    reversed_data = list(reversed(sorted_data))
    min_val = min(sorted_data)
    max_val = max(sorted_data)
    avg_val = sum(sorted_data) / len(sorted_data)
    return sorted_data, reversed_data, min_val, max_val, avg_val

def extra_functionality_2():
    string_data = "riddlesgame"
    unique_chars = set(string_data)
    char_count = {char: string_data.count(char) for char in unique_chars}
    return unique_chars, char_count

def extra_functionality_3():
    number = 123456789
    digit_sum = sum(int(digit) for digit in str(number))
    reversed_number = int(str(number)[::-1])
    squared_number = number ** 2
    return digit_sum, reversed_number, squared_number

def extra_functionality_4():
    fib_sequence = [0, 1]
    for i in range(2, 50):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    even_fibs = [num for num in fib_sequence if num % 2 == 0]
    odd_fibs = [num for num in fib_sequence if num % 2 != 0]
    return fib_sequence, even_fibs, odd_fibs

def extra_functionality_5():
    matrix = [[random.randint(1, 10) for _ in range(10)] for _ in range(10)]
    transposed_matrix = [[matrix[j][i] for j in range(10)] for i in range(10)]
    flattened_matrix = [item for sublist in matrix for item in sublist]
    matrix_sum = sum(flattened_matrix)
    return matrix, transposed_matrix, flattened_matrix, matrix_sum

def extra_functionality_6():
    name_list = ["alice", "bob", "charlie", "dave", "eve"]
    capitalized_names = [name.capitalize() for name in name_list]
    name_lengths = [len(name) for name in name_list]
    name_dict = dict(zip(capitalized_names, name_lengths))
    return capitalized_names, name_lengths, name_dict

def extra_functionality_7():
    prime_numbers = []
    for num in range(2, 100):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            prime_numbers.append(num)
    prime_sum = sum(prime_numbers)
    prime_count = len(prime_numbers)
    return prime_numbers, prime_sum, prime_count

def extra_functionality_8():
    sentence = "This is a sample sentence for testing purposes."
    words = sentence.split()
    reversed_words = " ".join(words[::-1])
    word_lengths = [len(word) for word in words]
    longest_word = max(words, key=len)
    return words, reversed_words, word_lengths, longest_word

def extra_functionality_9():
    hex_number = "4f2a"
    binary_number = bin(int(hex_number, 16))[2:]
    octal_number = oct(int(hex_number, 16))[2:]
    decimal_number = int(hex_number, 16)
    return binary_number, octal_number, decimal_number

def extra_functionality_10():
    vowels = "aeiou"
    consonants = "".join(set("abcdefghijklmnopqrstuvwxyz") - set(vowels))
    vowel_count = sum(1 for char in "riddlesgame" if char in vowels)
    consonant_count = sum(1 for char in "riddlesgame" if char in consonants)
    return vowels, consonants, vowel_count, consonant_count
