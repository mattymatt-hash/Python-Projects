class NumberGuesser:
    def __init__(self):
        self.guessed_list = []

    def add_guess(self, guess):
        self.guessed_list.append(guess)

    def reset(self):
        self.guessed_list.clear()