from typing import Any

from colorama.ansi import Back, Fore


class Matrix:
    width: int
    height: int
    matrix: list

    def __init__(self, background_char: tuple = (Back.BLACK, Fore.WHITE, " "), width: int = 80, height: int = 24):
        """
        A matrix is a list of lists of strings (single characters).
        By default, this matrix is initialized with spaces, and a size according to the width and height parameters.

        Args:
            background_char (tuple, optional): The 1st element in the tuple is the Back color; the 2nd is the Fore color; the 3rd is the character used for background. Defaults to (Back.BLACK, Fore.WHITE, " ").
            width (int, optional): Matrix width. Defaults to 80.
            height (int, optional): Matrix height. Defaults to 25.

        Example:
        ```py
            myMatrix = ScreenMatrix(width=3, height=3)
            myMatrix.matrix[0][1] = "o" # the first index is the x axis and the second index
                                        # is the y axis, counting from the top left corner
            print(myMatrix.matrix) # when printing it looks inverted
            [
                [[" "], ["o"], [" "]], # <- Column x=0
                [[" "], [" "], [" "]], # <- Column x=1
                [[" "], [" "], [" "]]  # <- Column x=2
            ]
        ```
        """

        self.width = width
        self.height = height

        self.matrix = []
        for _ in range(self.width):
            col = []
            for _ in range(self.height):
                col.append(background_char)
            self.matrix.append(col)
