import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from module import Module
from unit import Unit
from semester import Semester

def test_semester_average_and_credits():
    m1 = Module("M1", "Module 1", coef=2, credit=3, hours_tp=1.5)
    m1.set_grade(tp=10, exam=12)

    m2 = Module("M2", "Module 2", coef=1, credit=2, hours_tp=1.5)
    m2.set_grade(tp=8, exam=6)

    u1 = Unit("U1", "UE 1", [m1, m2])
    s1 = Semester("S1", "Semestre 1", [u1])

    # Check semester calculations
    assert round(s1.calculate_average(), 1) == round(u1.calculate_average(), 1)
    assert s1.calculate_credits() == u1.calculate_credits()
