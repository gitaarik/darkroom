from player import player
from helpers import match_word
from objects import Object, UnknownObject
from . import Action


class DigAction(Action):

    def can_do(self):

        cant_dig_item = False

        try:
            obj = Object.get_object(self.noun)
        except UnknownObject:
            cant_dig_item = True
        else:
            if not obj.can_apply_action(self.verb):
                cant_dig_item = True

        if cant_dig_item:
            self.cant_do_reason = "You can't dig '{}'.".format(self.noun)
            return False

        if self.using:
            if (
                match_word(self.using, 'hands?') or
                player.has_item(self.using)
            ):
                return True
            else:
                self.cant_do_reason = "You don't have a {}.".format(self.using)
                return False
        else:
            self.cant_do_reason = "Dig {} using what?".format(self.noun)
            return False
