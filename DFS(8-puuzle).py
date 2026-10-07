def get_puzzle(name):
    print("\nEnter", name)
    print("Use 0 for blank space")

    puzzle = []

    for i in range(3):
        while True:
            row = list(map(int, input("Row " + str(i + 1) + ": ").split()))

            if len(row) == 3:
                puzzle.append(row)
                break

            print("Enter exactly 3 numbers.")

    return tuple(tuple(row) for row in puzzle)


def display(state):
    for row in state:
        for x in row:
            if x == 0:
                print("_", end=" ")
            else:
                print(x, end=" ")
        print()
    print()


def count_inversions(state):
    numbers = []

    for row in state:
        for x in row:
            if x != 0:
                numbers.append(x)

    inversions = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1

    return inversions


def is_solvable(initial, goal):
    initial_inv = count_inversions(initial)
    goal_inv = count_inversions(goal)

    print("\nInitial inversions:", initial_inv)
    print("Goal inversions:", goal_inv)

    return initial_inv % 2 == goal_inv % 2


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    row, col = find_blank(state)

    moves = [
        ("UP", -1, 0),
        ("DOWN", 1, 0),
        ("LEFT", 0, -1),
        ("RIGHT", 0, 1)
    ]

    neighbors = []

    for move, dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(r) for r in state]

            new_state[row][col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[row][col]

            new_state = tuple(tuple(r) for r in new_state)

            neighbors.append((new_state, move))

    return neighbors


def dfs(initial, goal):
    stack = [(initial, [initial], [])]
    visited = set()

    while stack:
        current, path, moves = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, moves

        for next_state, move in reversed(get_neighbors(current)):
            if next_state not in visited:
                stack.append(
                    (
                        next_state,
                        path + [next_state],
                        moves + [move]
                    )
                )

    return None, None


print("=" * 45)
print("       8-PUZZLE USING DFS")
print("=" * 45)

initial = get_puzzle("INITIAL STATE")
goal = get_puzzle("GOAL STATE")

print("\n" + "=" * 45)
print("INITIAL STATE")
print("=" * 45)
display(initial)

print("=" * 45)
print("GOAL STATE")
print("=" * 45)
display(goal)

print("=" * 45)
print("CHECKING SOLVABILITY")
print("=" * 45)

if not is_solvable(initial, goal):
    print("\nNO SOLUTION EXISTS!")
    print("The initial and goal states have different")
    print("inversion parity.")
    print("\nDFS search is not performed.")

else:
    print("\nPuzzle is solvable.")
    print("\nDFS SEARCH STARTED...")
    print("=" * 45)

    solution, moves = dfs(initial, goal)

    if solution:
        print("\nGOAL REACHED!")
        print("Total moves:", len(moves))

        print("\nSOLUTION PATH")
        print("=" * 45)

        print("Step 0")
        display(solution[0])

        for i in range(1, len(solution)):
            print("Move:", moves[i - 1])
            print("Step", i)
            display(solution[i])

    else:
        print("\nNo solution found.")