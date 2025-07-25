# mini project on BMI Calculator (Functions + Conditions)
def cm_to_m(cm): return cm / 100
def kg_to_g(kg): return kg * 1000

print("1. CM to M\n2. KG to G")
choice = int(input("Choose option: "))

if choice == 1:
    cm = float(input("Enter length in cm: "))
    print(f"Meter: {cm_to_m(cm)} m")
elif choice == 2:
    kg = float(input("Enter weight in kg: "))
    print(f"Gram: {kg_to_g(kg)} g")
else:
    print("Invalid choice.")
