import random


__assignment__ = "Week 3: Jumper Game"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


class Puzzle:
    """A puzzle that represents the word that needs to be guessed.

    The responsibility of a Puzzle is to handle the words that needs to be guessed by the user.

    Attributes:
        word_list: List of words.
        word_selected: The random word from the word_list that needs to be guessed.
        word_guess: Hint to the user with the representation of underscore.
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): an instance of Puzzle.
        """
        self._word_list = ["word", "jump", "brothers"]
        self._word_selected = self._word_list[random.randint(
            0, len(self._word_list)-1)]
        self._word_guess = ["_"] * len(self._word_selected)

    def draw_word_guess(self):
        """Returns a string of underscores or letters.

        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return f"{' '.join(self._word_guess)}"

    def is_guess_incorrect(self, guess_letter):
        """Returns a boolean if the guess is correct or not.

        Args:
            self (Puzzle): an instance of Puzzle.
            guess_letter: the letter guessed by the user.
        """
        for i in range(len(self._word_selected)):
            letter = self._word_selected[i]

            if letter == guess_letter:
                self._word_guess[i] = letter

        return guess_letter not in self._word_selected

    def can_keep_guessing(self):
        """Returns a boolean if there are still underscores in the word_guess.

        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return "_" in self._word_guess
