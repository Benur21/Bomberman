import time
import cursor
from components import *
from colorama import init as colorama_init
from colorama import Fore, Back, Style
from helpers.logger import logger
import threading
colorama_init()
cursor.hide()

screen = Screen()
board = Board()


def draw_thread():
    while True:
        screen.do_frame()
        time.sleep(0.04)


def components_thread():
    while True:
        board.draw(screen)
        screen.prepare_frame()
        time.sleep(0.04)


threading.Thread(target=draw_thread, daemon=True).start()
threading.Thread(target=components_thread, daemon=True).start()

'''
a = ScreenMatrix(width=5, height=2)
a.matrix[0][1] = "o"
a.
'''

input("")
