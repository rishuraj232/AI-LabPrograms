# ============================================
# VACUUM CLEANER PROBLEM
# User Input Version
# ============================================

def display_state(state):
    vacuum, room_A, room_B = state

    print("\n-----------------------------")
    print("Current State")
    print("-----------------------------")
    print("Vacuum Position :", vacuum)
    print("Room A          :", "Dirty" if room_A == 1 else "Clean")
    print("Room B          :", "Dirty" if room_B == 1 else "Clean")
    print("-----------------------------")


# Check if goal is reached
def goal_test(state):
    vacuum, room_A, room_B = state

    return room_A == 0 and room_B == 0


# Vacuum Cleaner Agent
def vacuum_cleaner(state):

    state = list(state)

    print("\nInitial State:")
    display_state(state)

    step = 1

    while not goal_test(state):

        vacuum = state[0]

        # Vacuum is in Room A
        if vacuum == "A":

            # Room A is dirty
            if state[1] == 1:

                print("Step", step, ": SUCK")
                state[1] = 0

            # Room A is clean, move to B
            else:

                print("Step", step, ": MOVE RIGHT (A -> B)")
                state[0] = "B"

        # Vacuum is in Room B
        else:

            # Room B is dirty
            if state[2] == 1:

                print("Step", step, ": SUCK")
                state[2] = 0

            # Room B is clean, move to A
            else:

                print("Step", step, ": MOVE LEFT (B -> A)")
                state[0] = "A"

        display_state(state)

        step += 1

    print("\n================================")
    print("GOAL REACHED!")
    print("Both rooms are clean.")
    print("================================")


# ============================================
# USER INPUT
# ============================================

print("================================")
print("   VACUUM CLEANER PROBLEM")
print("================================")

# Get vacuum position
while True:
    vacuum = input("Enter vacuum position (A/B): ").upper()

    if vacuum == "A" or vacuum == "B":
        break

    print("Invalid input. Please enter A or B.")


# Get Room A status
while True:
    room_A = input("Is Room A dirty? (yes/no): ").lower()

    if room_A == "yes":
        room_A = 1
        break

    elif room_A == "no":
        room_A = 0
        break

    print("Invalid input. Please enter yes or no.")


# Get Room B status
while True:
    room_B = input("Is Room B dirty? (yes/no): ").lower()

    if room_B == "yes":
        room_B = 1
        break

    elif room_B == "no":
        room_B = 0
        break

    print("Invalid input. Please enter yes or no.")


# Create initial state
initial_state = (vacuum, room_A, room_B)

# Run the vacuum cleaner
vacuum_cleaner(initial_state)