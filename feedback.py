def get_feedback(guess, target):
    feedback = []
    target_letters = list(target)

    # First pass: mark letters in the correct position
    for i in range(len(guess)):
        if guess[i] == target[i]:
            feedback.append((guess[i], 'correct'))
            target_letters[i] = None  # remove so it won't be matched again
        else:
            feedback.append((guess[i], None))  # placeholder for second pass

    # Second pass: check remaining letters for misplaced or incorrect
    for i in range(len(guess)):
        if feedback[i][1] is None:
            if guess[i] in target_letters:
                feedback[i] = (guess[i], 'misplaced')
                target_letters[target_letters.index(guess[i])] = None  # consume the match
            else:
                feedback[i] = (guess[i], 'incorrect')

    return feedback