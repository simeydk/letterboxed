from dataclasses import dataclass, field
from functools import cached_property, lru_cache
import heapq
from typing import List, Set, Dict, Tuple
from sowpods import SOWPODS
import string

@dataclass(frozen = True)
class Letterboxed():

    puzzle_string: str
    dictionary: Tuple[str] = field(default_factory=lambda: tuple(SOWPODS))
    min_word_len: int = 3

    @cached_property
    def mapper(self) -> Dict[str, int]:
        mapper = {char: 0 for char in string.ascii_uppercase}
        for i, side in enumerate(self.puzzle_string.split(' ')):
            for c in side:
                mapper[c] = i+1
        return mapper

    def map_word(self, word: str) -> List[int]:
        """
        Map a word to a list of the sides of its letters
        """
        return [self.mapper[c] for c in word]

    def is_valid_word(self, word) -> bool:
        """
        Check if a word can be written in the given puzzle
        """
        mapped = self.map_word(word)
        if 0 in mapped: return False
        for i in range(len(mapped) - 1):
            if mapped[i] == mapped[i+1]:
                return False
        return True
    
    @cached_property
    def valid_words(self) -> List[str]:
        """
        returns all the valid words in the puzzle
        """
        valid_words = [word for word in self.dictionary if (self.is_valid_word(word) and (len(word) >= self.min_word_len))]
        valid_words.sort(key = lambda s: (self.score((s,)), -len(set(s)), -len(s)))
        return valid_words

    @cached_property
    def chars(self) -> Set[str]:
        """
        return a set of all the valid characters in the puzzle
        """
        return set(char for char in self.puzzle_string if char != ' ')

    @lru_cache(26)
    def starts_with(self, start: str) -> Set[str]:
        """
        returns all valid words that starts with a given letter
        """
        return set(word for word in self.valid_words if word.startswith(start))
    
    @lru_cache
    def score(self, words: Tuple[str]) -> int:
        """
        returns the number of remaining characters for a tuple of words
        """
        return len(self.chars.difference(set(''.join(words))))

    def get_solutions(self, max_solutions = 1000, max_len = 5):    
        """
            Get multiple solutions
            max_solutions: maximum number of solutions to return
            max_len: maximum length of a solution
        """
        
        # list of solution tuples        
        solutions = []

        # Priority queue of (score, word) tuples
        queue: List[tuple] = []
        push = lambda words: heapq.heappush(queue, (self.score(words), words))

        # for Djikstra or A* you normally need to keep track of nodes already visited, 
        # but for this problem we know each pach is unique so we don't have to do this 

        # initialise the list with all valid words, sorted by 
        for word in self.valid_words: push((word,))

        while queue:
            score, words = heapq.heappop(queue)

            if score == 0:
                solutions.append(words)
                if len(solutions) == max_solutions: return solutions
                continue

            if len(words) == max_len: continue

            last_char = words[-1][-1]
            next_words = self.starts_with(last_char)
            for next_word in next_words:
                push(words + (next_word,))

        return solutions