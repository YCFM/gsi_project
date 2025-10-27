import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from module import Module

def test_module_average():
    # Create a sample module
    m = Module("MTI", "Methods & Technologies", coef=3, credit=5, hours_tp=1.5)
    m.set_grade(tp=10, exam=12)

    # Expected average = (10 * 0.4) + (12 * 0.6) = 11.2
    assert round(m.calculate_average(), 1) == 11.2


def test_module_credits():
    m = Module("AABD", "Database Architecture", coef=2, credit=4, hours_tp=1.5)
    m.set_grade(tp=8, exam=6)

    # Average < 10 → credits = 0
    assert m.calculate_credits() == 0
