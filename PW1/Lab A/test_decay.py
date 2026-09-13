"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


# TODO 2: test_matches_law
def test_matches_law():
    N0 = 1000
    lam = 0.4
    seeds = range(100)
    results = [simulate(N0, lam, seed=s) for s in seeds]
    mean_results = np.mean(results, axis=0)

    dt = 0.05
    t = np.arange(len(mean_results)) * dt
    expected = N0 * np.exp(-lam * t)

    assert mean_results == pytest.approx(expected, rel=0.05)