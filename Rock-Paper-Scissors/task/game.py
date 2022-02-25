
options = ["scissors", "rock", "paper"]
beat_dict = {"scissors": "rock", "paper": "scissors", "rock": "paper"}

user_choice = input()
comp_choice = __import__("random").choice(options)
res = ""
message = (f"There is a draw ({comp_choice})",
           f"Sorry, but the computer chose {comp_choice}",
           f"Well done. The computer chose {comp_choice} and failed")
if user_choice == comp_choice:
    res = 0
elif beat_dict[user_choice] == comp_choice:
    res = 1
else:
    res = 2
print(message[res])
