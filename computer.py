class Computer:
    """
    Create a Computer player
    """
    def __init__(self, team):
        """Initialize the AI player"""
        COUNTDOWN = 50
        self.SQUARE_SIZE = 100
        self.HALF_SQAURE = 50
        self.team = team
        self.take_turn = False
        self.position = [[1, 0], [3, 0], [5, 0], [7, 0], [0, 1], [2, 1],
                         [4, 1], [6, 1], [1, 2], [3, 2], [5, 2], [7, 2]]
        self.countdown = COUNTDOWN

    def computer_move(self, cherkers):
        """Make red checker move and jump"""
        for i, c in enumerate(cherkers):
            if c.can_jump:
                cherkers[i].x = c.valid_jump[0][0]
                cherkers[i].y = c.valid_jump[0][1]
                cherkers[i].board_x = self.HALF_SQAURE + \
                    cherkers[i].x * self.SQUARE_SIZE
                cherkers[i].board_y = self.HALF_SQAURE + \
                    cherkers[i].y * self.SQUARE_SIZE
                return cherkers

        for i, c in enumerate(cherkers):
            if c.can_move:
                cherkers[i].x = c.valid_move[0][0]
                cherkers[i].y = c.valid_move[0][1]
                cherkers[i].board_x = self.HALF_SQAURE + \
                    cherkers[i].x * self.SQUARE_SIZE
                cherkers[i].board_y = self.HALF_SQAURE + \
                    cherkers[i].y * self.SQUARE_SIZE
                return cherkers
