import random
import time

answers = ['yes','no','maybe','most likely','probably not','try again']

while True:
    q = input("What is your question?").lower().strip()
    time.sleep(1.0)
    if 'die' in q:
        print("I do not want anyone to die")
    elif 'name' in q:
        print("I do not have a name, I am a computer")
    else:
        r = random.choice(answers)
        print(r) 
#python3 maybe :p
