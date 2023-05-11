from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_quantity):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty
    visited.add((0, 0))

    while queue:
        current_state = queue.popleft()
        jug1_quantity, jug2_quantity = current_state

        # Check if the target quantity is reached
        if jug1_quantity == target_quantity or jug2_quantity == target_quantity:
            return current_state

        # Generate possible next states by pouring water
        next_states = [
            (jug1_capacity, jug2_quantity),  # Fill jug1 to its capacity
            (jug1_quantity, jug2_capacity),  # Fill jug2 to its capacity
            (0, jug2_quantity),  # Empty jug1
            (jug1_quantity, 0),  # Empty jug2
            (min(jug1_capacity, jug1_quantity + jug2_quantity), max(0, jug1_quantity + jug2_quantity - jug1_capacity)),  # Pour from jug2 to jug1
            (max(0, jug1_quantity + jug2_quantity - jug2_capacity), min(jug2_capacity, jug1_quantity + jug2_quantity)),  # Pour from jug1 to jug2
        ]

        # Visit unvisited next states and add them to the queue
        for next_state in next_states:
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)

    return None  # No solution found

# Ask the user for inputs
jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
target_quantity = int(input("Enter the target quantity: "))

solution = water_jug_problem(jug1_capacity, jug2_capacity, target_quantity)
if solution:
    print(f"Solution found: Jug 1: {solution[0]}, Jug 2: {solution[1]}")
else:
    print("No solution found.")
