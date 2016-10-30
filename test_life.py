# life_test.py - Conway's Game of Life, unit tests
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


class TestLife(unittest.TestCase):
    def test_can_create_field(self):
        field = RectangularField(1, 1)
        self.assertIsNotNone(field)

    def test_cannot_create_negative_sized_field(self):
        with self.assertRaises(ValueError):
            field = RectangularField(0, -1)
        with self.assertRaises(ValueError):
            field = RectangularField(-1, 0)

    def test_new_field_is_unpopulated(self):
        field = RectangularField(1, 1)
        self.assertEqual(DEAD, field.cell(0, 0))

    def test_cells_outside_field_are_dead(self):
        field = RectangularField(1, 1)
        self.assertEqual(DEAD, field.cell(-1, 0))
        self.assertEqual(DEAD, field.cell(0, -1))
        self.assertEqual(DEAD, field.cell(1, 0))
        self.assertEqual(DEAD, field.cell(0, 1))

    def test_can_assign_state_at_creation(self):
        field = RectangularField(1, 1, state=[[ALIVE]])
        self.assertEqual(ALIVE, field.cell(0, 0))

    def test_cannot_assign_missized_state_at_creation(self):
        with self.assertRaises(ValueError):
            field = RectangularField(1, 1, state=[[]])
        with self.assertRaises(ValueError):
            field = RectangularField(1, 1, state=[[ALIVE, ALIVE]])
        with self.assertRaises(ValueError):
            field = RectangularField(1, 1, state=[[], []])

    def test_second_generation_of_unit_field_is_dead(self):
        dead_field = RectangularField(1, 1)
        self.assertEqual(DEAD, dead_field.successor().cell(0, 0))

        alive_field = RectangularField(1, 1, state=[[ALIVE]])
        self.assertEqual(DEAD, dead_field.successor().cell(0, 0))

    def test_second_generation_of_1d_alive_field(self):
        field = RectangularField(3, 1, state=[[ALIVE, ALIVE, ALIVE]])
        self.assertEqual(ALIVE, field.successor().cell(1, 0))

    def test_second_generation_of_2d_mostly_alive_field(self):
        field = RectangularField(2, 2, state=[[ALIVE, ALIVE],
                                              [ALIVE, DEAD]])
        second = field.successor()
        self.assertEqual(ALIVE, second.cell(0, 0))
        self.assertEqual(ALIVE, second.cell(0, 1))
        self.assertEqual(ALIVE, second.cell(1, 0))
        self.assertEqual(ALIVE, second.cell(1, 1))

    def test_second_generation_of_2d_half_alive_field_dies(self):
        field = RectangularField(2, 2, state=[[DEAD, ALIVE],
                                              [ALIVE, DEAD]])
        second = field.successor()
        self.assertEqual(DEAD, second.cell(0, 0))
        self.assertEqual(DEAD, second.cell(0, 1))
        self.assertEqual(DEAD, second.cell(1, 0))
        self.assertEqual(DEAD, second.cell(1, 1))


if __name__ == '__main__':
    unittest.main()
