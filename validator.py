def is_valid_input(guess, word_length=5):
    """
    Returns (is_valid, error_message)
    """
    if not guess.isalpha():
        return False, "Input must contain only letters."
    if len(guess) != word_length:
        return False, f"Input must be exactly {word_length} letters."
    return True, ""