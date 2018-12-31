import random


def roll():
    """Roll two pigs from a set of weighted probabilities and return the pigs
    as a list of two strings.

    A set of 3939 rolls found at http://passpigs.tripod.com/prob.html gives the
    weights as (34, 32, 20, 9, 4, 1). A better analyzed set of weights from
    11,954 rolls at http://jse.amstat.org/v14n3/datasets.kern.html gives the
    weights used here.
    """
    population = ('pink', 'dot', 'razorback', 'trotter', 'snouter', 'jowler')
    weights = (34.9, 30.2, 22.4, 8.8, 3.0, 0.61)
    pigs = random.choices(population, weights, k=2)
    return pigs


def is_bust(pigs):
    """Return whether a combination of two pigs is a bust."""
    if ((pigs[0] == 'pink' and pigs[1] == 'dot')
            or (pigs[0] == 'dot' and pigs[1] == 'pink')):
        return True
    return False


def calculate(pigs):
    """Return the integer value of a non-bust roll of two pigs."""
    assert not is_bust(pigs)
    singles = {'pink': 0,
               'dot': 0,
               'razorback': 5,
               'trotter': 5,
               'snouter': 10,
               'jowler': 15}
    matches = {'pink': 1,
               'dot': 1,
               'razorback': 20,
               'trotter': 20,
               'snouter': 40,
               'jowler': 60}
    if pigs[0] == pigs[1]:
        return matches[pigs[0]]
    return singles[pigs[0]] + singles[pigs[1]]
