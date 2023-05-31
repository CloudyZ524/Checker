from board import Board


def test_constructor():
    """
    Test the constructor of Board object
    """
    SQUARE = 50
    SQUARE2 = 100
    BOARD = 3
    BOARD2 = 2
    POSITION = {(0, 0): False, (0, 1): False, (0, 2): False,
                (1, 0): False, (1, 1): False, (1, 2): False,
                (2, 0): False, (2, 1): False, (2, 2): False}
    POSITION2 = {(0, 0): False, (0, 1): False,
                 (1, 0): False, (1, 1): False}

    # Test minimal required constructor args
    a = Board(SQUARE, BOARD)
    assert a.SQUARE_SIZE == SQUARE and a.BOARD_SIZE == BOARD \
           and a.position == POSITION

    b = Board(SQUARE2, BOARD2)
    assert b.SQUARE_SIZE == SQUARE2 and b.BOARD_SIZE == BOARD2 \
           and b.position == POSITION2

    # Test with insufficient arguments
    try:
        c = Board(SQUARE)
    except TypeError:
        failedWithTypeError = True
    assert failedWithTypeError
