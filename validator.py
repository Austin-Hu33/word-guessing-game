import requests

def is_valid_input(guess, word_length=5):
    if not guess.isalpha():
        return False, "Input must contain only letters."
    if len(guess) != word_length:
        return False, f"Input must be exactly {word_length} letters."
    
    # call word validator microservice
    try:
        response = requests.get("http://localhost:6240/validate", params={"word": guess})
        result = response.json()
        if not result.get("valid"):
            return False, "Not a valid English word."
    except Exception:
        pass  # skip if microservice is not running
    
    return True, ""