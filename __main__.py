import random
import coefficients
from collections import defaultdict


SET_SIZE = 100
DATA_RANGE = range(0, 1001)
SET_A = frozenset(random.sample(DATA_RANGE, SET_SIZE))
NOT_SET_A = set(DATA_RANGE) - SET_A


def compute_data(coefs:iter, seta:set, b_cases:iter) -> dict:
    ret = defaultdict(dict)
    for casename, setb in b_cases:
        for coef in coefs:
            ret[casename][coef] = coef(seta, setb)
    return ret


if __name__ == "__main__":
    coefs = tuple(attr for name, attr in globals().items()
                  if callable(attr) and name.startswith('coef_'))

    b_cases = (
        ('included', frozenset(random.sample(NOT_SET_A, SET_SIZE))),
        ('half', frozenset(set(random.sample(SET_A, SET_SIZE // 2)) | set(random.sample(NOT_SET_A, SET_SIZE // 2)))),
    )
    for inc_percent in range(0, 101, 10):
        yield str(inc_percent)

    print(compute_data(coefficients.functions(), SET_A, b_cases))
