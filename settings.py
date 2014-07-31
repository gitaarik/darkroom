# Valid verbs
# key: the verb
# value: a dict with the following keys:
#
# synonyms:
#    a list of synonyms
#
# required_items:
#    a list of lists of items that are required. The deeper level list
#    is a list of items that are ALL required for this action, and the
#    higher level list acts as an OR statement.
#
#    So for example, if the value is:
#    [
#        ['matches', 'matchbox'],
#        ['

VERBS = {
    'say': {
        'synonyms': [],
        'required_items': []
    },
    'hit': {
        'synonyms': ['slam', 'punch'],
        'required_items': []
    },
    'look': {
        'synonyms': [],
        'required_items': []
    },
    'dig': {
        'synonyms': [],
        'required_items': [['shovel']]
    }
}
