from game_controller import GameController


SQUARE_SIZE = 100
BOARD_SIZE = 5


def test_constructor():
    """
    Test the constructor of GameController object
    """
    # Test minimal required constructor args
    gc = GameController(SQUARE_SIZE, BOARD_SIZE)
    assert gc.SQUARE_SIZE == SQUARE_SIZE \
        and gc.BOARD_SIZE == BOARD_SIZE \
        and gc.move_count == 0 \
        and not gc.game_over and not gc.record \
        and gc.player.__class__.__name__ == "Player" \
        and gc.player_ai.__class__.__name__ == "Computer" \
        and gc.board.__class__.__name__ == "Board" \
        and gc.black_checkers[0].__class__.__name__ == "Checker" \
        and gc.red_checkers[0].__class__.__name__ == "Checker"

    # Test with insufficient arguments
    try:
        gc2 = GameController(BOARD_SIZE)
    except TypeError:
        failedWithTypeError = True
    assert failedWithTypeError


def test_end_game():
    """
    Test the end_game method
    """
    MOVE = 55
    gc = GameController(SQUARE_SIZE, BOARD_SIZE)
    gc2 = GameController(SQUARE_SIZE, BOARD_SIZE)
    gc3 = GameController(SQUARE_SIZE, BOARD_SIZE)

    gc.red_checkers = []
    gc.end_game()
    assert gc.game_over == "win"

    gc2.black_checkers = []
    gc2.end_game()
    assert gc2.game_over == "lose"

    gc3.move_count = MOVE
    gc3.end_game()
    assert gc3.game_over == "draw"
