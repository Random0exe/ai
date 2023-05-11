import random

def play_monty_hall(switch):
    doors = [1, 2, 3]  # Represents the three doors
    prize_door = random.choice(doors)  # Randomly select the door with the prize
    chosen_door = random.choice(doors)  # Contestant randomly chooses a door

    # Host reveals a door with a goat that wasn't chosen by the contestant
    revealed_door = random.choice([door for door in doors if door != chosen_door and door != prize_door])

    if switch:
        # Contestant switches their choice to the other unopened door
        chosen_door = [door for door in doors if door != chosen_door and door != revealed_door][0]

    # Determine if the contestant wins or loses
    win = chosen_door == prize_door
    return win

# Simulation
num_simulations = 1000
print("Do you want to switch doors? (y/n)")
if input() == "y" or input() == "Y":
    switch_strategy = True
else:
    switch_strategy = False
print(f"Simulating {num_simulations} games of Monty Hall...")

wins = 0

for _ in range(num_simulations):
    if play_monty_hall(switch_strategy):
        wins += 1

win_percentage = (wins / num_simulations) * 100

print(f"Win percentage: {win_percentage}%")
