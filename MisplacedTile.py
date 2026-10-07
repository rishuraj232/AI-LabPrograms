from heapq import heappush, heappop

def misplaced_tiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def print_state(state):
    for row in state:
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()

def a_star(start, goal):
    pq = []
    h = misplaced_tiles(start, goal)

    heappush(pq, (h, 0, start, []))
    visited = set()

    while pq:
        f, g, current, path = heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path + [current]

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                h = misplaced_tiles(neighbor, goal)
                new_f = new_g + h

                heappush(pq, (new_f, new_g, neighbor, path + [current]))

    return None

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

start = get_puzzle("Initial State")
goal = get_puzzle("Goal State")

solution = a_star(start, goal)

if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)
    print("\nSteps:")

    for i, state in enumerate(solution):
        print("Step", i)
        print_state(state)
else:
    print("No solution found.")