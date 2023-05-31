SQUARE_SIZE = 100
BOARD_SIZE = 8


def setup():
    global gc
    from game_controller import GameController
    size(SQUARE_SIZE * BOARD_SIZE, SQUARE_SIZE * BOARD_SIZE)
    gc = GameController(SQUARE_SIZE, BOARD_SIZE)


def draw():
    gc.update()


def mousePressed(self):
    gc.press_checker()


def mouseDragged(self):
    gc.drag_checker()


def mouseReleased(self):
    gc.release_checker()
