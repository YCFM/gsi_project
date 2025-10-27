from abc import abstractmethod

class AcademicElement:
    """Abstract base class for academic entities (Module, Unit, Semester, etc.)."""

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self._WEEKS = 15  # Encapsulation: private attribute
        self.coef = 0
        self.credit = 0

        # Workload distribution (volume horaire)
        self.hours_lecture = 0
        self.hours_td = 0
        self.hours_tp = 0

    @abstractmethod
    def calculate_average(self):
        """Example of aggregation — combining module averages."""
        if not self._modules:
            return 0

        total = sum(m.calculate_average() * m.coef for m in self._modules)
        coef_sum = sum(m.coef for m in self._modules)
        return total / coef_sum


    def calculate_credits(self):
        """Polymorphism: different modules could override this behavior."""
        if not self._modules:
            return 0

        avg = self.calculate_average()
        if avg >= 10:
            total_credits = sum(m.credit for m in self._modules)
        else:
            total_credits = sum(m.calculate_credits() for m in self._modules)

        return total_credits

