SIZE = 10

def display(grid):
    for row in grid:
        print(' '.join(row))

def can_place(grid, word, x, y, dir, overlap_index):
    length = len(word)

    if dir == 0:  # horizontal
        start_y = y - overlap_index
        if start_y < 0 or start_y + length > SIZE:
            return False
        for i in range(length):
            cell = grid[x][start_y + i]
            if cell != '-' and cell != word[i]:
                return False
    else:  # vertical
        start_x = x - overlap_index
        if start_x < 0 or start_x + length > SIZE:
            return False
        for i in range(length):
            cell = grid[start_x + i][y]
            if cell != '-' and cell != word[i]:
                return False

    return True

def place_word(grid, word, x, y, dir, overlap_index):
    length = len(word)
    if dir == 0:
        start_y = y - overlap_index
        for i in range(length):
            grid[x][start_y + i] = word[i]
    else:
        start_x = x - overlap_index
        for i in range(length):
            grid[start_x + i][y] = word[i]

def find_place_with_overlap(grid, word):
    for i, ch in enumerate(word):
        for x in range(SIZE):
            for y in range(SIZE):
                if grid[x][y] == ch:
                    for dir in [0, 1]:  # 0 = horizontal, 1 = vertical
                        if can_place(grid, word, x, y, dir, i):
                            place_word(grid, word, x, y, dir, i)
                            return True
    return False

def fallback_place(grid, word):
    for x in range(SIZE):
        for y in range(SIZE):
            for dir in [0, 1]:
                if can_place(grid, word, x, y, dir, 0):
                    place_word(grid, word, x, y, dir, 0)
                    return True
    return False

def main():
    grid = [['-' for _ in range(SIZE)] for _ in range(SIZE)]
    words = input("Enter words separated by space: ").upper().split()

    for idx, word in enumerate(words):
        placed = False
        if idx == 0:
            placed = fallback_place(grid, word)
        else:
            placed = find_place_with_overlap(grid, word)
            if not placed:
                placed = fallback_place(grid, word)

        print(f"{'Placed' if placed else 'Could not place'}: {word}")

    print("\nFinal Crossword Grid:")
    display(grid)

if __name__ == "__main__":
    main()
