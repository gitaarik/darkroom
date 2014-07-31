from console import console
from objects.ground import GroundObject
from helpers import match_word
from . import State


_ = console.message


class OtherRoom(State):

    sank = 0
    ground = GroundObject()
    ground.digged = 0

    def look(self):
        if self.ground.digged == 0:
            _("There's some ground under your feet...")
        elif self.ground.digged == 1:
            _(
                "The ground under your feet seems to be getting softer "
                "and easier to dig."
            )
        elif self.ground.digged == 2:
            _("The hole in the ground is pretty big now.")
        elif self.ground.digged == 3:
            self.sinking(False)

    def process_action(self, action):

        if action.verb == 'dig' and action.noun == 'ground':
            if action.using == 'shovel':
                self.dig()
            elif self.match_word(action.using, 'hands?'):

                if self.ground.digged > 1:
                    self.dig()
                else:
                    _(
                        "The ground is too hard to dig with your {}."
                        .format(action.using)
                    )
        elif (
            self.ground.digged > 0 and
            (
                (
                    match_word(action.verb, ['keep( on)?', 'go on']) and
                    action.noun == 'digging'
                ) or (
                    action.verb == 'dig' and action.noun == 'more'
                )
            )
        ):
            self.dig()
        else:
            return False

    def dig(self):

        if self.ground.digged == 3:
            self.sinking(True)
        else:

            if self.ground.digged == 0:
                _(
                    "You begin to dig... The ground is very hard, but "
                    "you're managing little by little."
                )
            elif self.ground.digged == 1:
                _(
                    "You keep digging... The ground starts to get softer "
                    "and the hole starts to get bigger. However, it is "
                    "hard work and you are getting tired."
                )
            elif self.ground.digged == 2:
                _(
                    "While you dig further, the ground starts to get wet "
                    "and before you know it you start to sink down into "
                    "it. The shovel starts to glow faintly."
                )

            self.ground.digged += 1

    def sinking(self, try_digging):

        if self.sank == 0:

            if try_digging:
                message = (
                    "You try to dig but the ground is becoming too muddy "
                    "and you keep on sinking. Slowly you sink futher and "
                    "futher."
                )
            else:
                message = (
                    "The ground is getting very muddy and you keep on "
                    "sinking futher and futher."
                )

            _("{}\n{}".format(
                message,
                "You're in the mud now up to your knees. The shovel is "
                "starting to glow more brightly."
            ))

        elif self.sank == 1:

            if try_digging:
                _(
                    "You try your best to dig but it doesn't work with "
                    "this mud. You start sinking rapidly now and you "
                    "are just above the mud with your arms and "
                    "shoulders."
                )
            else:
                _(
                    "The ground is getting very thin and you start "
                    "sinking rapidly now.\n"
                    "You are just above the mud with your arms and "
                    "shoulders."
                )

        elif self.sank == 2:
            _(
                "You can still grap a last bit of breath before you fully "
                "disappeared in the mud. Together with the shovel that is "
                "glowing very bright now."
            )

        self.sank += 1
