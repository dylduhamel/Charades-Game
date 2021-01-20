from player import Player
import time as t
from tkinter import *
from tkinter.ttk import Combobox
from assets import game_categories, world_list, sports_list, art_list


class Game:
    def __init__(self, master):
        self.team_1 = Player("Team 1")
        self.team_2 = Player("Team 2")
        self.categories = game_categories
        self.chosen_category = ""
        # have each list of words for each category

        # main frame for window
        self.frame = Frame(master)
        self.frame.grid()

        # label for title
        self.top_label = Label(self.frame, text="Welcome to Dylan's Category game.", font=15)
        self.top_label.grid(column=0, row=0)

        # label for play time
        self.time_label = Label(self.frame, text="Enter round time:", font=15)
        self.time_label.grid(column=0, row=1)

        # entry for time
        self.time_entry = Entry(self.frame, width = 20)
        self.time_entry.grid(column=1, row=1, sticky="w", pady=5)

        # genre label
        self.genre_label = Label(self.frame, text="Select Genre:", font=15)
        self.genre_label.grid(column=0, row=2)

        # dropdown for genre
        self.combobox_categories = Combobox(self.frame, values=self.categories)
        self.combobox_categories.grid(column=1, row=2, sticky="w")
        self.combobox_categories.current(0)

        # start and stop buttons
        self.start_button = Button(self.frame, fg="white", text="Start", relief=RAISED,
        highlightbackground="#ff0000", padx=10, pady=5, command=self.start, width=7, height=2)
        self.start_button.grid(column=0, row=3, pady=20, columnspan=1)

        self.next_button = Button(self.frame, fg="white", text="Next", relief=RAISED, 
        highlightbackground="#ff0000", padx=10, pady=5, width=7, height=2)
        self.next_button.grid(column=1, row=3, pady=20)

        # frame for the category to be displayed
        self.category_labelframe = LabelFrame(self.frame, text="Phrase:", width=250, height=75)
        self.category_labelframe.grid(column=0, row=4, padx=18, pady=15)
        self.category_labelframe.pack_propagate(0)

        self.time_labelframe = LabelFrame(self.frame, text="Game Time:", width=250, height=75)
        self.time_labelframe.grid(column=1, row=4, pady=15)
        self.time_labelframe.pack_propagate(0)

        # label to print phrases in the labelframe
        self.phrase_label = Label(self.category_labelframe, text="")
        self.phrase_label.pack()

        # label to print time
        self.time_string = StringVar()
        self.time_label = Label(self.time_labelframe, textvariable=self.time_string)
        self.time_label.pack()

    def next(self, category_to_play):
        #return a random number from 0-end of list - find a way to stop repeats
        pass

    def start(self):
        ## WHEN CLICKED START TIMER AND DO WORD
        time = int(self.time_entry.get())
        category_lists = self.select_category(self.combobox_categories.get())

        self.phrase_label.configure(text="Put the words in here and loop")

        self.timer_countdown(time)


    def select_category(self, category):
        # choose the category list that will be used for the game
        if category == "World":
            return world_list
        elif category == "Art":
            return art_list
        elif category == "Sports":
            return sports_list

    def timer_countdown(self, time):
        count = time
        while count > 0:
            self.time_string.set(time)

            self.frame.update()
            t.sleep(1)

            count = (time - 1)
