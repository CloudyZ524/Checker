class Player:
    """
    Create the black team player
    """
    def __init__(self, team):
        """Initialize the player"""
        self.team = team
        self.take_turn = True
        self.position = [(0, 5), (2, 5), (4, 5), (6, 5), (1, 6), (3, 6),
                         (5, 6), (7, 6), (0, 7), (2, 7), (4, 7), (6, 7)]
