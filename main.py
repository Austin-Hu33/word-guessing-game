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

def ask_instructions():
    print("\nEnter your choice: [S] Start Game   [Q] Quit")
    choice = input("> ").strip().lower()
    return choice

def ask_start():
    print("\nReady to start?")
    print("  Type 'yes' to start playing")
    print("  Type 'no' to quit")
    choice = input("> ").strip().lower()
    return choice == 'yes'

def confirm_guess(guess):
    print(f"\nYou entered: {guess.upper()}")
    print("  Type 'yes' to confirm")
    print("  Type 'no' to re-enter your guess")
    choice = input("> ").strip().lower()
    return choice == 'yes'

def ask_restart():
    print("\nEnter your choice: [R] Play Again   [Q] Quit")
    choice = input("> ").strip().lower()
    return choice == 'r'

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
            from game import get_hint
            # warn user before spending an attempt on a hint
            print("\n⚠️  Warning: Using a hint costs one attempt!")
            confirm = input("Use hint? (yes/no): ").strip().lower()
            if confirm == 'yes':
                hint = get_hint(game['target'], game['history'])
                if hint:
                    print(f"\n💡 Hint: The word contains the letter '{hint.upper()}'")
                game['attempts_left'] -= 1
                if game['attempts_left'] == 0:
                    game['game_over'] = True
            continue

        if raw_input == 'history':
            show_guess_history(game['history'])
            continue

        valid, error_message = is_valid_input(raw_input, game['word_length'])
        if not valid:
            show_error(error_message)
            continue

        # ask user to confirm before submitting the guess
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

    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    main()