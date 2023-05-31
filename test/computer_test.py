from computer import Computer


def test_constructor():
    """
    Test the constructor of Player object
    """
    SQUARE_SIZE = 100
    HALF_SQAURE = 50
    COUNTDOWN = 50
    COLOR = "Purple"
    POSITION = [[1, 0], [3, 0], [5, 0], [7, 0], [0, 1], [2, 1],
                [4, 1], [6, 1], [1, 2], [3, 2], [5, 2], [7, 2]]

    # Test minimal required constructor args
    a = Computer(COLOR)
    assert a.SQUARE_SIZE == SQUARE_SIZE \
        and a.HALF_SQAURE == HALF_SQAURE \
        and a.team == COLOR \
        and a.position == POSITION \
        and a.countdown == COUNTDOWN \
        and not a.take_turn

    # Test with insufficient arguments
    try:
        b = Computer()
    except TypeError:
        failedWithTypeError = True
    assert failedWithTypeError


def test_computer_move():
    pass
