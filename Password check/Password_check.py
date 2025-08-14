import string

def check_password(password: str):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1


    if any(ch.isupper() for ch in password):
        score += 1

    if any(ch.islower() for ch in password):
        score += 1

    if any(ch.isdigit() for ch in password):
        score += 1

    if any(ch in string.punctuation for ch in password):
        score += 1

    if score >= 6:
        strength = "Strong"
    elif 3 <= score < 6:
        strength = "Medium"
    else:
        strength = "Weak"

    return score, strength


if __name__ == "__main__":
    user_password = input("Enter the password: ")
    score, strength = check_password(user_password)
    print("Password score:", score)
    if strength == "Strong":
        print("✅ Strong password")
    elif strength == "Medium":
        print("⚠️ Medium password")
    else:
        print("❌ Weak password")
