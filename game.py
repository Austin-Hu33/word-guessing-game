from words import get_random_word
from feedback import get_feedback

def get_hint(target, history):
    # collect all letters already guessed correctly
    guessed_correct = set()
    for _, feedback in history:
        for letter, status in feedback:
            if status == 'correct':
                guessed_correct.add(letter)

    # return the first letter in target that hasn't been found yet
    for letter in target:
        if letter not in guessed_correct:
            return letter
    return None

def check_win(feedback):
    # win only if every letter is in the correct position
    return all(status == 'correct' for _, status in feedback)

def start_game(word_length=5, max_attempts=6):
    # initialize a new game state as a dictionary
    return {
        'target': get_random_word(),
        'word_length': word_length,
        'max_attempts': max_attempts,
        'attempts_left': max_attempts,
        'history': [],
        'game_over': False,
        'won': False
    }

def process_guess(game, guess):
    target = game['target']
    feedback = get_feedback(guess, target)
    game['history'].append((guess, feedback))
    game['attempts_left'] -= 1

    # check if the player won or ran out of attempts
    if check_win(feedback):
        game['game_over'] = True
        game['won'] = True
    elif game['attempts_left'] == 0:
        game['game_over'] = True

    return feedback