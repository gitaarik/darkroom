from . import Object


class GroundObject(Object):

    def can_apply_action(self, action):

        if action == 'dig':
            return True
        else:
            return False
