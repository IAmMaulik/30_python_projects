import json

def find(w):
    try:
        return data[word.lower()]
    except:
        return("That word does not exist. Please try again")

data = json.load(open("data.json"))

word = input("Enter the word: ")
print(find(word))
