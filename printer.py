# printer.py - Conway's Game of Life, pretty printer
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

from life import RectangularField, ALIVE, DEAD


ALIVE_GLYPH = '*'
DEAD_GLYPH = '.'


def printField(field):
    return '\n'.join([
        ''.join([
            ALIVE_GLYPH if cell == ALIVE else DEAD_GLYPH
            for cell in row
        ]) for row in field.cells
    ])
