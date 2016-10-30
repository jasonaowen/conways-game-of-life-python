# test_printer.py - Conway's Game of Life, pretty printer unit tests
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

import unittest

from life import RectangularField, ALIVE, DEAD
from printer import printField


class TestPrinter(unittest.TestCase):
    def test_print_one_dead_cell(self):
        field = RectangularField(1, 1)
        output = printField(field)
        self.assertEqual('.', output)

    def test_print_one_alive_cell(self):
        field = RectangularField(1, 1, state=[[ALIVE]])
        output = printField(field)
        self.assertEqual('*', output)

    def test_print_2_by_1(self):
        field = RectangularField(2, 1, state=[[ALIVE, DEAD]])
        output = printField(field)
        self.assertEqual('*.', output)

    def test_print_2_by_2(self):
        field = RectangularField(2, 2, state=[[ALIVE, DEAD],
                                              [DEAD, ALIVE]])
        output = printField(field)
        self.assertEqual('*.\n.*', output)


if __name__ == '__main__':
    unittest.main()
