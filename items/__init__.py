import imp
from importlib import import_module


class UnknownItem(Exception):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.message = "Unknown item '{}'".format(name)
        super(UnknownItem, self).__init__(*args, **kwargs)


class Item(object):

    possible_actions = None
    possible_uses = None

    @classmethod
    def get_item(self, name, quantity=1):

        if not self.has_item(name):
            raise UnknownItem(name)

        item_module = import_module('.{}'.format(name), 'items')
        item_class_name = '{}Item'.format(name.capitalize())
        item_class = getattr(item_module, item_class_name)

        return item_class(quantity=quantity)

    @classmethod
    def has_item(self, name):
        try:
            imp.find_module(name, ['items'])
        except ImportError:
            return False
        else:
            return True

    def __init__(self, name, quantity=1):
        self.name = name
        self.quantity = 1

    def __unicode__(self):

        if self.quantity > 1:
            quantity_text = ' ({})'.format(self.quantity)
        else:
            quantity_text = ''

        return '{}{}'.format(self.name, quantity_text)

    def can_apply_action(self, action):
        """
        Returns whether you can apply the given `action` on this item.

        True means yes
        False means no
        None means unknown

        If `self.possible_actions` is `None`, this method will return
        `None`. Otherwise, it will check if the provided `action` is in
        `self.possible_actions` (which is assumed to be a list if it's
        not `None`) and return `True` if it's in the list and `False` if
        it's not.

        Any item can overwrite this method to have custom behaviour.
        """
        if self.possible_actions:
            if action in self.possible_actions:
                return True
            else:
                return False
        else:
            return None

    def can_use_for_action(self, action):
        """
        Returns whether this item can be used for the given `action`.

        True means yes
        False means no
        None means unknown

        If `self.possible_uses` is `None`, this method will return
        `None`. Otherwise, it will check if the provided `action` is in
        `self.possible_uses` (which is assumed to be a list if it's not
        `None`) and return `True` if it's in the list and `False` if
        it's not.

        Any item can overwrite this method to have custom behaviour.
        """
        if self.possible_uses:
            if action in self.possible_uses:
                return True
            else:
                return False
        else:
            return None
