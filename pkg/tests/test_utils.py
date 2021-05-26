from pkg.utils import plus, minus

def test_calc():
    assert plus(1, 2) == 3
    assert plus(3, 4) == 7
    assert minus(1, 2) == -1
    assert minus(2, 1) == 1
