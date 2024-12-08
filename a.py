import streamlit as st
import numpy as np

# Initialize the board
def initialize_board():
    return np.full((3, 3), None)

# Check for a winner
def check_winner(board):
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        if all(cell == 'O' for cell in row):
            return 'O'

    for col in range(3):
        if all(row[col] == 'X' for row in board):
            return 'X'
        if all(row[col] == 'O' for row in board):
            return 'O'

    if all(board[i, i] == 'X' for i in range(3)) or all(board[i, 2 - i] == 'X' for i in range(3)):
        return 'X'
    if all(board[i, i] == 'O' for i in range(3)) or all(board[i, 2 - i] == 'O' for i in range(3)):
        return 'O'

    if not any(cell is None for row in board for cell in row):
        return "Draw"

    return None

# AI (Minimax Algorithm)
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] is None:
                    board[i, j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i, j] = None
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] is None:
                    board[i, j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i, j] = None
                    best_score = min(best_score, score)
        return best_score

# AI makes a move
def ai_move(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i, j] is None:
                board[i, j] = 'O'
                score = minimax(board, 0, False)
                board[i, j] = None
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move] = 'O'

# Main Streamlit app
def main():
    st.title("AI-based Tic Tac Toe")
    st.markdown("""
    Play Tic Tac Toe against an AI that uses the minimax algorithm.
    - You are **X**.
    - The AI is **O**.
    """)

    # Initialize session state
    if "board" not in st.session_state:
        st.session_state.board = initialize_board()
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    board = st.session_state.board
    game_over = st.session_state.game_over

    # Display the board
    st.markdown("### Board:")
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                if board[i, j] is None and not game_over:
                    if st.button(" ", key=f"{i}-{j}"):
                        board[i, j] = 'X'
                        winner = check_winner(board)
                        if winner is None:
                            ai_move(board)
                            winner = check_winner(board)

                        if winner:
                            st.session_state.game_over = True
                            if winner == "Draw":
                                st.success("It's a Draw!")
                            else:
                                st.success(f"{winner} wins!")
                else:
                    st.button(board[i, j] if board[i, j] else " ", disabled=True)

    # Reset button
    if st.button("Reset Game"):
        st.session_state.board = initialize_board()
        st.session_state.game_over = False

if __name__ == "__main__":
    main()
