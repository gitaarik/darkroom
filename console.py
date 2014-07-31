from errors import ExitGame
import textwrap


class Console(object):

    def message(self, text):
        """
        Prints a message on the screen.
        """

        for paragraph in text.split('\n'):
            print '   {}'.format(
                '\n   '.join(
                    textwrap.wrap(paragraph, 76)
                )
            )

    def user_prompt(self):
        """
        Prompts the player for input.
        """

        self.newline()

        try:
            user_input = raw_input(' > ')
        except (KeyboardInterrupt, EOFError):
            raise ExitGame()

        self.newline()

        return user_input

    def newline(self):
        """
        Prints a newline.
        """
        print

    def empty_input(self):
        """
        Prints a message to let the player know that he should input
        some text.
        """
        self.message("What?")

    def unknown_action(self, verb):
        """
        Prints a message to let the player know that the action contains
        an unknown verb.
        """
        self.message(
            "Sorry, '{}' is not something I understand.".format(verb)
        )

    def no_noun_for_verb(self, verb):
        """
        Prints a message that let's the player know that he forgot to
        provide a noun in his action.
        """
        console.message("{} what?".format(verb))

    def non_working_action(self, action):
        """
        Prints a (possibly humurous) message to let the player know that
        the requested action doesn't work in this specific situation.
        """

        message = None

        if action.verb == 'look':

            direction = None

            if action.noun == 'up':
                direction = 'above'
            elif action.noun == 'down':
                direction = 'underneath'
            elif action.noun == 'left':
                direction = 'left from'
            elif action.noun == 'right':
                direction = 'right from'

            if direction:
                message = (
                    "There doesn't seem to be anything interesting {} you."
                    .format(direction)
                )

        else:

            if action.verb == 'hit' and action.noun == 'you':
                message = "No, thanks."
            if action.verb == 'say' and action.noun == 'fuck':
                message = "Easy man."

        if not message:
            message = "That doesn't seem to work."

        console.message(message)

    def wronly_formatted_action(self):
        console.message(
            "I don't really understand that, try formatting it "
            "differntly."
        )

console = Console()
