import random

WORD_LIST = [
    "apple", "brave", "crane", "dress", "eagle",
    "flame", "grape", "honey", "irony", "joker",
    "kneel", "lemon", "mango", "nerve", "ocean",
    "piano", "queen", "rider", "stone", "tiger",
    "umbra", "vivid", "water", "xenon", "yacht",
    "zebra", "blaze", "chest", "drift", "elbow",
    "frost", "gloom", "haste", "inlet", "juice"
]

def get_random_word():
    return random.choice(WORD_LIST)