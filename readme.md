# Letterboxed Solver

This repo contains a python script to solve the [New York Times Letterboxed Puzzle](https://www.nytimes.com/puzzles/letter-boxed).

## Word list
For a list of valid english words, the script makes use of the [SOWPODS wordlist used for Scrablle](https://en.wikipedia.org/wiki/Collins_Scrabble_Words). The list was sourced from here [this GitHub repo from Jessica McKellar](https://github.com/jesstess/Scrabble)

## Algorithm
The script makes use of [Djikstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find the shortest possible solution.