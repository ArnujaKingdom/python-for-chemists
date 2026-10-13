
# Python for Chemists
# Project 1: Molar Mass Calculator

atomic_masses = {
    "H": 1.008,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "Na": 22.990,
    "Cl": 35.45,
    "S": 32.06,
    "Ca": 40.078,
    "Mg": 24.305,
    "K": 39.098
}


def calculate_molar_mass(formula_counts):
    total = 0

    for element, count in formula_counts.items():
        if element not in atomic_masses:
            raise ValueError(f"Unknown element: {element}")

        if not isinstance(count, int) or count < 0:
            raise ValueError("Counts must be non-negative integers.")

        total += atomic_masses[element] * count

    return total


# Test molecules
molecules = {
    "Water (H2O)": {"H": 2, "O": 1},
    "Carbon dioxide (CO2)": {"C": 1, "O": 2},
    "Sodium chloride (NaCl)": {"Na": 1, "Cl": 1},
    "Calcium carbonate (CaCO3)": {"Ca": 1, "C": 1, "O": 3}
}

for name, formula in molecules.items():
    mass = calculate_molar_mass(formula)
    print(f"{name}: {mass:.3f} g/mol")
