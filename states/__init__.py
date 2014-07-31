from helpers import match_word


class State(object):

    def __init__(self):
        self.look_count = 0

    def _look(self):
        self.look()
        self.look_count += 1

    def match_word(self, word, valid_matches):
        return match_word(word, valid_matches)
