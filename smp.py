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


if __name__=='__main__':

    # assign letter variables for the girls
    a,b,c,d,e,f = 'abcdef'

    boys = {
      1: [a,b,c,d,e,f],
      2: [b,c,d,e,a,f],
      3: [c,d,e,a,b,f],
      4: [d,e,a,b,c,f],
      5: [e,a,b,c,d,f],
      6: [a,b,c,d,e,f],
    }
    girls = {
      a: [2,1,6,5,4,3],
      b: [3,2,1,6,5,4],
      c: [4,3,2,1,5,6],
      d: [5,4,3,2,1,6],
      e: [6,5,4,3,2,1],
      f: [1,2,3,4,5,6],
    }

    get_stable_marriage(6, boys, girls, verbose=True)

