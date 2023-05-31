from player import Player


def test_constructor():
    """
    Test the constructor of Player object
    """
    COLOR = "Red"
    POSITION = [(0, 5), (2, 5), (4, 5), (6, 5), (1, 6), (3, 6),
                (5, 6), (7, 6), (0, 7), (2, 7), (4, 7), (6, 7)]

    # Test minimal required constructor args
    a = Player(COLOR)
    assert a.team == COLOR and a.take_turn is True \
           and a.position == POSITION

    # Test with insufficient arguments
    try:
        b = Player()
    except TypeError:
        failedWithTypeError = True
    assert failedWithTypeError
