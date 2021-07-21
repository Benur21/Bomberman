from colorama.ansi import Back, Fore
from components.Screen import Screen
from components.Matrix import Matrix


class Board:
    x: int
    y: int
    width: int
    height: int

    def __init__(self):
        self.x = 1
        self.y = 1
        self.width = 17
        self.height = 7

    def draw(self, screen: Screen) -> None:
        """Draw this board to the screen. It's the delimitation of the game, the unbreakable walls surrounding everything.

        Args:
            screen (Screen): The screen object to which the object should be drawn.
        """

        new_obj = Matrix((Back.BLACK, Fore.WHITE, " "),
                         self.width, self.height)

        for x in range(new_obj.width):
            new_obj.matrix[x][0] = (Back.BLACK, Fore.GREEN, "█")
            new_obj.matrix[x][new_obj.height-1] = (Back.BLACK, Fore.GREEN, "█")
        for y in range(new_obj.height):
            new_obj.matrix[0][y] = (Back.BLACK, Fore.GREEN, "█")
            new_obj.matrix[new_obj.width-1][y] = (Back.BLACK, Fore.GREEN, "█")

        screen.add_object(self.x, self.y, new_obj)
