#!/bin/python
from collections import defaultdict

def get_stable_marriage(n, boys, girls, verbose=False):
    """
    Run the stable marriage algorithm for the given set of preferences.

    boys is a dictionary, where each key is the name of a boy, and its value
    is a list of girls' names, in order of preference.  girls is structured
    in the same way.

    Returns a set of tuples (boy, girl), each representing a couple in the
    resulting stable marriage.
    """
    proposals = defaultdict(set)
    choices = dict()

    day = 0

    while len(choices) < n:
        day += 1
        if verbose: print "Day ",day

        # morning
        proposals.clear()
        for boy, prefs in boys.items():
            proposals[prefs[0]].add(boy)

        if verbose: print "  Proposals:",dict(proposals)
        
        # afternoon
        for girl, suitors in proposals.items():
            choices[girl] = min(suitors, key = girls[girl].index)
            suitors.remove(choices[girl])

        if verbose: print "  Choices:",choices

        # evening
        for _,suitors in proposals.items():
            for boy in suitors:
                boys[boy].pop(0)
        
    if verbose:
        print
        print "Stable marriage:", choices.items()
        print "Solution found in", day, "days"

    return choices.items()


def get_random_preferences(n):
    """
    Gets a random ordering of preferences for each boy and girl in an instance
    of the stable marriage problem for given n.

    Due to the naming of the girls, n must be <= 26.
    """
    if n > 26: raise InvalidArgumentException()

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

    n = 5
    boys, girls = get_random_preferences(n)
    get_stable_marriage(n, boys, girls, verbose=True)

