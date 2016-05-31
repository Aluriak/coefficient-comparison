"""Definition of all similarity coefficients

Functions should be defined as (set, set) -> float,
with return value in [0;1].

"""


def functions() -> iter:
    """Yield all functions of this module, excluding this one"""
    yield from (attr for name, attr in globals().items()
                if callable(attr) and name != 'functions')


def jaccard(a:set, b:set) -> float:
    return len(a & b) / (len(a | b))
