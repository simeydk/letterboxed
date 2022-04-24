from letterboxed import Letterboxed

# lb = Letterboxed('HNA CRI ELT OBV')

puzzles = [
    'HNA CRI ELT OBV',
    'HEU KCT PVL ROM',
    'FKU EPR ACW DSO',
    'AOT KJW RSL CEU',
    'AEI OMR JND UXY',
]

lb = Letterboxed(puzzles[4])

# print(len(lb.valid_words))
# print(lb.is_valid_word('CHEAT'), lb.is_valid_word('HAND'), lb.is_valid_word('SAND'))

# for char in lb.chars:
#     print(char, len(lb.starts_with(char)))

print(f"Letters: {' '.join(lb.chars)}")

print('\n')
print(f"{len(lb.valid_words)} valid words. Best words:")
print('\n'.join(lb.valid_words[:10]))
print('\n')

num_solutions: int = 10

print(f'{num_solutions} best solutions:')
print('\n'.join(' -> '.join(sol) for sol in lb.get_solutions(num_solutions, max_len=5)))
