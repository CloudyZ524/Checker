from checker import Checker


def test_constructor():
    """
    Test the constructor of Checker object
    """
    SQUARE_SIZE = 100
    HALF_SQAURE = 50
    X1, Y1 = 0, 3
    X2, Y2 = 4, 6
    COLOR1 = "Blue"
    COLOR2 = "Pink"
    BOARD_X1 = HALF_SQAURE + 0 * SQUARE_SIZE
    BOARD_Y1 = HALF_SQAURE + 3 * SQUARE_SIZE
    BOARD_X2 = HALF_SQAURE + 4 * SQUARE_SIZE
    BOARD_Y2 = HALF_SQAURE + 6 * SQUARE_SIZE

    # Test minimal required constructor args
    a = Checker(X1, Y1, COLOR1)
    assert a.x == X1 and a.y == Y1 and a.color == COLOR1 \
        and a.board_x == BOARD_X1 \
        and a.board_y == BOARD_Y1 \
        and a.SQUARE_SIZE == SQUARE_SIZE \
        and a.HALF_SQAURE == HALF_SQAURE \
        and not a.can_jump and not a.can_move \
        and not a.dragged and not a.king \
        and hasattr(a, "valid_move") \
        and hasattr(a, "valid_jump")

    b = Checker(X2, Y2, COLOR2)
    assert b.x == X2 and b.y == Y2 and b.color == COLOR2 \
        and b.board_x == BOARD_X2 \
        and b.board_y == BOARD_Y2 \
        and b.SQUARE_SIZE == SQUARE_SIZE \
        and b.HALF_SQAURE == HALF_SQAURE \
        and not b.can_jump and not b.can_move \
        and not b.dragged and not b.king \
        and hasattr(b, "valid_move") \
        and hasattr(b, "valid_jump")

    # Test with insufficient arguments
    try:
        c = Checker(X1, Y2)
    except TypeError:
        failedWithTypeError = True
    assert failedWithTypeError
