import requests
from game import start_game, process_guess
from validator import is_valid_input
from display import (
    show_welcome,
    show_instructions,
    show_feedback,
    show_guess_prompt,
    show_guess_history,
    show_win,
    show_lose,
    show_error
)

WORD_INFO_URL = "http://localhost:5002/word-info"
SCORE_TRACKER_URL = "http://localhost:5003/get-scores"

def get_word_hint(target):
    # request word info from microservice
    try:
        response = requests.get(WORD_INFO_URL, params={'word': target})
        info = response.json()
        return info.get('pos'), info.get('definition')
    except Exception:
        return None, None

def get_game_history():
    # request game history from score tracker microservice
    try:
        response = requests.get(SCORE_TRACKER_URL)
        return response.json().get('scores', [])
    except Exception:
        return []

def show_history():
    scores = get_game_history()
    if not scores:
        print("\nNo game history found.")
        return
    print("\n=== Game History ===")
    for s in scores:
        print(f"  {s['outcome'].upper()} | attempts: {s['attempts']} | word: {s['target_word'].upper()}")

def ask_instructions():
    print("\nEnter your choice: [S] Start Game   [Q] Quit")
    choice = input("> ").strip().lower()
    return choice

def confirm_guess(guess):
    print(f"\nYou entered: {guess.upper()}")
    print("  Type 'yes' to confirm")
    print("  Type 'no' to re-enter your guess")
    choice = input("> ").strip().lower()
    return choice == 'yes'

def ask_restart():
    while True:
        print("\nEnter your choice: [R] Play Again   [H] View History   [Q] Quit")
        choice = input("> ").strip().lower()
        if choice == 'h':
            show_history()
        elif choice == 'r':
            return True
        elif choice == 'q':
            return False

def handle_hint(game):
    print("\n⚠️  Warning: Using a hint costs one attempt!")
    print("  [1] Part of speech")
    print("  [2] Definition")
    choice = input("> ").strip()
    pos, definition = get_word_hint(game['target'])
    if choice == '1' and pos:
        print(f"\n💡 Hint: The word is a {pos}.")
    elif choice == '2' and definition:
        print(f"\n💡 Hint: {definition}")
    else:
        print("\n💡 No hint available.")
    game['attempts_left'] -= 1
    if game['attempts_left'] == 0:
        game['game_over'] = True

def play_game():
    game = start_game()
    while not game['game_over']:
        show_guess_prompt(game['attempts_left'], game['max_attempts'])
        print("\nEnter your guess (or type 'hint' / 'history' / 'quit'):")
        raw_input = input("> ").strip().lower()
        if raw_input == 'quit':
            print("\nGoodbye!")
            exit()
        if raw_input == 'hint':
            handle_hint(game)
            continue
        if raw_input == 'history':
            show_guess_history(game['history'])
            continue
        valid, error_message = is_valid_input(raw_input, game['word_length'])
        if not valid:
            show_error(error_message)
            continue
        if not confirm_guess(raw_input):
            print("Re-enter your guess.")
            continue
        feedback = process_guess(game, raw_input)
        show_feedback(raw_input, feedback)
    attempts_used = game['max_attempts'] - game['attempts_left']
    if game['won']:
        show_win(game['target'], attempts_used)
    else:
        show_lose(game['target'])

def clear_scores():
    # clear all scores on quit
    try:
        requests.delete("http://localhost:5003/clear-scores")
    except Exception:
        pass

def main():
    show_welcome()
    choice = ask_instructions()
    if choice == 'q':
        print("\nGoodbye!")
        return
    elif choice == 's':
        play_game()
    while ask_restart():
        play_game()
    clear_scores()
    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    main()