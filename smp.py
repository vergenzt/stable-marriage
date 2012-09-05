#!/bin/python

def stableMarriage(boys, girls, verbose=False):
    """
    Run the stable marriage algorithm for the given set of preferences.

    Args:
      boys: a dict from boy names their preference lists (most preferred to least)
      girls: a dict from girl names to their preference lists (most preferred to least)
      verbose: when True, print information on each step

    Returns a set of tuples (boy, girl), each representing a couple in the
    resulting stable marriage.
    """
    if len(boys) != len(girls):
        raise ValueError()

    from collections import defaultdict
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

    stableMarriage(n, boys, girls, verbose=True)

