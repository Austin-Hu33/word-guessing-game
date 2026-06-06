import random
import requests

# fallback word list if microservice is not running
FALLBACK_WORDS = [
    "apple", "brave", "crane", "dress", "eagle",
    "flame", "grape", "honey", "irony", "joker",
    "kneel", "lemon", "mango", "nerve", "ocean",
    "piano", "queen", "rider", "stone", "tiger",
    "umbra", "vivid", "water", "xenon", "yacht",
    "zebra", "blaze", "chest", "drift", "elbow",
    "frost", "gloom", "haste", "inlet", "juice"
]

MICROSERVICE_URL = "http://localhost:5001/random-word"


def get_random_word():
    # request a random word from the microservice
    try:
        response = requests.get(MICROSERVICE_URL)
        return response.json().get('word')
    except Exception:
        return random.choice(FALLBACK_WORDS)