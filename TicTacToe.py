# ============================================
# TIC-TAC-TOE USING GAME TREE AND MINIMAX
# ============================================

# Board positions:
#
#  1 | 2 | 3
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  7 | 8 | 9
#
# AI  = X
# User = O


# -----------------------------
# Display the board
# -----------------------------
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


# -----------------------------
# Check winner
# -----------------------------
def check_winner(board):

    winning_combinations = [
        (0, 1, 2),  # Row 1
        (3, 4, 5),  # Row 2
        (6, 7, 8),  # Row 3
        (0, 3, 6),  # Column 1
        (1, 4, 7),  # Column 2
        (2, 5, 8),  # Column 3
        (0, 4, 8),  # Diagonal
        (2, 4, 6)   # Diagonal
    ]

    for a, b, c in winning_combinations:

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    # If board is full, it is a draw
    if " " not in board:
        return "Draw"

    # Game is still running
    return None


# -----------------------------
# Get available moves
# -----------------------------
def get_available_moves(board):
    return [i for i in range(9) if board[i] == " "]


# -----------------------------
# MINIMAX ALGORITHM
# -----------------------------
def minimax(board, is_maximizing):

    # Check whether the current state is terminal
    result = check_winner(board)

    # AI wins
    if result == "X":
        return 1

    # Human wins
    if result == "O":
        return -1

    # Draw
    if result == "Draw":
        return 0


    # --------------------------------
    # AI's turn - MAXIMIZE the score
    # --------------------------------
    if is_maximizing:

        best_score = -float("inf")

        for move in get_available_moves(board):

            # Make the move
            board[move] = "X"

            # Explore child node
            score = minimax(board, False)

            # Undo the move
            board[move] = " "

            # Choose maximum score
            best_score = max(best_score, score)

        return best_score


    # --------------------------------
    # Human's turn - MINIMIZE the score
    # --------------------------------
    else:

        best_score = float("inf")

        for move in get_available_moves(board):

            # Make the move
            board[move] = "O"

            # Explore child node
            score = minimax(board, True)

            # Undo the move
            board[move] = " "

            # Choose minimum score
            best_score = min(best_score, score)

        return best_score


# -----------------------------
# Find AI's best move
# -----------------------------
def get_best_move(board):

    best_score = -float("inf")
    best_move = None

    for move in get_available_moves(board):

        # Try the move
        board[move] = "X"

        # Calculate its score
        score = minimax(board, False)

        # Undo the move
        board[move] = " "

        # Keep the best move
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# -----------------------------
# MAIN GAME
# -----------------------------
def play_game():

    # Empty board
    board = [" "] * 9

    print("================================")
    print("       TIC-TAC-TOE AI")
    print("================================")
    print("You are O")
    print("AI is X")
    print()
    print("Choose a position from 1 to 9:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    # Game loop
    while True:

        # -------------------------
        # AI TURN
        # -------------------------
        print("AI is thinking...")

        ai_move = get_best_move(board)

        board[ai_move] = "X"

        print_board(board)

        # Check game status
        result = check_winner(board)

        if result is not None:

            if result == "X":
                print("AI wins!")

            elif result == "Draw":
                print("It's a draw!")

            break


        # -------------------------
        # HUMAN TURN
        # -------------------------
        while True:

            try:

                move = int(input("Enter your move (1-9): "))

                # Convert 1-9 to 0-8
                move = move - 1

                if move < 0 or move > 8:
                    print("Please enter a number between 1 and 9.")

                elif board[move] != " ":
                    print("That position is already occupied.")

                else:
                    board[move] = "O"
                    break

            except ValueError:
                print("Please enter a valid number.")


        print_board(board)

        # Check game status
        result = check_winner(board)

        if result is not None:

            if result == "O":
                print("You win!")

            elif result == "Draw":
                print("It's a draw!")

            break


# -----------------------------
# START THE GAME
# -----------------------------
play_game()