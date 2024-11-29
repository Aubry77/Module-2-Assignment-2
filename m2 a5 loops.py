import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(len(days)):
    mood = random.choice(moods)
    print(f"On {days[i]}, you were feeling {mood}.")
