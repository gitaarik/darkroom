class ExitGame(Exception):
    pass


class NoNoun(Exception):

    def __init__(self, verb):
        self.verb = verb
        self.message = "No noun for verb '{}'".format(verb)


class UnknownAction(Exception):

    def __init__(self, verb, *args, **kwargs):
        self.verb = verb
        self.message = "Unknown action '{}'".format(verb)
        super(UnknownAction, self).__init__(*args, **kwargs)


class WronglyFormattedAction(Exception):

    def __init__(self, words, *args, **kwargs):
        self.words = words
        self.message = "Wrong format for action: {}".format(' '.join(words))
        super(WronglyFormattedAction, self).__init__(*args, **kwargs)
