import random
import coefficients
from collections import defaultdict


SET_SIZE = 10
DATA_RANGE = range(0, SET_SIZE * 10 + 1)
SET_A = frozenset(random.sample(DATA_RANGE, SET_SIZE))
NOT_SET_A = set(DATA_RANGE) - SET_A
DEBUG_PRINT = False


def compute_data(coefs:iter, seta:set, b_cases:iter) -> dict:
    ret = defaultdict(dict)
    if DEBUG_PRINT:
        print(seta)
    for inc_ratio, setb in b_cases:
        if DEBUG_PRINT:
            print(inc_ratio, setb, sum(1 for e in setb if e in seta))
        for coef in coefs:
            ret[coef][inc_ratio] = coef(seta, setb)
    return ret


def gen_set_b() -> iter:
    """Yield pairs (ratio of included in SET_A, elements), where elements are
    choosen in DATA_RANGE, and ratio*100 percent of these elements
    are present in SET_A.
    """
    for inc_percent in range(0, 101, 10):
        inc_ratio = inc_percent / 100.
        set_b = frozenset(
            set(random.sample(SET_A, int(SET_SIZE * inc_ratio))) |
            set(random.sample(NOT_SET_A, int(SET_SIZE * (1. - inc_ratio))))
        )
        yield str(inc_ratio), set_b


if __name__ == "__main__":
    coefs = tuple(attr for name, attr in globals().items()
                  if callable(attr) and name.startswith('coef_'))

    print(compute_data(coefficients.functions(), SET_A, gen_set_b()))
