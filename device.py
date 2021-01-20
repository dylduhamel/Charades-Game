from player import Player
from tkinter import *
from tkinter.ttk import Combobox
from assets import game_categories 


class Game:
    def __init__(self, master):
        self.team_1 = Player("Team 1")
        self.team_2 = Player("Team 2")
        self.categories = game_categories
        self.chosen_category = ""
        # have each list of words for each category

        # main frame for window
        frame = Frame(master)
        frame.grid()

        # label for title
        self.top_label = Label(frame, text="Welcome to Dylan's Category game.", font=15)
        self.top_label.grid(column=0, row=0)

        # label for play time
        self.time_label = Label(frame, text="Enter round time:", font=15)
        self.time_label.grid(column=0, row=1)

        # entry for time
        self.time_entry = Entry(frame, width = 20)
        self.time_entry.grid(column=1, row=1, sticky="w", pady=5)

        # genre label
        self.genre_label = Label(frame, text="Select Genre:", font=15)
        self.genre_label.grid(column=0, row=2)

        # dropdown for genre
        self.combobox_categories = Combobox(frame, values=self.categories)
        self.combobox_categories.grid(column=1, row=2, sticky="w")
        self.combobox_categories.current(0)

        # start and stop buttons
        self.start_button = Button(frame, fg="white", text="Start", relief=RAISED,
        highlightbackground="#ff0000", padx=10, pady=5, command=self.start, width=7, height=2)
        self.start_button.grid(column=0, row=3, pady=20, columnspan=1)

        self.next_button = Button(frame, fg="white", text="Next", relief=RAISED, 
        highlightbackground="#ff0000", padx=10, pady=5, width=7, height=2)
        self.next_button.grid(column=1, row=3, pady=20)

        # frame for the category to be displayed
        self.category_labelframe = LabelFrame(frame, text="Phrase:", width=250, height=75)
        self.category_labelframe.grid(column=0, row=4, padx=18, pady=15)
        self.category_labelframe.pack_propagate(0)

        self.time_labelframe = LabelFrame(frame, text="Game Time:", width=250, height=75)
        self.time_labelframe.grid(column=1, row=4, pady=15)
        self.time_labelframe.pack_propagate(0)

        # label to print phrases in the labelframe
        self.phrase_label = Label(self.category_labelframe, text="")
        self.phrase_label.pack()

        # label to print time
        self.time_label = Label(self.time_labelframe, text="")
        self.time_label.pack()









        """ # the main background layer
        self.canvas = Canvas(master, height=600, width = 800, background="#263D42")
        self.canvas.pack()

        # the frame for the phrases to be put
        self.phrase_frame = Frame(master, background="white")
        self.phrase_frame.place(height=100, width=450, relx=.23, rely=.4)

        # buttons for start and play
        self.start_button = Button(master, text="Start", relief=RAISED, 
        fg="white", bg="#263D42", padx=10, pady=5, command=self.start)
        self.start_button.pack()

        self.play_button = Button(master, text="Play", relief=RAISED, 
        fg="white", background="#263D42", padx=10, pady=5)
        self.play_button.pack()

        self.combobox_categories = Combobox(master, values=self.categories)
        self.combobox_categories.pack() """

    def play(self, category_to_play):
        #return a random number from 0-end of list - find a way to stop repeats
        pass

    def start(self):
        ## WHEN CLICKED START TIMER AND DO WORD
        time = int(self.time_entry.get())
        self.phrase_label.configure(text="Put the words in here and loop")

        for i in range(0,time):
            self.time_label

    def select_category(self, category):
        self.chosen_category = category