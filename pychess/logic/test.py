
def convert_square_to_index(self, square: str) -> tuple[int, int]:
    letter = square[0]
    number = int(square[1])

    row_index = 8 - number
    column_index = ord(letter) - ord("a")

    return (row_index, column_index)