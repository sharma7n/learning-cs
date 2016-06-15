# Board class client

from board import Board

# b = Board()

b = Board.get_instance()
b.set_size(15)

b2 = Board.get_instance()
assert b2 == b
print(str(b2.get_size()))