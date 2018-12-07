
from collections import defaultdict
from puzzle_1 import react


with open('day-5-input') as f:
    original_data = f.readline().rstrip()

char_counts = defaultdict(lambda: 0)
for char in original_data.lower():
    char_counts[char] += 1

for letter in char_counts:
    data = original_data.replace(letter[0], '').replace(letter[0].upper(), '')
    data = react(data)
    print(letter, ': -->', len(data))
