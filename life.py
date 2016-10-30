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
    def __init__(self, height, width, state=None):
        if height <= 0 or width <= 0:
            raise ValueError("Width and height must be positive!")
        self.height = height
        self.width = width
        self.cells = state or [[DEAD] * width for i in range(height)]

    def cell(self, x, y):
        if x in range(self.width) and y in range(self.height):
            return self.cells[y][x]
        else:
            raise IndexError
