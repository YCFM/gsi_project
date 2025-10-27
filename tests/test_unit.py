import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from module import Module
from unit import Unit

def test_unit_average():
    m1 = Module("M1", "Example 1", coef=2, credit=3, hours_tp=1.5)
    m1.set_grade(tp=10, exam=12)

    m2 = Module("M2", "Example 2", coef=1, credit=2, hours_tp=1.5)
    m2.set_grade(tp=8, exam=10)

    u = Unit("U1", "UE Test", [m1, m2])

    # Weighted average: (11.2*2 + 9.2*1) / (2+1) = 10.53
    assert round(u.calculate_average(), 2) == 10.53


def test_unit_credits():
    m1 = Module("M1", "Example 1", coef=2, credit=3, hours_tp=1.5)
    m1.set_grade(tp=10, exam=12)

    u = Unit("U1", "UE Test", [m1])

    # Average >= 10 → full credits
    assert u.calculate_credits() == 3
