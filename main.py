import string

password = input("Enter your password: ")

score = 0
missing = []

if len(password) >= 8:
    score += 1
else:
    missing.append("at least 8 characters")

if any(char.isupper() for char in password):
    score += 1
else:
    missing.append("an uppercase letter")

if any(char.islower() for char in password):
    score += 1
else:
    missing.append("a lowercase letter")

if any(char.isdigit() for char in password):
    score += 1
else:
    missing.append("a number")

if any(char in string.punctuation for char in password):
    score += 1
else:
    missing.append("a special symbol")

if score <= 2:
    strength = "Weak"
    quantum_risk = "High"
elif score <= 4:
    strength = "Medium"
    quantum_risk = "Moderate"
else:
    strength = "Strong"
    quantum_risk = "Low"

print("\nPassword Strength:", strength)
print("Quantum Risk:", quantum_risk)

if missing:
    print("To make your password stronger, add:")
    for item in missing:
        print("-", item)

if strength != "Strong":
    suggestion = password + "@2026"
    print("Suggested stronger password:", suggestion)