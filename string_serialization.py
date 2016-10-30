# string_serialization.py - Conway's Game of Life, string [de]serialization
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
NEWLINE = '\n'


def printField(field):
    return NEWLINE.join([
        ''.join([
            ALIVE_GLYPH if cell == ALIVE else DEAD_GLYPH
            for cell in row
        ]) for row in field.cells
    ])


def parseString(string):
    invalid_characters = set(string) - set([ALIVE_GLYPH, DEAD_GLYPH, NEWLINE])
    if len(invalid_characters) > 0:
        raise ValueError("Invalid character(s) in input: {}".format(
            invalid_characters
        ))

    rows = string.split(NEWLINE)
    if len(set([len(row) for row in rows])) > 1:
        raise ValueError("All rows must be of equal length!")

    height = len(rows)
    width = len(rows[0])
    if width == 0:
        raise ValueError("Cannot have empty field!")

    return RectangularField(width, height, state=[
        [
            ALIVE if cell == ALIVE_GLYPH else DEAD
            for cell in row
        ] for row in rows
    ])
