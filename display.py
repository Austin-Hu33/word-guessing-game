WIDTH = 58

def draw_box(lines):
    border = "+" + "-" * WIDTH + "+"
    print(border)
    for line in lines:
        padding = WIDTH - len(line)
        print("|" + line + " " * padding + "|")
    print(border)

def show_welcome():
    draw_box([
        "",
        "           === WORD SAFARI ===          ",
        "",
        "  RULES:                                ",
        "  1. Guess the hidden 5-letter word     ",
        "     in 6 tries.                        ",
        "  2. Feedback symbols:                  ",
        "     [ + ] : Correct letter, correct spot.",
        "     [ - ] : Correct letter, wrong spot.",
        "     [ * ] : Not in the word.           ",
        "",
        "  ----------------------------------    ",
        "  [S] START GAME        [Q] QUIT        ",
        "",
    ])

def show_instructions():
    draw_box([
        "",
        "           === WORD SAFARI ===          ",
        "",
        "  HOW TO PLAY:                          ",
        "  Step 1: Enter a 5-letter word.        ",
        "  Step 2: View feedback for each letter.",
        "  Step 3: Use feedback to guess better. ",
        "  Step 4: Repeat until you win or lose. ",
        "",
        "  NOTE: Invalid input does NOT count    ",
        "        as an attempt.                  ",
        "        Type 'hint' for a hint.         ",
        "        Type 'history' to see guesses.  ",
        "",
    ])

def show_guess_prompt(attempts_left, max_attempts):
    step = max_attempts - attempts_left + 1
    draw_box([
        "",
        "           === WORD SAFARI ===          ",
        "",
        f"  STEP: [ {step} / {max_attempts} ]    ",
        "",
        "  Type your next 5-letter word:         ",
        "",
        "  > _ _ _ _ _                           ",
        "",
        "  (or type 'hint' / 'history')          ",
        "",
    ])

def show_feedback(guess, feedback):
    letters = "  ".join([l.upper() for l, _ in feedback])
    symbols = "  ".join([
        "+" if s == "correct" else
        "-" if s == "misplaced" else
        "*"
        for _, s in feedback
    ])
    draw_box([
        "",
        "           === WORD SAFARI ===          ",
        "",
        "  [ New Feedback ]                      ",
        "",
        f"  WORD : {letters}                     ",
        "",
        f"  CLUE : {symbols}                     ",
        "",
        "  Great job! Look at the symbols above. ",
        "",
        "  [ Press ENTER to continue ]           ",
        "",
    ])
    input()

def show_attempts_left(attempts_left):
    pass  # now handled in show_guess_prompt

def show_guess_history(history):
    if not history:
        return
    lines = [
        "",
        "           === WORD SAFARI ===          ",
        "",
        "  [ Last Guess ]                        ",
        "",
    ]
    for guess, feedback in history[-1:]:
        lines.append(f"  {guess.upper()}          ")
    lines.append("")
    draw_box(lines)

def show_win(word, attempts_used):
    draw_box([
        "",
        "           === WORD SAFARI ===          ",
        "",
        "  MISSION ACCOMPLISHED!                 ",
        "",
        "  [ YOU WON! ]                          ",
        "",
        f"  The magic word was:  {word.upper()}  ",
        "",
        f"  You found it in {attempts_used} steps!",
        "",
        "  Want to go on another safari?         ",
        "",
        "  > [R] Play Again     [Q] Quit         ",
        "",
    ])

def show_lose(word):
    draw_box([
        "",
        "           === WORD SAFARI ===          ",
        "",
        "  GAME OVER!                            ",
        "",
        f"  The word was:  {word.upper()}        ",
        "",
        "  Better luck next time!                ",
        "",
        "  > [R] Play Again     [Q] Quit         ",
        "",
    ])

def show_error(message):
    draw_box([
        "",
        "           === WORD SAFARI ===          ",
        "",
        "  OOPS! SOMETHING WENT WRONG...         ",
        "",
        "  [ Error ]                             ",
        "",
        f"  - {message}                          ",
        "",
        "  Don't worry, try again!               ",
        "",
        "  [ Press ENTER to go back ]            ",
        "",
    ])
    input()