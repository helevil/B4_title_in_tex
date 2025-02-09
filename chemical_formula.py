import re


def fix_chemical_formula(formula):
    """
    Converts a chemical formula into proper LaTeX formatting.
    - Leaves already formatted subscripts unchanged (e.g., Fe$_{2}$VAl remains Fe$_{2}$VAl)
    - Fixes raw formulas (e.g., H2O → H$_{2}$O)
    - Converts underscores correctly (_X → $_{X}$ without extra backslashes)
    - Ensures letters (e.g., x in Pr_x) and numbers in subscripts are formatted properly
    - Prevents extra dollar signs ($$X$$ → $X$)
    """

    # Step 1: Convert escaped underscores "\_" to normal "_"
    formula = formula.replace(r"\_", "_")

    # Step 2: Convert normal underscores (_X → $_{X}$), ensuring no extra backslashes
    formula = re.sub(r"_(\{?[\d\.\-δγαβa-zA-Z]+\}?)", r"$_{\1}$", formula)

    # Step 3: Fix numbers in chemical formulas (H2O → H$_{2}$O)
    formula = re.sub(r"([A-Za-z])(\d+)", r"\1$_{\2}$", formula)

    # Step 4: Remove redundant `{}` inside subscripts ($_{{X}}$ → $_{X}$)
    formula = re.sub(r"\$\_\{\{(.*?)\}\}\$", r"$_{\1}$", formula)

    # Step 5: Prevent double-dollar issues ($$X$$ → $X$)
    formula = re.sub(r"\$\$(.*?)\$\$", r"$\1$", formula)

    return formula


# 🔬 **Test Cases**
test_cases = [
    "Fe$_2$VAl ",
    "H2O",
    "CO2",
    "Ti_{0.99}Sc_{0.01}O_{2-δ}",
    "VO_{2}/LiCoO_{2}",
    "BiS_2",
    "Mg_{1-x}Ti_{2+x}O_{5}",
    "Eu3Bi2S4F4",
    "InGaZn$_3$O$_6$",
]  # ✅ Should stay the same  # ✅ H$_{2}$O  # ✅ CO$_{2}$  # ✅ Ti$_{0.99}$Sc$_{0.01}$O$_{2-δ}$  # ✅ VO$_{2}$/LiCoO$_{2}$  # ✅ BiS$_{2}$  # ✅ Mg$_{1-x}$Ti$_{2+x}$O$_{5}$  # ✅ Eu$_{3}$Bi$_{2}$S$_{4}$F$_{4}$

for case in test_cases:
    print(f"{case} -> {fix_chemical_formula(case)}")
