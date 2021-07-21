import threading
from components.Matrix import Matrix
from helpers.goto_inline import goto_inline
from colorama import Fore, Back, Style
from helpers.logger import logger
import time

import math


class Screen:
    """This object allows to control drawing to screen
    """
    background_color = Back.BLACK

    buffer1 = Matrix((background_color, Fore.WHITE, " "))
    buffer2 = Matrix((background_color, Fore.WHITE, " "))

    def __init__(self):
        # In order to prevent do_frame() to access buffer1 while prepare_Frame is writing to it
        self._buffer1_lock = threading.Lock()
        self._buffer2_lock = threading.Lock()

    def prepare_frame(self) -> None:
        """
        Calling this method means the frame is completed and it can be drawn to screen on next frame.
        """
        with self._buffer2_lock:
            # Copy buffer2 matrix to buffer1 matrix
            with self._buffer1_lock:
                for x in range(self.buffer2.width):
                    for y in range(self.buffer2.height):
                        self.buffer1.matrix[x][y] = self.buffer2.matrix[x][y]

            # Clean buffer2
            for x in range(self.buffer2.width):
                for y in range(self.buffer2.height):
                    self.buffer2.matrix[x][y] = (
                        self.background_color, Fore.WHITE, " ")

    def do_frame(self) -> None:
        """Call this method to finally print the frame on screen."""
        # Print what is on buffer1
        counter = time.perf_counter_ns()
        with self._buffer1_lock:
            color_lock = self.__GetColor()
            s = ""
            for y in range(self.buffer1.height):
                s += goto_inline(0, y)
                for x in range(self.buffer1.width):
                    s += color_lock.Back(self.buffer1.matrix[x][y][0]) + \
                        color_lock.Fore(
                            self.buffer1.matrix[x][y][1]) + self.buffer1.matrix[x][y][2]
        logger.debug(
            f"1st took {math.floor((time.perf_counter_ns() - counter)/1000000)}ms")
        counter = time.perf_counter_ns()
        print(s, end=color_lock.Back(Back.BLACK))
        logger.debug(
            f"2st took {math.floor((time.perf_counter_ns() - counter)/1000000)}ms")
        logger.debug(f"len(s): {len(s)}")
        logger.debug(f"---------")

    def add_object(self, x: int, y: int, matrix: Matrix):
        """Add an object to the frame in order to be drawn.

        Args:
            x (int): X coordinate of the top left corner of the object in the screen.
            y (int): Y coordinate of the top left corner of the object in the screen.
            matrix (ScreenMatrix): A ScreenMatrix including only the object to be drawn.
        """
        with self._buffer2_lock:
            # This is to add to buffer2
            for x_i in range(matrix.width):
                for y_i in range(matrix.height):
                    if x+x_i < self.buffer2.width and y+y_i < self.buffer2.height:
                        self.buffer2.matrix[x+x_i][y +
                                                   y_i] = matrix.matrix[x_i][y_i]

    class __GetColor:
        """Private class made to make printing on screen more efficient, since the same color is not selected twice in a row"""
        last_used_back_color = ""
        last_used_fore_color = ""

        def Back(self, color: str):
            if self.last_used_back_color == color:
                return ""
            else:
                self.last_used_back_color = color
                return color

        def Fore(self, color: str):
            if self.last_used_fore_color == color:
                return ""
            else:
                self.last_used_fore_color = color
                return color
