# main.py - Conway's Game of Life, user interface
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

import argparse
from string_serialization import printField, parseString


def parse_args():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('generations', type=int)
    parser.add_argument('filename')
    return parser.parse_args()


def parse_file(filename):
    with open(filename) as f:
        initial_state_string = f.read().strip()
    return parseString(initial_state_string)


def run(initial_state, generations):
    state = initial_state
    for i in range(generations):
        state = state.successor()
    return state


def main():
    args = parse_args()
    initial_state = parse_file(args.filename)
    final_state = run(initial_state, args.generations)
    print(printField(final_state))


if __name__ == '__main__':
    main()
