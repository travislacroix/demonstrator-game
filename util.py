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
