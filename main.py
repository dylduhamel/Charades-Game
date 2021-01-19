from assets import game_categories
from player import Player
from device import Game
from tkinter import *


if __name__ == "__main__":
    # have start butten which asks for team names, and creates the game object
    # then select category 
    # then ask if you are ready to play? button
    # show a random word in that category
    root = Tk()
    root.title("Dylan Phrase")
    root.geometry("550x300")
    Game(root)
    root.mainloop()