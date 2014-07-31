from player import player
from console import console
from items.shovel import ShovelItem
from .otherroom import OtherRoom
from . import State


class Darkroom(State):

    def look(self):

        if self.look_count == 0:
            console.message("You are in a dark room and you don't see anything")
        elif self.look_count == 1:
            console.message(
                "It's really dark and even though you have your eyes "
                "wide open you can't see anything."
            )
        else:
            console.message(
                "It's still pitch dark and your eyes don't seem to get "
                "used to this kind of darkness."
            )

    def process_action(self, action):

        if action.verb != 'say':
            return False

        valid_sayings = (
            'hello',
            '(wa?)?jow?',
            'yo'
        )

        if self.match_word(action.noun, valid_sayings):

            console.message(
                '"Jow", a low voice responds. The figure walks up to you and '
                "looks you in the eye, although you don't see anything, "
                "because it's still dark.\n"
                "He hands you over a shovel and then leaves. You now have a "
                "shovel."
            )

            player.add_item(ShovelItem())

            return OtherRoom()

        else:
            return False
