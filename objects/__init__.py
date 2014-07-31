import imp
from importlib import import_module


class UnknownObject(Exception):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.message = "Unknown object '{}'".format(name)
        super(UnknownObject, self).__init__(*args, **kwargs)


class Object(object):

    @classmethod
    def get_object(self, name):
        """
        Returns an object instance for the given `name`.
        """

        if not self.has_object(name):
            raise UnknownObject(name)

        object_module = import_module('.{}'.format(name), 'objects')
        object_class_name = '{}Object'.format(name.capitalize())
        object_class = getattr(object_module, object_class_name)

        return object_class()

    @classmethod
    def has_object(self, verb):
        try:
            imp.find_module(verb, ['objects'])
        except ImportError:
            return False
        else:
            return True

    def can_apply_action(self, action):
        """
        Returns whether you can apply the given `action` to the object.

        True means yes
        False means no
        None means unknown
        """
        return None
