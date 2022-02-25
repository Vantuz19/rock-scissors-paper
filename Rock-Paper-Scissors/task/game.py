name = input("Enter your name: ")
score = 0
print(f"Hello, {name}")
options = ["scissors", "rock", "paper", ]
play_options = input()
if play_options != "":
    options = play_options.split(",")
beat_dict = {"rock": ["lightning", "gun", "air", "water", "dragon", "paper", "devil"],
             "gun": ["lightning", "sponge", "air", "water", "dragon", "paper", "devil"],
             "lightning": ["wolf", "sponge", "air", "water", "dragon", "paper", "devil"],
             "devil": ["wolf", "sponge", "air", "water", "dragon", "paper", "tree"],
             "dragon": ["wolf", "sponge", "air", "water", "human", "paper", "tree"],
             "water": ["wolf", "sponge", "air", "snake", "human", "paper", "tree"],
             "air": ["wolf", "sponge", "scissors", "snake", "human", "paper", "tree"],
             "paper": ["wolf", "sponge", "scissors", "snake", "human", "fire", "tree"],
             "sponge": ["wolf", "rock", "scissors", "snake", "human", "fire", "tree"],
             "wolf": ["gun", "rock", "scissors", "snake", "human", "fire", "tree"],
             "tree": ["gun", "rock", "scissors", "snake", "human", "fire", "lightning"],
             "human": ["gun", "rock", "scissors", "snake", "devil", "fire", "lightning"],
             "snake": ["gun", "rock", "scissors", "dragon", "devil", "fire", "lightning"],
             "scissors": ["gun", "rock", "water", "dragon", "devil", "fire", "lightning"],
             "fire": ["lightning", "gun", "air", "water", "dragon", "rock", "devil"]}
with open("rating.txt", "+r") as file:
    for i in file.readlines():
        if i.split()[0] == name:
            score = int(i.split()[1])
print("Okay, let's start")
while True:
    user_choice = input()
    if user_choice == "!exit":
        break
    if user_choice == "!rating":
        print(f"Your rating: {score}")
        continue
    if user_choice not in options:
        print("Invalid input")
        continue
    comp_choice = __import__("random").choice(options)
    res = ""
    message = (f"There is a draw ({comp_choice})",
               f"Sorry, but the computer chose {comp_choice}",
               f"Well done. The computer chose {comp_choice} and failed")
    if user_choice == comp_choice:
        res = 0
        score += 50
    elif comp_choice in beat_dict[user_choice]:
        res = 1
    else:
        res = 2
        score += 100
    print(message[res])

print("Bye!")
