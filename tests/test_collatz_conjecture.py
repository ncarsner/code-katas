from abstract_use_cases.collatz_conjecture import CollatzChecker, collatz_next


def _checker(n: int) -> CollatzChecker:
    checker = CollatzChecker()
    checker.ensure_up_to(n)
    return checker


# --- collatz_next ---

def test_collatz_next_even():
    assert collatz_next(8) == 4


def test_collatz_next_odd():
    assert collatz_next(3) == 10


def test_collatz_next_one():
    assert collatz_next(1) == 4   # 3*1+1; progression stops because 1 is pre-resolved


# --- step counts for small integers ---

def test_steps_for_1():
    checker = _checker(1)
    assert checker.steps_for[1] == 0


def test_steps_for_2():
    # 2 -> 1  (1 step)
    checker = _checker(2)
    assert checker.steps_for[2] == 1


def test_steps_for_3():
    # 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (7 steps)
    checker = _checker(3)
    assert checker.steps_for[3] == 7


def test_steps_for_4():
    # 4 -> 2 -> 1  (2 steps); 4 is resolved early during start=3 traversal
    checker = _checker(4)
    assert checker.steps_for[4] == 2


def test_steps_for_6():
    # 6 -> 3 -> … -> 1  (8 steps)
    checker = _checker(6)
    assert checker.steps_for[6] == 8


def test_steps_for_7():
    # 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 ->
    # 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (16 steps)
    checker = _checker(7)
    assert checker.steps_for[7] == 16


def test_steps_for_9():
    # 9 -> 28 -> 14 -> 7 -> … -> 1  (19 steps)
    checker = _checker(9)
    assert checker.steps_for[9] == 19


# --- all integers 1..n are resolved ---

def test_all_resolved_up_to_10():
    checker = _checker(10)
    for k in range(1, 11):
        assert checker.proven(k), f"{k} should be resolved"


def test_max_valid():
    checker = _checker(20)
    assert checker.max_valid == 20


# --- precomputed values are reused (early-termination correctness) ---

def test_precomputed_steps_reused():
    """Numbers resolved as side-effects of earlier starts must have correct step counts."""
    checker = _checker(20)
    expected = {
        1: 0, 2: 1, 3: 7, 4: 2, 5: 5, 6: 8, 7: 16,
        8: 3, 9: 19, 10: 6, 11: 14, 12: 9, 13: 9,
        14: 17, 15: 17, 16: 4, 17: 12, 18: 20, 19: 20, 20: 7,
    }
    for k, expected_steps in expected.items():
        assert checker.steps_for[k] == expected_steps, (
            f"steps_for[{k}]: expected {expected_steps}, got {checker.steps_for[k]}"
        )


# --- histogram reflects correct step counts ---

def test_histogram_step_zero_only_for_1():
    """Only integer 1 should have 0 steps."""
    checker = _checker(10)
    assert checker.steps_histogram.get(0, 0) == 1
