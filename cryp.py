from itertools import permutations

def get_user_input():
    """Gets and validates user input for the cryptarithmetic puzzle"""
    print("Enter your cryptarithmetic puzzle (e.g., SEND + MORE = MONEY)")
    print("Format: WORD1 + WORD2 = RESULT (supports 2 words for now)")
    while True:
        try:
            equation = input("Enter the equation: ").upper().replace(" ", "")
            if "=" not in equation:
                raise ValueError("Equation must contain '='")
            parts = equation.split("=")
            if len(parts) != 2:
                raise ValueError("Invalid equation format")
            left_part = parts[0]
            result_word = parts[1]
            if "+" not in left_part:
                raise ValueError("Equation must contain '+'")
            words = left_part.split("+")
            if len(words) != 2:
                raise ValueError("Currently only supports adding two words")
            # Validate words contain only letters
            for word in words + [result_word]:
                if not word.isalpha():
                    raise ValueError("Words must contain only letters")
            # Automatically detect leading letters (first character of each word)
            leading_letters = [word[0] for word in words + [result_word]]
            return {
                'words': words,
                'result': result_word,
                'leading_letters': list(set(leading_letters))  # Remove duplicates
            }
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")

def solve_cryptarithmetic(problem):
    """Solves the cryptarithmetic puzzle using constraint satisfaction"""
    words = problem['words']
    result = problem['result']
    leading_letters = problem.get('leading_letters', [])
    # Collect all unique letters
    letters = sorted(set(''.join(words + [result])))
    # Generate all possible digit assignments
    for perm in permutations(range(10), len(letters)):
        # Create letter to digit mapping
        mapping = {letter: digit for letter, digit in zip(letters, perm)}
        # Skip if any leading letter is assigned 0
        if any(mapping[letter] == 0 for letter in leading_letters):
            continue
        # Convert words to numbers
        def word_to_number(word):
            return sum(mapping[ch] * (10 ** i) for i, ch in enumerate(reversed(word)))
        # Calculate sum of words and the result
        word_sum = sum(word_to_number(word) for word in words)
        result_num = word_to_number(result)
        # Check if the equation holds
        if word_sum == result_num:
            return mapping
    return None

def print_solution(problem, solution):
    """Prints the solution in a readable format"""
    if not solution:
        print("\nNo solution exists for this puzzle.")
        return
    print("\nSolution found:")
    # Print letter assignments alphabetically
    for letter, digit in sorted(solution.items()):
        print(f"{letter}: {digit}")
    # Print the equation with numbers
    print("\nVerification:")
    max_len = max(len(word) for word in problem['words'] + [problem['result']])
    for i, word in enumerate(problem['words']):
        num = ''.join(str(solution[ch]) for ch in word)
        operator = "+" if i == 0 else "  "
        print(f"{operator} {num.rjust(max_len)}")
    print(" " + "-" * (max_len + 1))
    result_num = ''.join(str(solution[ch]) for ch in problem['result'])
    print(f"  {result_num.rjust(max_len)}\n")

def main():
    print("Cryptarithmetic Puzzle Solver")
    print("-----------------------------")
    while True:
        problem = get_user_input()
        solution = solve_cryptarithmetic(problem)
        print_solution(problem, solution)
        if input("Solve another puzzle? (y/n): ").lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
