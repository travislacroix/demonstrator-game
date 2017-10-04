import numpy as np
import random

# NOTE: Some of this is used for a different implementation of the game, and so some code is redundant.

def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w > r:
            return c
        upto += w
    assert False, "Shouldn't get here"


def normalize(vec):
    # a hack for the FuncGame case
    return vec if np.sum(vec) == 0.0 else vec / np.sum(vec)


def matNormalize(mat):
    row_sums = mat.sum(axis=1)
    return mat / row_sums[:, np.newaxis]


def swap(xs, a, b):
    xs[a], xs[b] = xs[b], xs[a]


# A Derangement is a permutation with no fixed points
# http://en.wikipedia.org/wiki/Derangement
# http://stackoverflow.com/questions/25200220/generate-a-random-derangement-of-a-list

def derange(xs):
    for a in xrange(1, len(xs)):
        b = random.choice(xrange(0, a))
        swap(xs, a, b)
    return xs
