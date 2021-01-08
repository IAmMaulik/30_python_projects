import random

def memeify(text):
    arr = []
    b = '..ok boomer'
    if len(b) < len(text):
        for i in range(len(text)-len(b)):
            c = text[i]
            r = random.randint(0, 1)
            if r==1:
                arr.append(c.upper())
            else:
                arr.append(c.lower())
        return ''.join(arr + [b])

    else:
        for c in text:
            r = random.randint(0, 1)
            if r:
                arr.append(c.upper())
            else:
                arr.append(c.lower())
        return ''.join(arr)

a = input("Enter the text you want to memeify: ")
print(memeify(a))
