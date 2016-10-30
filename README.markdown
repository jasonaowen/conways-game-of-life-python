# Conway's Game of Life

An implementation of Conway's Game of Life in Python.

# Usage

The program takes two arguments: the number of generations to run, and a
filename containing the initial state. Populated cells are represented by a
`*` (star), and unpopulated cells by a `.` (period). There are several examples
in the `patterns/` directory.

```sh
python3 main.py 20 patterns/spaceships/glider.txt
```

This will show how far the glider has moved after 20 generations:

```
..........
..........
..........
..........
..........
..........
.......*..
........*.
......***.
..........
```

Licensed under the GPL, v3.
