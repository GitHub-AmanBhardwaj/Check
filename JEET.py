# def display_students_by_semester(file_name):
#     with open(file_name, 'r') as file:
#         students = []
#         for line in file:
#             name, enrollment, semester, cgpa = line.strip().split(', ')
#             students.append((name, enrollment, int(semester), float(cgpa)))
#     semesters = {}
#     for student in students:
#         name, enrollment, semester, cgpa = student
#         if semester not in semesters:
#             semesters[semester] = []
#         semesters[semester].append(student)
#     for semester, student_list in sorted(semesters.items()):
#         print(f"\nSemester {semester}:")
#         sorted_students = sorted(student_list, key=lambda x: x[3], reverse=True)
#         for student in sorted_students:
#             name, enrollment, semester, cgpa = student
#             print(f"Name: {name}, Enrollment: {enrollment}, CGPA: {cgpa:.2f}")

# file_name = "A.txt"
# display_students_by_semester(file_name)





# # Initialize the board
# board = [' ' for i in range(9)]
# current_player = 'X'

# # Function to print the board
# def print_board():
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print("--+---+--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("--+---+--")
#     print(f"{board[6]} | {board[7]} | {board[8]}")

# # Function to check if a player has won
# def check_win(player):
#     win_combinations = [
#         [0, 1, 2],  # Top row
#         [3, 4, 5],  # Middle row
#         [6, 7, 8],  # Bottom row
#         [0, 3, 6],  # Left column
#         [1, 4, 7],  # Center column
#         [2, 5, 8],  # Right column
#         [0, 4, 8],  # Diagonal
#         [2, 4, 6]   # Diagonal
#     ]
#     for combo in win_combinations:
#         match = True
#         for i in combo:
#             if board[i] != player:
#                 match = False
#                 break
#         if match:
#             return True
#     return False

# # Function to check if the board is full
# def is_board_full():
#     return ' ' not in board

# # Function to handle a player’s move
# def player_move():
#     while True:
#         try:
#             move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
#             if move < 0 or move >= 9 or board[move] != ' ':
#                 print("Invalid move! Try again.")
#             else:
#                 board[move] = current_player
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 9.")

# # Main game loop
# while True:
#     print_board()
#     player_move()
#     if check_win(current_player):
#         print_board()
#         print(f"Player {current_player} wins!")
#         break
#     elif is_board_full():
#         print_board()
#         print("It's a draw!")
#         break

#     # Switch player
#     if current_player == 'X':
#         current_player = 'O'  
#     else:
#         current_player = 'X'


# class Student:
#     semester_1_students = {}
#     semester_2_students = {}
#     semester_3_students = {}

#     def __init__(self, name, student_id, semester, cgpa):
#         self.name = name
#         self.student_id = student_id
#         self.semester = semester
#         self.cgpa = cgpa
#         self.update_students()

#     def update_students(self):
#         if self.semester == 1:
#             Student.semester_1_students[self.cgpa] = {"Name": self.name, "ID": self.student_id, "CGPA": self.cgpa}
#         elif self.semester == 2:
#             Student.semester_2_students[self.cgpa] = {"Name": self.name, "ID": self.student_id, "CGPA": self.cgpa}
#         elif self.semester == 3:
#             Student.semester_3_students[self.cgpa] = {"Name": self.name, "ID": self.student_id, "CGPA": self.cgpa}
#         else:
#             print("Semester not supported.")

#     @staticmethod
#     def display_merit_list(semester):
#         if semester == 1:
#             students = sorted(Student.semester_1_students.items(), reverse=True)
#         elif semester == 2:
#             students = sorted(Student.semester_2_students.items(), reverse=True)
#         elif semester == 3:
#             students = sorted(Student.semester_3_students.items(), reverse=True)
#         else:
#             print("Semester not supported.")
#             return

#         if not students:
#             print(f"No students found for Semester {semester}.")
#             return

#         print(f"\nMerit List for Semester {semester}:")
#         for position, (cgpa, details) in enumerate(students, start=1):
#             print(f"Position {position}: Name: {details['Name']}, ID: {details['ID']}, CGPA: {cgpa}")

#     def display_student(self):
#         print(f"Name: {self.name}")
#         print(f"ID: {self.student_id}")
#         print(f"Semester: {self.semester}")
#         print(f"CGPA: {self.cgpa}")
# students = [
#     Student("Aman", "S123", 1, 9.0),
#     Student("Jeet", "S124", 1, 9.5),
#     Student("Tulsidas Khan", "S125", 1, 8.8),
#     Student("Inspector Roy", "S126", 1, 9.2),
#     Student("David Kumar", "S127", 2, 8.7),
#     Student("Bhanu Pratap", "S128", 2, 9.1),
#     Student("Bulla", "S129", 2, 8.9),
#     Student("Hatele", "S130", 3, 9.8),
#     Student("Paplu", "S131", 3, 9.0),
#     Student("Oggy", "S132", 3, 9.3)
# ]

# Student.display_merit_list(1)
# Student.display_merit_list(2)
# Student.display_merit_list(3)



import streamlit as st

# Fibonacci function
def fibonacci(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Coin Change Problem
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Longest Common Subsequence (LCS)
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
  
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n] 

# Main Streamlit App
def main():
    st.title("Dynamic Programming Problem Solver")

    # Interactive Problem Selection
    problem_choice = st.selectbox(
        "Choose a problem to solve:",
        ("Fibonacci", "Coin Change", "Longest Common Subsequence")
    )

    # Fibonacci Problem
    if problem_choice == "Fibonacci":
        st.markdown("""
        ### Fibonacci Number
        This app calculates the **n-th Fibonacci number** using dynamic programming.
        The function computes Fibonacci numbers efficiently using **O(n)** time complexity.
        """)
        n = st.number_input("Enter the value of n for Fibonacci:", min_value=0, value=10)
        if n >= 0:
            result = fibonacci(n)
            st.subheader(f"The {n}-th Fibonacci number is:")
            st.write(result)

    # Coin Change Problem
    elif problem_choice == "Coin Change":
        st.markdown("""
        ### Coin Change Problem
        Given a list of coin denominations and a total amount, 
        this problem finds the minimum number of coins needed to make the given amount. 
        The result is computed using dynamic programming.
        """)
        coins_input = st.text_input("Enter the coin denominations (comma separated):", "1, 2, 5")
        amount = st.number_input("Enter the amount to make change for:", min_value=0, value=11)

        if coins_input:
            coins = list(map(int, coins_input.split(",")))
            result = coin_change(coins, amount)
            st.subheader(f"Minimum coins needed for amount {amount}:")
            if result != -1:
                st.write(result)
            else:
                st.write("It's not possible to make the exact change with the given coins.")

    # Longest Common Subsequence (LCS) Problem
    elif problem_choice == "Longest Common Subsequence":
        st.markdown("""
        ### Longest Common Subsequence (LCS)
        Given two strings, this problem finds the length of the longest subsequence that 
        is common to both strings using dynamic programming.
        """)
        str1 = st.text_input("Enter the first string:", "AGGTAB")
        str2 = st.text_input("Enter the second string:", "GXTXAYB")

        if str1 and str2:
            result = longest_common_subsequence(str1, str2)
            st.subheader(f"Length of LCS between '{str1}' and '{str2}':")
            st.write(result)

if __name__ == "__main__":
    main()

