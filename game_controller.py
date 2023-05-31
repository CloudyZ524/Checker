from player import Player
from computer import Computer
from checker import Checker
from board import Board


class GameController:
    """
    The Game Controller
    """
    def __init__(self, SQUARE_SIZE, BOARD_SIZE):
        """Initialize the game controller"""
        self.BOARD_SIZE = BOARD_SIZE
        self.SQUARE_SIZE = SQUARE_SIZE
        self.board = Board(SQUARE_SIZE, BOARD_SIZE)
        self.move_count = 0
        self.player = Player("Black")
        self.player_ai = Computer("Red")
        self.black_checkers = [Checker(x, y, "Black")
                               for x, y in self.player.position]
        self.red_checkers = [Checker(x, y, "Red")
                             for x, y in self.player_ai.position]
        self.game_over = False
        self.record = False

    def update(self):
        """Updates game state on every frame"""
        self.board.display()
        self.update_board_position()
        self.finalize_move_and_switch()
        self.update_checkers()
        if self.player_ai.take_turn:
            self.ai_move()
        if self.game_over:
            self.display_end_text()
        self.end_game()

    def update_board_position(self):
        """Update the checker position on the board"""
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                self.board.position[(i, j)] = False

        if self.black_checkers:
            for c in self.black_checkers:
                self.board.position[(c.x, c.y)] = True

        if self.red_checkers:
            for c in self.red_checkers:
                self.board.position[(c.x, c.y)] = True

    def update_checkers(self):
        """Update the value of checkers"""
        if not self.red_checkers:
            self.red_checkers = []
        for checker in self.red_checkers:
            self.create_king(checker)
            self.check_valid_jump(checker)
            self.check_valid_move(checker)
            checker.display()
        for checker in self.black_checkers:
            self.create_king(checker)
            self.check_valid_jump(checker)
            checker.can_move, checker.valid_move = False, []
            checker.display()
        if True not in [c.can_jump for c in self.black_checkers]:
            for checker in self.black_checkers:
                self.check_valid_move(checker)
                checker.display()

    def finalize_move_and_switch(self):
        """Update checker position and switch players"""
        old = new = jump_c = None
        last_position = self.player.position
        self.player.position = []
        for i, c in enumerate(self.black_checkers):
            self.player.position.append((c.x, c.y))
            if abs(c.y - last_position[i][1]) == 2:
                new, old = (c.x, c.y), last_position[i]
                jump_c = c
        if len(last_position) == len(self.player.position) \
                and (old and new) and self.player.take_turn:
            print(new, old)
            self.remove_checker(new, old, "Red")
            return self.if_double_jump(jump_c)

        if last_position != self.player.position \
                and len(last_position) == len(self.player.position):
            self.player.take_turn = False
            self.player_ai.take_turn = True
            self.move_count += 1
            print("It's computer's turn.")

        old = new = jump_c = None
        last_ai_position = self.player_ai.position
        self.player_ai.position = []
        if self.red_checkers:
            for i, c in enumerate(self.red_checkers):
                self.player_ai.position.append((c.x, c.y))
                if abs(c.y - last_ai_position[i][1]) == 2:
                    new, old = (c.x, c.y), last_ai_position[i]
                    jump_c = c
            if len(last_ai_position) == len(self.player_ai.position) \
                    and old and new and self.player_ai.take_turn:
                print(new, old)
                self.remove_checker(new, old, "Black")
                return self.if_double_jump(jump_c)

        if last_ai_position != self.player_ai.position \
                and len(last_ai_position) == len(self.player_ai.position):
            self.player.take_turn = True
            self.player_ai.take_turn = False
            self.move_count += 1
            print("It's player's turn.")

    def if_double_jump(self, checker):
        self.update_board_position()
        self.check_valid_jump(checker)
        if self.player_ai.take_turn:
            if checker.valid_jump:
                print("Can jump, It's computer's turn.")
            else:
                self.player.take_turn = True
                self.player_ai.take_turn = False
                self.move_count += 1
                print("It's player's turn.")
                return
        if self.player.take_turn:
            if checker.valid_jump:
                print("Can jump, It's player's turn.")
            else:
                self.player.take_turn = False
                self.player_ai.take_turn = True
                self.move_count += 1
                print("It's computer's turn.")

    def create_king(self, checker):
        """Make a king checker """
        if checker.y == 0 and checker.color == "Black":
            if not checker.king:
                checker.king = True
                print("This checker became a King")
        if checker.y == self.BOARD_SIZE - 1 and checker.color == "Red":
            if not checker.king:
                checker.king = True
                print("This checker became a King")

    def check_valid_jump(self, checker):
        """Check valid jump of black checkers"""
        JUMP_STEP = 2
        MOVE_STEP = 1
        checker.can_jump = False
        checker.valid_jump = []
        x, y = checker.x, checker.y

        if checker.color == "Black" or \
                (checker.color == "Red" and checker.king):
            if x - JUMP_STEP >= 0 and y - JUMP_STEP >= 0 \
                    and not self.board.position[(x - JUMP_STEP, y-JUMP_STEP)] \
                    and self.board.position[(x - MOVE_STEP, y - MOVE_STEP)]:
                if (checker.color == "Black" and (x - MOVE_STEP, y - MOVE_STEP)
                    not in self.player.position) or (checker.color == "Red" and
                   (x - MOVE_STEP, y-MOVE_STEP)not in self.player_ai.position):
                    checker.can_jump = True
                    checker.valid_jump.append((x - JUMP_STEP, y - JUMP_STEP))

            if x + JUMP_STEP < self.BOARD_SIZE and y - JUMP_STEP >= 0 \
                    and not self.board.position[(x + JUMP_STEP, y-JUMP_STEP)] \
                    and self.board.position[(x + MOVE_STEP, y - MOVE_STEP)]:
                if (checker.color == "Black" and (x + MOVE_STEP, y - MOVE_STEP)
                    not in self.player.position) or (checker.color == "Red" and
                   (x + MOVE_STEP, y-MOVE_STEP)not in self.player_ai.position):
                    checker.can_jump = True
                    checker.valid_jump.append((x + JUMP_STEP, y - JUMP_STEP))

        if checker.color == "Red" or \
                (checker.color == "Black" and checker.king):
            if x - JUMP_STEP >= 0 and y + JUMP_STEP < self.BOARD_SIZE \
                    and not self.board.position[(x - JUMP_STEP, y+JUMP_STEP)]\
                    and self.board.position[(x - MOVE_STEP, y + MOVE_STEP)]:
                if (checker.color == "Black" and (x - MOVE_STEP, y + MOVE_STEP)
                    not in self.player.position) or (checker.color == "Red" and
                   (x - MOVE_STEP, y+MOVE_STEP)not in self.player_ai.position):
                    checker.can_jump = True
                    checker.valid_jump.append((x - JUMP_STEP, y + JUMP_STEP))

            if x + JUMP_STEP < self.BOARD_SIZE \
                    and y + JUMP_STEP < self.BOARD_SIZE \
                    and not self.board.position[(x + JUMP_STEP, y+JUMP_STEP)]\
                    and self.board.position[(x + MOVE_STEP, y + MOVE_STEP)]:
                if (checker.color == "Black" and (x + MOVE_STEP, y + MOVE_STEP)
                    not in self.player.position) or (checker.color == "Red" and
                   (x + MOVE_STEP, y+MOVE_STEP)not in self.player_ai.position):
                    checker.can_jump = True
                    checker.valid_jump.append((x + JUMP_STEP, y + JUMP_STEP))

    def check_valid_move(self, checker):
        """Check valid move of checkers"""
        MOVE_STEP = 1
        checker.can_move = False
        checker.valid_move = []
        x, y = checker.x, checker.y

        if checker.color == "Black" or \
                (checker.color == "Red" and checker.king):
            if x - MOVE_STEP >= 0 and y - MOVE_STEP >= 0 \
                    and not self.board.position[(x - MOVE_STEP, y-MOVE_STEP)]:
                checker.can_move = True
                checker.valid_move.append((x - MOVE_STEP, y - MOVE_STEP))

            if x + MOVE_STEP < self.BOARD_SIZE and y - MOVE_STEP >= 0 \
                    and not self.board.position[(x + MOVE_STEP, y-MOVE_STEP)]:
                checker.can_move = True
                checker.valid_move.append((x + MOVE_STEP, y - MOVE_STEP))
        if checker.color == "Red" or \
                (checker.color == "Black" and checker.king):
            if x - MOVE_STEP >= 0 and y + MOVE_STEP < self.BOARD_SIZE \
                    and not self.board.position[(x - MOVE_STEP, y+MOVE_STEP)]:
                checker.can_move = True
                checker.valid_move.append((x - MOVE_STEP, y + MOVE_STEP))

            if x + MOVE_STEP < self.BOARD_SIZE and \
                    y + MOVE_STEP < self.BOARD_SIZE \
                    and not self.board.position[(x + MOVE_STEP, y+MOVE_STEP)]:
                checker.can_move = True
                checker.valid_move.append((x + MOVE_STEP, y + MOVE_STEP))

    def drag_checker(self):
        """Drag checkers"""
        if self.player.take_turn:
            for checker in self.black_checkers:
                if checker.can_move or checker.can_jump:
                    checker.mouseDragged()

    def release_checker(self):
        """Release checkers"""
        if self.player.take_turn:
            for checker in self.black_checkers:
                checker.mouseReleased()

    def press_checker(self):
        """Press checkers"""
        if self.player.take_turn:
            for checker in self.black_checkers:
                checker.mousePressed()

    def remove_checker(self, new_pos, old_pos, team):
        """remove the rival's checker"""
        target_x = (new_pos[0] + old_pos[0]) // 2
        target_y = (new_pos[1] + old_pos[1]) // 2
        if team == "Red":
            for i, c in enumerate(self.red_checkers):
                if c.x == target_x and c.y == target_y:
                    print(c.x, c.y, c.color)
                    self.red_checkers.remove(self.red_checkers[i])
                    return
        if team == "Black":
            for i, c in enumerate(self.black_checkers):
                if c.x == target_x and c.y == target_y:
                    print(c.x, c.y, c.color)
                    self.black_checkers.remove(self.black_checkers[i])
                    return

    def end_game(self):
        """Check the result of game"""
        TOTAL_CHECKERS = 24

        if not self.game_over:
            if not self.red_checkers:
                self.game_over = "win"
                return
            if len(self.black_checkers) == 0:
                self.game_over = "lose"
                return
            if self.move_count > 50 and len(self.player.position
               + self.player_ai.position) == TOTAL_CHECKERS:
                self.game_over = "draw"
                return
            black_valid_move = []
            for c in self.black_checkers:
                black_valid_move += c.valid_move
                black_valid_move += c.valid_jump
            if not black_valid_move:
                self.game_over = "lose"
                return
            red_valid_move = []
            for c in self.red_checkers:
                red_valid_move += c.valid_move
                red_valid_move += c.valid_jump
            if not red_valid_move:
                self.game_over = "win"
                return

    def display_end_text(self):
        """Display end of game message"""
        TEXT_SIZE = 120
        if self.game_over == "lose":
            message = "Red wins!"
        elif self.game_over == "win":
            message = "Black wins!"
        elif self.game_over == "draw":
            message = "Draw!"
        center = self.SQUARE_SIZE * self.BOARD_SIZE // 2
        offset = 3
        textSize(TEXT_SIZE)
        textAlign(CENTER, CENTER)
        fill(0)
        text(message, center+offset, center+offset)
        fill(255)
        text(message, center, center)
        self.record_winner()

    def ai_move(self):
        """Computer player play the checker"""
        if self.player_ai.countdown > 0:
            self.player_ai.countdown -= 1
        if self.player_ai.countdown == 0:
            self.red_checkers = self.player_ai.computer_move(self.red_checkers)
            self.initiate_delay()

    def record_winner(self):
        """Keep track of the winners in a file"""
        if not self.record and self.game_over == "win":
            ranking = {}
            try:
                file = open("score.txt", "r+")
            except OSError as e:
                print("Can't open score.txt for writing")
            for line in file:
                if line == "\n":
                    continue
                line = line.split()
                name = line[0]
                score = int(line[1])
                ranking[name] = score
            winner = self.input("Enter your name: ")
            ranking[winner] = ranking.get(winner, 0) + 1
            ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
            file.seek(0)
            for name, score in ranking:
                file.write(name + " " + str(score) + "\n")
        self.record = True

    def input(self, message=''):
        """Overwrite the input method"""
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def initiate_delay(self):
        """Initialze the coundown of delay"""
        COUNTDOWN = 50
        self.player_ai.countdown = COUNTDOWN
