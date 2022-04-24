from typing import List, Set
from functools import lru_cache
import string




def get_mapper(puzzle_str: str) -> dict:
    '''
    maps a word to a list of numbers, where the number is the side of the puzzle that the letter occurs
    '''
    mapper = {char: 0 for char in string.ascii_uppercase}
    for i, side in enumerate(puzzle_str.split(' ')):
        for c in side:
            mapper[c] = i+1
    return mapper

def is_valid_word(mapper, word) -> bool:
    mapped = [mapper[c] for c in word]
    if 0 in mapped: return False
    for i in range(len(mapped) - 1):
        if mapped[i] == mapped[i+1]:
            return False
    return True

def get_valid_words(all_words, puzzle_str, min_len = 3):
    mapper = get_mapper(puzzle_str)
    valid_words = [word for word in all_words if ( is_valid_word(mapper, word)) ]
#     and is_valid_word(mapper, word)
    valid_words.sort(reverse=True, key = lambda s: len(set(s)))
    return valid_words


def test_word(puzzle, word):
    return is_valid_word(get_mapper(puzzle), word)


# In[36]:


puzzle = 'HNA CRI ELT OBV'
puzzles = [
    'HEU KCT PVL ROM',
    'FKU EPR ACW DSO',
    'AOT KJW RSL CEU',
]


# In[10]:


test_word(puzzle, 'HOVER')


# In[41]:


def get_solutions(puzzle_str, all_words = set(SOWPODS), max_len = 5, max_solutions = 1000):
    valid_words = get_valid_words(all_words, puzzle_str)
    chars = {c for c in puzzle_str if c != ' '}
#     print({'valid_words': valid_words, 'chars': chars})
    num_solutions = 0
    for solution in step(chars, valid_words, max_len = 5):
        num_sulutions =+ 1 
        yield solution
        if num_solutions == max_solutions: return
        
    
def filter_startswith(word_set: Set[str], start: str):
    return {word for word in word_set if word.startswith(start)}
    
def step(chars_left: Set[str], all_words: Set[str], existing_words: List[str] = [], max_len = 5):
#     print("step", chars_left, all_words, existing_words, max_len)
    valid_words = all_words
    if existing_words:
        last_char = existing_words[-1][-1]
        valid_words = filter_startswith(all_words, last_char)
        valid_words = valid_words.difference(set(existing_words))
    words = list(valid_words)
    words.sort(reverse=True, key = lambda w: len(chars_left.intersection(set(w))))
    for word in words:
        new_chars_left = chars_left.difference(set(word))
        new_words = existing_words + [word]
        if len(new_chars_left) == 0:
            yield new_words
        elif len(new_words) < max_len and len(new_chars_left) < len(chars_left): 
            yield from step(new_chars_left, all_words, new_words, max_len)
        


# In[1]:


list(get_solutions('HVN AED', set(['HAVE', 'END', 'HEAD', 'MONEY', 'NAVEH', 'HAND'])))


# In[27]:


get_valid_words(['HAVE', 'END', 'HEAD', 'MONEY'], 'HVN AED')


# In[44]:


list(get_solutions(puzzles[0], max_solutions=10))

