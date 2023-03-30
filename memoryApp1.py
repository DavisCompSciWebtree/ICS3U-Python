import tkinter as tk
import random

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Card Game")
        self.master.resizable(width=False, height=False)

        # Create a list of symbols to use for the cards
        self.symbols = [
            "\u2660", # spade suit
            "\u2665", # heart suit
            "\u2666", # diamond suit
            "\u2663", # club suit
            "\u2600", # sun
            "\u2601", # cloud
            "\u263A", # smiley face
            "\u263B", # black smiley face
            "\u2615", # hot beverage
            "\u2668", # hot springs
        ]
        self.card_symbols = self.symbols + self.symbols

        # Shuffle the card symbols
        random.shuffle(self.card_symbols)

        # Create a list to hold the card buttons
        self.cards = []

        # Create a grid of card buttons
        for row in range(4):
            for col in range(5):
                index = row * 5 + col
                card = tk.Button(self.master, width=6, height=3, font=("Arial", 24), command=lambda i=index: self.card_click(i))
                card.grid(row=row+1, column=col, padx=5, pady=5)
                self.cards.append(card)

        # Keep track of the currently selected cards
        self.selected_cards = []

        # Keep track of the number of pairs found
        self.pairs_found = 0

    def card_click(self, index):
        # Ignore clicks on cards that have already been matched
        if self.cards[index]["state"] == "disabled":
            return

        # Flip the card over to reveal the symbol
        self.cards[index].config(text=self.card_symbols[index], state="disabled")

        # Add the card to the list of selected cards
        self.selected_cards.append((index, self.card_symbols[index]))

        # Check if two cards have been selected
        if len(self.selected_cards) == 2:
            self.master.after(1000, self.check_selection)

    def check_selection(self):
        # Check if the two selected cards match
        if self.selected_cards[0][1] == self.selected_cards[1][1]:
            # Disable the matched cards
            for index, symbol in self.selected_cards:
                self.cards[index].config(state="disabled")

            # Clear the list of selected cards
            self.selected_cards = []

            # Increment the number of pairs found
            self.pairs_found += 1

            # Check if all pairs have been found
            if self.pairs_found == 10:
                tk.messagebox.showinfo(title="Game Over", message="Congratulations! You won the game!")
        else:
            # Flip the cards back over
            for index, symbol in self.selected_cards:
                self.cards[index].config(text="", state="normal")

            # Clear the list of selected cards
            self.selected_cards = []

root = tk.Tk()
app = MemoryGame(root)
root.mainloop()
