# Python for Chemists
# First project: Molar mass calculator

atomic_masses = {
    "H": 1.008,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999
}

def calculate_molar_mass(formula_counts):
    total = 0

    for element, count in formula_counts.items():
        if element not in atomic_masses:
            raise ValueError(f"Unknown element: {element}")

        total += atomic_masses[element] * count

    return total


# Example: water, H2O
water = {"H": 2, "O": 1}

print("Molar mass of H2O:",
      calculate_molar_mass(water), "g/mol")
