"""These strategies are added to the UI with checkboxes for participating
in tournaments. The docstring of each class is included as a tooltip."""

# HOW TO ADD YOUR OWN STRATEGY:
# Simply copy the listing of the last entry in this file and paste
# it at the bottom with a different name.

# The function keep_rolling is called after every roll. Return True to keep
# rolling and False to pass the pigs.

from Player import Player  # don't touch this line!

strategies = []


def register(func):
    strategies.append(func)
    return func


@register
class roll_once(Player):
    """Try to roll once, then pass."""
    name = "Roll once"

    def keep_rolling(self):
        return False


@register
class roll_twice(Player):
    """Try to roll twice, then hold."""
    name = "Roll twice"

    def keep_rolling(self):
        return self.rolls < 2


@register
class roll_thrice(Player):
    """Try to roll thrice, then hold."""
    name = "Roll thrice"

    def keep_rolling(self):
        return self.rolls < 3


@register
class roll_four_times(Player):
    """Try to roll four times, then hold."""
    name = "Roll four times"

    def keep_rolling(self):
        return self.rolls < 4


@register
class roll_five_times(Player):
    """Try to roll five times, then hold."""
    name = "Roll five times"

    def keep_rolling(self):
        return self.rolls < 5


class roll_greedily(Player):
    """Keep rolling until either a bust or a win."""
    name = "Greedy roller"

    def keep_rolling(self):
        return True


@register
class get15(Player):
    """Try to get 15 points, then pass."""
    name = "Go for 15"

    def keep_rolling(self):
        return self.turnscore < 15


@register
class get20(Player):
    """Try to get 20 points, then pass."""
    name = "Go for 20"

    def keep_rolling(self):
        return self.turnscore < 20


@register
class get25(Player):
    """Try to get 25 points, then pass."""
    name = "Go for 25"

    def keep_rolling(self):
        return self.turnscore < 25


@register
class get30(Player):
    """Try to get 30 points, then pass."""
    name = "Go for 30"

    def keep_rolling(self):
        return self.turnscore < 30


@register
class high_roller(Player):
    """Only pass after an individual roll worth 15 points or more."""
    name = "High roller"

    def keep_rolling(self):
        return self.result >= 15


@register
# From http://passpigs.tripod.com/strat.html
class Jonah(Player):
    """If opponent score is greater than or equal to 85% of the winning
    score or my score is greater than or equal to 90% of the winning score,
    then don't stop rolling. Otherwise, if my turn score is greater than or
    equal to 15 in one roll, then stop. Otherwise, if my score is within 20
    of my opponent's, then stop only when I pass my opponent's score.
    Otherwise, if my turn score is greater than 20, then stop. """
    name = "Jonah"

    def keep_rolling(self):
        if self.opponent.score >= (0.85 * self.to_score):
            return True
        if self.score >= (0.9 * self.to_score):
            return True
        if self.result >= 15:
            return False
        if 0 < (self.opponent.score - self.score) <= 20:
            return True
        if self.turnscore < 20:
            return True
        return False


# From http://passpigs.tripod.com/strat.html
@register
class Morgen(Player):
    """Only stop if my opponent's score is less than 80% of the winning
    score, and if my score is greater than opponent's score, and if my turn
    score is greater than 15. """
    name = "Morgen"

    def keep_rolling(self):
        if (self.opponent.score < (0.8 * self.to_score)
                and self.score > self.opponent.score
                and self.turnscore > 15):
            return False
        return True


# From http://passpigs.tripod.com/strat.html
@register
class Julia(Player):
    """If my opponent's score is less than 80% of the winning score, and if
    I'm within 20 of my opponent, and if my turn score is greater than or
    equal to twenty, then stop. Otherwise, stop if my turn score is greater
    than or equal to 15. """
    name = "Julia"

    def keep_rolling(self):
        if (self.opponent.score < (0.8 * self.to_score)
                and abs(self.score - self.opponent.score) <= 20
                and self.turnscore >= 20):
            return False
        return True

# Copy and uncomment this class, including @register, to add your own strategy
# @register
# class edit_me(Player):
#     """Enter your tooltip description here."""
#     name = "Your strategy"
#
#     def keep_rolling(self):
#         pass
