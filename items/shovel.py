from . import Item


class ShovelItem(Item):

    possible_actions = ['throw']
    possible_uses = ['dig']

    def __init__(self, *args, **kwargs):
        super(ShovelItem, self).__init__('shovel', *args, **kwargs)

    @property
    def description(self):
        return (
            "The shovel looks very old, but very robust too. As you "
            "look at it, you can feel that the shovel has had a long "
            "history. It certainly isn't the most common shovel around."
        )
