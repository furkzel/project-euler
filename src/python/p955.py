import math
import sympy as sp


def T(n: int) -> int:
    return n * (n + 1) // 2


def is_tri(x: int) -> bool:
    d = 1 + 8 * x
    s = int(math.isqrt(d))
    return s * s == d


def minimal_m_for_j(j: int):
    """
    Let be a minimum m>0: T_j + T_m triangular,
    Factor approach: (w-v)(w+v) = 4 j (j+1),
    x=(w-v)/2, y=(w+v)/2, xy = j(j+1), v = y-x = 2m+1 odd.
    """
    N = j * (j + 1)

    # pgcd(j, j+1)=1 in this way, divisors of N come from the pairs d|j and e|(j+1): y = d*e, x = N // y.
    dj = sp.divisors(j)
    dp = sp.divisors(j + 1)

    best_v = None

    for d in dj:
        for e in dp:
            y = d * e
            x = N // y
            v = y - x
            # Should be v > 1 and odd: plus, x,y must be of opposite parity (that is, v odd is enough).
            if v > 1 and (v % 2 == 1):
                if best_v is None or v < best_v:
                    best_v = v

    if best_v is None:
        raise RuntimeError("(x,y) not found for j={}".format(j))

    m = (best_v - 1) // 2

    # If we want to return also j' (the index of the next triangular number seen):
    Tr = T(j) + T(m)
    r = (int(math.isqrt(1 + 8 * Tr)) - 1) // 2
    assert is_tri(Tr) and T(r) == Tr
    return m, r


def index_of_kth_triangular(k: int) -> int:
    """
    n_k is the index such that a_{k} = T_{n_k} is the k-th triangular number
    which can be written as a sum of two triangular numbers.
    Initial condition: a_0 = T_2, cad k=1 -> n_1 = 0.
    """
    if k < 1:
        raise ValueError("It should be k >= 1")
    n = 0  # n_1 = 0
    j = 2  # T_2 = 3
    for _ in range(1, k):  # It not enter to the loop if k=1.
        m, j_next = minimal_m_for_j(j)
        n += m
        j = j_next
    return n


assert index_of_kth_triangular(10) == 2964
print(index_of_kth_triangular(70))
