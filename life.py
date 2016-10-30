# life.py - Conway's Game of Life
# Copyright (C) 2016 Jason Owen

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

ALIVE = True
DEAD = False


class RectangularField:
    def __init__(self, width, height, state=None):
        if height <= 0 or width <= 0:
            raise ValueError("Width and height must be positive!")
        if state is not None:
            if height != len(state):
                raise ValueError("Heights must match!")
            for row in state:
                if len(row) != width:
                    raise ValueError("Widths must match!")
        self.width = width
        self.height = height
        self.cells = state or [[DEAD] * width for i in range(height)]

    def cell(self, x, y):
        """Convenience function to look up the state of a cell.

        Cells outside the rectangular field are dead."""

        if x in range(self.width) and y in range(self.height):
            return self.cells[y][x]
        else:
            return DEAD

    def nextCellState(self, x, y):
        """Use the optimization described in
        https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Algorithms :

        > To avoid decisions and branches in the counting loop, the rules can be
        > rearranged from an egocentric approach of the inner field regarding
        > its neighbors to a scientific observer's viewpoint: if the sum of all
        > nine fields is 3, the inner field state for the next generation will
        > be life (no matter of its previous contents); if the all-field sum is
        > 4, the inner field retains its current state and every other sum sets
        > the inner field to death.
        """
        x_range = [x-1, x, x+1]
        y_range = [y-1, y, y+1]
        cells = [self.cell(x, y) for x in x_range for y in y_range]
        cell_sum = sum(cells)
        if cell_sum == 3:
            return ALIVE
        elif cell_sum == 4:
            return self.cell(x, y)
        else:
            return DEAD


    def successor(self):
        return RectangularField(
            self.width,
            self.height,
            [
                [self.nextCellState(x, y)
                    for x in range(self.width)]
                for y in range(self.height)
            ]
        )
