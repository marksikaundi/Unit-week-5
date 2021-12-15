# 1
def any_lowercase1(s):
    """Actually returns True whether _first_ letter is lowercase otherwise False

    Incorrect result: argument has three lowercase 'z' - expected True
    >>> any_lowercase1('Bzzz')
    False
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

# 2
def any_lowercase2(s):
    """Actually _always_ retuns _string_ "True"

    Incorrect result: argument has no lowercase letters - expected False
    >>> any_lowercase2('UEFA')
    'True'
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# 3
def any_lowercase3(s):
    """Actually returns True whether _last_ letter is lowercase otherwise False

    Incorrect result: argument has four lowercase 'd' - expected True
    >>> any_lowercase3('ddddD')
    False
    """
    for c in s:
        flag = c.islower()
    return flag

# 4
def any_lowercase4(s):
    """Actually returns True whether _any_ letter is lowercase otherwise False
        No incorrect results

    Argument has lowercase 'x' - expected True
    >>> any_lowercase4('Ux')
    True

    Argument nas no lowercase letters - expected False
    >>> any_lowercase4('BAR')
    False
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# 5
def any_lowercase5(s):
    """Actually returns True whether _all_ letters is lowercase otherwise False

    Incorrect result: all letters in argument except 'E' are lowercase - expected True
    >>> any_lowercase5('abcdEfg')
    False
    """
    for c in s:
        if not c.islower():
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)