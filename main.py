import random

riddles = {
    "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": "echo",
    "I’m tall when I’m young, and I’m short when I’m old. What am I?": "candle",
    "What has keys but can't open locks?": "piano",
    "What can travel around the world while staying in a corner?": "stamp",
    "What has a heart that doesn’t beat?": "artichoke"
}

def play_game():
    riddle, answer = random.choice(list(riddles.items()))
    print("Riddle: " + riddle)
    user_answer = input("Your answer: ").strip().lower()
    if user_answer == answer:
        print("Correct!")
    else:
        print("Wrong! The answer was: " + answer)

if __name__ == "__main__":
    play_game()
