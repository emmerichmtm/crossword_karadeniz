import numpy as np
import random
def place_word(grid, word, orientation, row, col, first_letter_color, color_grid):
    word_length = len(word)
    placed = False
    flipped = False
    if random.random() < 0.5:
        word = word[::-1]
        flipped = True

    if orientation == 'horizontal':
        placed = True
        for i in range(word_length):
            if grid[row, col + i] != ' ' and grid[row, col + i] != word[i]:
                placed = False
        if placed:
            grid[row, col:col + word_length] = list(word)
            print('Placed ' + word + ' at col' + str(col + word_length))
            if flipped:
                color_grid[row, col + word_length - 1] = first_letter_color
            else:
                color_grid[row, col] = first_letter_color
        return placed
    else:  # vertical
        placed = True
        for i in range(word_length):
            if grid[row + i, col] != ' ' and grid[row + i, col] != word[i]:
                placed = False
        if placed:
            grid[row:row + word_length, col] = list(word)
            print('Placed ' + word + ' at row ' + str(row + word_length))
            if flipped:
                color_grid[row + word_length - 1, col] = first_letter_color
            else:
                color_grid[row, col] = first_letter_color
        return placed
def create_crossword(word_list, color_codes_sonnenstrand, size=(15, 15)):
    grid = np.full(size, ' ', dtype=str)
    # create a grid of colors with random colors from color_codes dictionary values
    color_grid = np.array([[random.choice(color_coded_sonnenstrand) for _ in range(size[1])] for _ in range(size[0])])


    for index, word in enumerate(word_list):
        # find corresponding color
        color_first_letter = color_codes_sonnenstrand[index]
        # Find a place for the wor
        # Iterate ALL possible orientations and positions
        # Not random
        placed = False
        orientation_list = ['horizontal', 'vertical']

        # shuffle the orientation list
        random.shuffle(orientation_list)
        for orientation in orientation_list:
            # create a list of all row indexes
            row_list = range(size[0]-len(word))
            # make it a list
            row_list = list(row_list)
            # shuffle the row list
            random.shuffle(row_list)
            for row in row_list:
                # create a list of all column indexes
                col_list = range(size[1]-len(word))
                # make it a list
                col_list = list(col_list)
                # shuffle the column list
                random.shuffle(col_list)
                for col in col_list:
                    placed = place_word(grid, word, orientation, row, col, color_first_letter, color_grid)
                    if placed:
                        break
                if placed:
                    break
            if placed:
                break
    # fill the empty cells with random letters
    for i in range(size[0]):
        for j in range(size[1]):
            if grid[i, j] == ' ':
                grid[i, j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return grid, color_grid

# List of cities
words = ['Odessa', 'Goldstrand', 'Alapli', 'Yalta', 'Sochi','Batumi',
         'Constanca','Zonguldak', 'Trabzon', 'Sulina', 'Burgas', 'Varna']

# Make the words uppercase
words = [word.upper() for word in words]

print('words', words)
#Make as many words as letters in the word SONNENSTRAND
# count letters in the word SONNENSTRAND
l = len('SONNENSTRAND')
# truncate the list of words to the length of the word SONNENSTRAND
words = words[:l]


# Define ANSI color codes specifically for each letter in "SONNENSTRAND"
color_codes = {
    'S': '37',    # White (represents a light or unique color different from others)
    'O': '33',    # Yellow
    'N': '36',    # Cyan
    'E': '35',    # Magenta
    'T': '90',    # Bright black (dark gray)
    'R': '31;1',  # Bright red (distinct variation from normal red)
    'A': '39',  # Bright magenta (different from normal magenta)
    'D': '92'     # Blue (ensure 'D' is included)
}

# Randomize the order of keys
keys = list(color_codes.keys())
random.shuffle(keys)

# Print each key in its associated color
for key in keys:
    color = color_codes[key]
    print(f"\033[1;{color}m{key}\033[0m", end=' ')
print()  # Newline after the loop to ensure clean output


# Print the letters of SONNENSTRAND in the colors from the color list
for letter in 'SONNENSTRAND':
    color_code = color_codes[letter]
# Make a list of colors "color_coded_sonnenstrand" for each letter in "SONNENSTRAND" in this order using color_codes
color_coded_sonnenstrand = []

# For letters of string 'SONNENSTRAND'
for letter in 'SONNENSTRAND':
    if letter in color_codes:
        color_coded_sonnenstrand.append(color_codes[letter])


crossword, color_grid = create_crossword(words,color_coded_sonnenstrand)

# Print the crossword in random colors of the colors dictionary
for i in range(crossword.shape[0]):
    for j in range(crossword.shape[1]):
        color_code = random.choice(list(color_codes.values()))
        print(f"\033[1;{color_grid[i,j]}m{crossword[i, j]}\033[0m", end=' ')
    print()


