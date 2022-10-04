from os import system
from game.director import Director


__assignment__ = "Week 3: Jumper Game"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


system("cls")
director = Director()
director.start_game()
