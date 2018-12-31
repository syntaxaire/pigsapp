import roll


class Player:
    """The base class for strategies. As much as possible is implemented here
    to make writing additional strategies very straightforward."""

    def __init__(self, to_score):
        """Safe to call __init__ more than once per instance, if recycling
        instances for speed is desired."""
        self.to_score = to_score
        self.score = 0      # total score, preserved between turns
        self.turnscore = 0  # tracking score earned on each turn
        self.rolls = 0      # how many times we have rolled on our turn
        self.result = None  # the result of the previous roll

    def reg_opponent(self, opponent):
        """Register an opponent after both Players in a game have been
        instantiated. Some strategies consider the opponent's score."""
        self.opponent = opponent

    def process_roll(self, pigs):
        if roll.is_bust(pigs):
            self.score -= self.turnscore
            return "pass"
        val = roll.calculate(pigs)
        self.score += val
        self.turnscore += val
        if self.score >= self.to_score:
            return "win"
        return val

    def turn(self):
        """Roll, and query the player instance whether to keep rolling."""
        self.turnscore = 0
        self.rolls = 0
        rolling = True  # roll at least once
        while rolling:
            self.rolls += 1
            pigs = roll.roll()
            self.result = self.process_roll(pigs)
            if self.result in ("pass", "win"):
                return self.result
            rolling = self.keep_rolling()

    def keep_rolling():
        """Stub method overwritten with strategy."""
        return True
