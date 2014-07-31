import imp
from importlib import import_module


class UnknownAction(Exception):

    def __init__(self, verb, *args, **kwargs):
        self.verb = verb
        self.message = "Unknown action '{}'".format(verb)
        super(UnknownAction, self).__init__(*args, **kwargs)


class WronglyFormattedAction(Exception):

    def __init__(self, words, *args, **kwargs):
        self.words = words
        self.message = "Wrongly formatted action '{}'".format(' '.join(words))
        super(WronglyFormattedAction, self).__init__(*args, **kwargs)


class Action:

    @classmethod
    def get_action(self, verb, noun, preposition, using):
        """
        Returns an action instance for the given `verb`, `noun` and
        `preposition`.
        """

        if not self.has_action(verb):
            raise UnknownAction(verb)

        action_module = import_module('.{}'.format(verb), 'actions')
        action_class_name = '{}Action'.format(verb.capitalize())
        action_class = getattr(action_module, action_class_name)

        return action_class(verb, noun, preposition, using)

    @classmethod
    def has_action(self, verb):
        try:
            imp.find_module(verb, ['actions'])
        except ImportError:
            return False
        else:
            return True

    def __init__(self, verb, noun, preposition, using):
        self.verb = verb
        self.noun = noun
        self.preposition = preposition
        self.using = using

    def can_do(self):
        """
        Returns a boolean indicating whether the action can be done by
        the player at this moment.
        """
        return True

    @property
    def cant_do_reason(self):
        """
        If `can_do()` returned `False`, this method returns a message
        describing why the action cannot be done.

        By default returns `None`.
        """
        return None
