from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


__assignment__ = "Week 3: Jumper Game"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's puzzle.
        is_playing (boolean): Whether or not to keep playing.
        jumper (Seeker): The game's jumper.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self._guess_letter = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service.write_text(self._puzzle.draw_word_guess())
        self._terminal_service.write_text(self._jumper.show_stage())
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Ask the user to guess a letter.

        Args:
            self (Director): An instance of Director.
        """

        self._guess_letter = self._terminal_service.read_text(
            "\nGuess a letter [a-z]: "
        )

    def _do_updates(self):
        """Check if user's letter guess is a valid alphabet and process the guess.

        Args:
            self (Director): An instance of Director.
        """
        if self._guess_letter.isalpha():
            if self._puzzle.is_guess_incorrect(self._guess_letter):
                self._jumper.lives -= 1

    def _do_outputs(self):
        """Shows the current stage of the jumper based on the remaining guess chances.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._puzzle.draw_word_guess()
        self._terminal_service.write_text(hint)

        jumper_state = self._jumper.show_stage()
        self._terminal_service.write_text(jumper_state)

        if not self._puzzle.can_keep_guessing():
            self._is_playing = False
            self._terminal_service.write_text("Congratulations! You Won!")

        if self._jumper.lives == 0:
            self._is_playing = False
            self._terminal_service.write_text("Game Over! You Lose!")
