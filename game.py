#!/usr/bin/env python

import sys
from states.darkroom import Darkroom
from console import console
from player import player
from errors import ExitGame, NoNoun, UnknownAction, WronglyFormattedAction
from actions import Action
from helpers import match_word


class Game(object):

    def __init__(self):
        self.state = Darkroom()
        self.run_game()

    def run_game(self):

        while True:

            new_state = None
            console.newline()
            self.state._look()

            while not new_state:

                try:
                    user_input = console.user_prompt()
                except ExitGame:
                    console.newline()
                    console.newline()
                    self.exit()
                else:
                    self.handle_user_input(user_input)

    def handle_user_input(self, user_input):

        if user_input.strip() == '':
            console.empty_input()
        elif match_word(user_input, ['help', 'help me']):
            self.show_help()
        elif match_word(user_input, ['look', 'look around']):
            self.state._look()
        elif match_word(user_input, ['items', 'show_items']):
            self.show_items()
        elif match_word(user_input, ['exit', 'quit']):
            self.exit()
        else:

            try:
                action = self.get_action(user_input)
            except NoNoun, error:
                console.no_noun_for_verb(error.verb)
            except UnknownAction, error:
                console.unknown_action(error.verb)
            except WronglyFormattedAction:
                console.wronly_formatted_action()
            else:

                if not action.can_do():
                    console.message(action.cant_do_reason)
                else:

                    if (
                        action.verb == 'look' and
                        action.preposition == 'at' and
                        match_word(action.noun, player.items.keys())
                    ):
                        console.message(player.items[action.noun].description)
                    else:

                        new_state = self.state.process_action(action)

                        if new_state is False:
                            console.non_working_action(action)
                        elif new_state:
                            self.state = new_state

    def show_help(self):
        console.message(
            "Some common commands:\n"
            "\n"
            "   help - show this help text\n"
            "   look - shows you what's around you\n"
            "   items - show the items you have\n"
            "   exit - exit the game"
        )

    def show_items(self):

        if player.items:
            console.message(
                "Your items:\n"
                "{}".format(
                    ''.join(map(
                        lambda i: '- {}'.format(unicode(i)),
                        player.items
                    ))
                )
            )
        else:
            console.message("You don't have any items")

    def get_action(self, user_input):

        def get_words(user_input):
            return user_input.lower().split(' ')

        def get_sentence_parts(words):

            verb = words[0]
            noun = None
            preposition = None
            using = None
            using_words = ('using', 'with')

            if len(words) == 1:
                raise NoNoun(verb)
            elif len(words) > 1 and words[1] in using_words:
                if len(words) > 2:
                    raise NoNoun(verb)
                else:
                    raise WronglyFormattedAction(words)
            elif len(words) == 2:
                noun = words[1]
                preposition = None
            elif len(words) == 3:
                preposition = words[1]
                noun = words[2]
            elif len(words) == 4 and words[2] in using_words:
                noun = words[1]
                using = words[3]
            else:
                raise WronglyFormattedAction(words)

            return verb, preposition, noun, using

        words = get_words(user_input)

        if not Action.has_action(verb=words[0]):
            raise UnknownAction(words[0])

        verb, preposition, noun, using = get_sentence_parts(words)

        return Action.get_action(
            verb=verb,
            preposition=preposition,
            noun=noun,
            using=using
        )

    def exit(self):

        answer = None

        while answer not in ('yes', 'no'):

            if answer is None:
                console.message(
                    "Are you sure you want to stop playing this "
                    "awesome game? All your progress will be lost!"
                )
            else:
                console.message("Sorry... what? Please answer 'yes' or 'no'.")

            try:
                answer = console.user_prompt()
            except ExitGame:
                console.newline()
                console.newline()

            if answer == 'yes':
                console.message("Bye bye!")
                console.newline()
                sys.exit()
            elif answer == 'no':
                console.message("A very wise choice.")
                console.newline()
                self.state._look()


Game()
