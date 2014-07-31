import re


def match_word(word, regex):

    def match_one_word(word, regex):
        if re.match(r'^{}$'.format(regex), word, re.I):
            return True
        else:
            return False

    if isinstance(regex, list) or isinstance(regex, tuple):
        for valid_match in regex:
            if match_one_word(word, valid_match):
                return True
    else:
        return match_one_word(word, regex)

    return False
