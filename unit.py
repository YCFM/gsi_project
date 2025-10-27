from module import Module
from AcademicElement import AcademicElement

class Unit(AcademicElement):
    """Represents a teaching unit containing multiple modules."""
    def __init__(self, name, title, modules=None):
        super().__init__(name, title)
        self._modules = modules if modules is not None else []

    def add_module(self, module):
        self._modules.append(module)

    def calculate_average(self):
        """Calculate weighted average of all modules in the Unit."""
        if not self._modules:
            return 0
        total = 0
        total_coef = 0
        for m in self._modules:
            total += m.calculate_average() * m.coef
            total_coef += m.coef
        return total / total_coef if total_coef else 0

    def calculate_credits(self):
        """Calculate the credits for the Unit."""
        avg = self.calculate_average()
        if avg >= 10:
            return sum(m.credit for m in self._modules)
        else:
            return sum(m.calculate_credits() for m in self._modules)


# Example usage (for demonstration)
if __name__ == "__main__":
    m1 = Module(
        "MTI",
        "Methods & Technologies of Implementation",
        coef=3,
        credit=5,
        hours_tp=1.5,
        continous_percent=40,
        exam_percent=60
    )

    m2 = Module(
        "AABD",
        "Database architecture and administration",
        coef=2,
        credit=4,
        hours_tp=1.5,
        continous_percent=40,
        exam_percent=60
    )

    u11 = Unit("UEM11", "UE Méthodologie", [m1, m2])
    m1.set_grade(tp=10, exam=12)
    m2.set_grade(tp=8, exam=6)

    print("Module average:", m2.name, m2.calculate_average())
    print
    print("Unit average:", u11.calculate_average())
    print("Unit credits:", u11.calculate_credits())
