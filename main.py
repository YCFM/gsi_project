from module import Module
from unit import Unit
from semester import Semester

# ======================================================
#                  SEMESTER 1
# ======================================================

# ---- UE Fondamentales ----
F111 = Module("F111", "Réseaux des couches basses", coef=3, credit=6, hours_tp=1.5)
F112 = Module("F112", "Algorithmique Avancée et Complexité", coef=2, credit=4, hours_tp=1.5)

# ---- UE Fondamentales 2 ----
F121 = Module("F121", "Système d’exploitation", coef=2, credit=4, hours_tp=1.5)
F122 = Module("F122", "Architectures Modernes des Systèmes Informatiques", coef=2, credit=4, hours_tp=1.5)

# ---- UE Méthodologie ----
M111 = Module("M111", "Architecture et administration des bases de données", coef=2, credit=4, hours_tp=1.5)
M112 = Module("M112", "Méthodes et Technologies d’Implémentation", coef=3, credit=5, hours_tp=1.5)

# ---- UE Découverte ----
D111 = Module("D111", "Systèmes de Communication Vocaux et Vidéos", coef=2, credit=2, hours_tp=1.5)

# ---- UE Transversale ----
T111 = Module("T111", "Cloud Computing", coef=1, credit=1)

# ---- Units ----
UEF11 = Unit("UEF11", "UE Fondamentales 1", [F111, F112])
UEF12 = Unit("UEF12", "UE Fondamentales 2", [F121, F122])
UEM11 = Unit("UEM11", "UE Méthodologie", [M111, M112])
UED11 = Unit("UED11", "UE Découverte", [D111])
UET11 = Unit("UET11", "UE Transversale", [T111])

# ---- Semester 1 ----
S1 = Semester("S1", "Semestre 1", [UEF11, UEF12, UEM11, UED11, UET11])

# ---- Assign mock grades (for test) ----
for m in [F111, F112, F121, F122, M111, M112, D111, T111]:
    m.set_grade(tp=12, exam=14) 

# ======================================================
#                  SEMESTER 2
# ======================================================

F211 = Module("F211", "Middlewares pour systèmes répartis", coef=3, credit=6, hours_tp=1.5)
F212 = Module("F212", "Modélisation et Architectures logicielles", coef=2, credit=4, hours_tp=1.5)
F221 = Module("F221", "Réseaux de la couche IP", coef=3, credit=6, hours_tp=1.5)
F222 = Module("F222", "Introduction au Machine Learning", coef=2, credit=4, hours_tp=1.5)
M211 = Module("M211", "Infographie", coef=2, credit=3, hours_tp=1.5)
M212 = Module("M212", "Gestion de l’incertain", coef=2, credit=3, hours_tp=1.5)
D211 = Module("D211", "Internet of Things", coef=2, credit=3, hours_tp=1.5)
T211 = Module("T211", "Cybercriminalité", coef=1, credit=1)

UEF21 = Unit("UEF21", "UE Fondamentales 1", [F211, F212])
UEF22 = Unit("UEF22", "UE Fondamentales 2", [F221, F222])
UEM21 = Unit("UEM21", "UE Méthodologique", [M211, M212])
UED21 = Unit("UED21", "UE Découverte", [D211])
UET21 = Unit("UET21", "UE Transversale", [T211])

S2 = Semester("S2", "Semestre 2", [UEF21, UEF22, UEM21, UED21, UET21])

for m in [F211, F212, F221, F222, M211, M212, D211, T211]:
    m.set_grade(tp=13, exam=15)

# ======================================================
#              FINAL STUDENT RESULTS
# ======================================================

print("\n========== SEMESTRE 1 ==========")
print(f"Average: {S1.calculate_average():.2f}")
print(f"Credits: {S1.calculate_credits()}")

print("\n========== SEMESTRE 2 ==========")
print(f"Average: {S2.calculate_average():.2f}")
print(f"Credits: {S2.calculate_credits()}")

# ---- Overall Year (M1) ----
year_average = (S1.calculate_average() + S2.calculate_average()) / 2
year_credits = S1.calculate_credits() + S2.calculate_credits()

print("\n========== YEAR RESULTS ==========")
print(f"Year average: {year_average:.2f}")
print(f"Total credits: {year_credits}")
