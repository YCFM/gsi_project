from AcademicElement import AcademicElement
from unit import Unit

class Semester(AcademicElement):
    """Represents an academic semester composed of multiple Units."""

    def __init__(self, name, title, units=None):
        super().__init__(name, title)
        self._units = units if units is not None else []

    def add_unit(self, unit):
        """Add a Unit object to this Semester."""
        self._units.append(unit)

    def calculate_average(self):
        """Compute the weighted average of all units in the semester."""
        if not self._units:
            return 0
        total = 0
        total_coef = 0
        for u in self._units:
            coef = getattr(u, "coef", 1)
            if coef == 0:
                coef = 1
            total += u.calculate_average() * coef
            total_coef += coef
        return total / total_coef if total_coef else 0

    def calculate_credits(self):
        """Sum the credits of all validated units."""
        return sum(u.calculate_credits() for u in self._units)
