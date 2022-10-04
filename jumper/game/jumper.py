from game.art import stages


__assignment__ = "Week 3: Jumper Game"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


class Jumper:
    """A jumper that represent the remaining chances.

    The responsibility of a Jumper is to keep track of chances and show the current state.

    Attributes:
        lives: The user's remaining chances to guess.
        stages: The different states of a jumper.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): an instance of Jumper.
        """
        self.lives = len(stages) - 1
        self._stages = stages

    def show_stage(self):
        """Shows a drawing of a jumper based on the remaining number of guess.

        Args:
            self (Jumper): an instance of Jumper.

        Return:
            self._stages[self.lives]: an ascii art of a jumper.
        """
        return self._stages[self.lives]
