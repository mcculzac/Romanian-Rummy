##########################
# Zachary McCullough
# zam.mccullough@gmail.com
# 2020-05-03
##########################

from typing import Union
from random import shuffle

# note any time in typing, a type has a '_' before it, it means the type or None
_str = Union[str, None]
_int = Union[int, None]


class Tile:

    def __init__(self, color: _str = None, number: _int = None, joly: bool = False) -> None:
        """
        Constructor. Logic is to determine what name (for repr) to use. Tiles are NOT unique
        :param color:
        :param number:
        :param joly:
        """
        self.name = 'n/a'
        self.color = color
        self.number = number
        if joly is False:
            if self.color is not None or self.number is not None:
                self.name = str(color) + ' ' + str(self.number)
        else:
            if color is None:
                raise ValueError('When creating a tile, got joly is true, but no color!')
            self.name = color + ' joly'

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class Board:

    def __init__(self, players):
        if players < 2 or players > 4:
            raise ValueError('Players must be between 2 and 4!')
        self.players = players
        self.board, self.top = self.generate_board()

    def __repr__(self):
        output = 'Top tile: ' + str(self.top) + '\n'
        for row in self.board:
            output += str(row) + '\n'

        return output

    @staticmethod
    def generate_board():
        all_tiles = []
        for i in range(2):
            for color in ['red', 'orange', 'blue', 'black']:
                for number in range(1, 14):
                    all_tiles.append(Tile(color=color, number=number))
        all_tiles.append(Tile(color='red', joly=True))
        all_tiles.append(Tile(color='black', joly=True))

        shuffle(all_tiles)

        board = [all_tiles[i:i+7] for i in range(0, 105, 7)]
        flip = all_tiles[-1]
        return board, flip


