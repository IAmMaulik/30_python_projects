import json
from difflib import get_close_matches

def find(w):
    if w in data:
        return data[word.lower()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yon = input(f"That word doesn't exist. Did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y is Yes or N if no:  ")
        if yon.lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yon.lower() == 'n':
            return "That word does not exist. Please try again..."
        else:
            return f"{yon} is not a valid input. Exiting Program..."
    else:
        return "That word does not exist. Please try again..."

data = json.load(open("data.json"))

word = input("Enter the word: ")
output = (find(word))
i = 1

if type(output) == list:
    for item in output:
        print(f"{i}. {item}")
        i += 1
