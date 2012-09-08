#!/bin/python

class Person:
    """
    Implements a boy or a girl for the stable marriage problem.
    """

    def __init__(self, name, name_prefs = None):
        self.name = name
        self.name_prefs = name_prefs  # preferences by name
        self.prefs = None             # preferences by Person objects
        self._prefs = None
        self.proposals = set()
        self.choice = None

    def preference(self, other):
        """
        Returns a preference ranking for other, where a higher number means
        other is more preferred.  In other words, this should work as expected:

        >>> girl = max(girls, key=boy.preference)
        """
        return -1 * self._prefs.index(other)

    def proposeTo(self, other):
        """
        Propose marriage to other Person.  Adds self to other's set of proposals.
        """
        other.proposals.add(self)

    def reject(self, other):
        """
        Reject a proposal from other Person.  Removes other from self's set of
        proposals, and removes self from other's preference list.
        """
        self.proposals.remove(other)
        other._prefs.remove(self)

    def choose(self, other):
        """
        Say 'maybe' to other Person.  Removes other from self's set of proposals,
        but does not remove self from other's preference list.
        """
        self.proposals.remove(other)
        self.choice = other

    def __str__(self):
        return self.name
    def __repr__(self):
        return repr(self.name)

    @staticmethod
    def getPersonSets(boys, girls):
        """
        Get a set of Person objects from a dictionary of their preferences.

        Args:
            boys: a dictionary from the boys's name to his preference list
            girls: a dictionary from the girl's name to her preference list

        Preference lists should be lists of names (must equal the keys in the
        other dictionary) in descending order of preference.

        Returns a tuple (boys, girls), where each item is a set of Person objects.
        """
        from itertools import chain

        # construct a name table
        names = dict()
        for name, prefs in chain(boys.items(), girls.items()):
            names[name] = Person(name, prefs)

        # link up the preferences for each Person
        for _, person in names.items():
            person.prefs = [names[name] for name in person.name_prefs]
            person._prefs = person.prefs.copy()

        boys = set(names[name] for name in boys)
        girls = set(names[name] for name in girls)

        return (boys, girls)


def stableMarriage(boys, girls, verbose=False):
    """
    Run the stable marriage algorithm for the given set of preferences.

    Args:
      boys: a set of Person objects
      girls: a set of Person objects
      verbose: when True, print information on each step

    Returns a set of tuples (boy, girl), each representing a couple in the
    resulting stable marriage.
    """
    if len(boys) != len(girls):
        raise ValueError()

    day = 0

    while any(girl.choice == None for girl in girls):
        day += 1

        # morning
        for boy in boys:
            best = boy.prefs[0]
            boy.proposeTo(best)

        # afternoon and evening
        for girl in girls:
            if len(girl.proposals) != 0:
                best = max(girl.proposals, key=girl.preference)
                girl.choose(best)
                map(girl.reject, girl.proposals.copy())

    marriage = set((girl.choice,girl) for girl in girls)

    if verbose:
        print
        print "Stable marriage:", marriage
        print "Solution found in", day, "days"

    return marriage


def randomPreferences(n):
    """
    Gets a random ordering of preferences for each boy and girl in an instance
    of the stable marriage problem for given n.

    Due to the naming of the girls, n must be <= 26.
    """
    if n > 26: raise ValueError()

    import string
    import random

    b, g = {}, {}
    bnames = [i+1 for i in range(n)]     # use numbers for the boys
    gnames = list(string.lowercase[:n])  # use letters for the girls

    for boy in bnames:
        random.shuffle(gnames)
        b[boy] = gnames[:]
    for girl in gnames:
        random.shuffle(bnames)
        g[girl] = bnames[:]

    return b,g

if __name__=='__main__':

    n = 4
    a,b,c,d = 'abcd'
    boys = {
        1: [c, d, b, a],
        2: [d, a, c, b],
        3: [d, c, b, a],
        4: [c, d, b, a],
    }
    girls = {
        a: [2, 3, 4, 1],
        b: [3, 4, 1, 2],
        c: [2, 3, 1, 4],
        d: [4, 1, 2, 3],
    }

    boys, girls = Person.getPersonSets(boys, girls)

    stableMarriage(boys, girls, verbose=True)

