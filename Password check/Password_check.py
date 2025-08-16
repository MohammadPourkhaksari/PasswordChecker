import string

# لیست پسوردهای رایج
COMMON_PASSWORDS = {
    "123456", "123456789", "qwerty", "password", "111111",
    "123123", "abc123", "12345678", "iloveyou", "000000"
}

def is_sequential(password: str) -> bool:
    """بررسی پشت سر هم بودن کاراکترها (اعداد یا حروف)"""
    seqs = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789"]
    for seq in seqs:
        if password in seq:
            return True
        for i in range(len(seq) - 3):
            if password in seq[i:i+len(password)]:
                return True
    return False

def is_repeated(password: str) -> bool:
    """بررسی تکراری بودن کاراکترها یا الگوهای ساده"""
    if len(set(password)) < len(password) // 2:
        return True
    for i in range(1, len(password)//2 + 1):
        if password == password[:i] * (len(password)//i):
            return True
    return False

def format_time(seconds: float) -> str:
    """تبدیل ثانیه به واحد خوانا"""
    units = [
        ("seconds", 60),
        ("minutes", 60),
        ("hours", 24),
        ("days", 365),
        ("years", 100),
        ("centuries", 100)
    ]
    result = seconds
    for unit, step in units:
        if result < step:
            return f"{result:.2f} {unit}"
        result /= step
    return f"{result:.2f} centuries"

def brute_force_time(password: str, guesses_per_second=1e9) -> str:
    """محاسبه زمان تقریبی brute-force آفلاین"""
    charset_size = 0
    if any(ch.islower() for ch in password): charset_size += 26
    if any(ch.isupper() for ch in password): charset_size += 26
    if any(ch.isdigit() for ch in password): charset_size += 10
    if any(ch in string.punctuation for ch in password): charset_size += len(string.punctuation)
    if any('\u0600' <= ch <= '\u06FF' for ch in password): charset_size += 32  # حروف فارسی تقریبی

    combinations = charset_size ** len(password)
    seconds = combinations / guesses_per_second
    return format_time(seconds)

def estimate_crack_time(password: str) -> str:
    """تخمین ساده سطح زمان کرک شدن"""
    charset_size = 0
    if any(ch.islower() for ch in password): charset_size += 26
    if any(ch.isupper() for ch in password): charset_size += 26
    if any(ch.isdigit() for ch in password): charset_size += 10
    if any(ch in string.punctuation for ch in password): charset_size += len(string.punctuation)
    if any('\u0600' <= ch <= '\u06FF' for ch in password): charset_size += 32

    combinations = charset_size ** len(password)

    if combinations < 10**6:
        return "Instantly (<1 second)"
    elif combinations < 10**9:
        return "Few minutes"
    elif combinations < 10**12:
        return "Few hours"
    elif combinations < 10**15:
        return "Few days"
    elif combinations < 10**18:
        return "Few years"
    else:
        return "Centuries (very strong)"

def check_password(password: str):
    score = 0
    feedback = []

    # --- بررسی طول ---
    score += min(len(password) // 4, 3)

    # --- بررسی دسته‌های مختلف ---
    categories = 0
    if any(ch.isupper() for ch in password):
        categories += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    if any(ch.islower() for ch in password):
        categories += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    if any(ch.isdigit() for ch in password):
        categories += 1
    else:
        feedback.append("Add at least one digit.")
    if any(ch in string.punctuation for ch in password):
        categories += 1
    else:
        feedback.append("Add at least one special character (!, @, #, etc).")
    if " " in password:
        categories += 1
    if any('\u0600' <= ch <= '\u06FF' for ch in password):
        categories += 1

    score += categories

    # --- قوانین اضافی ---
    if password in COMMON_PASSWORDS:
        return 0, "Weak", ["Password is too common! Choose something unique."], "Instantly (<1 second)", "Instantly (<1 second)"
    if is_sequential(password):
        return 0, "Weak", ["Avoid sequential characters like 123456 or abcdef."], "Instantly (<1 second)", "Instantly (<1 second)"
    if is_repeated(password):
        return 0, "Weak", ["Avoid repeated patterns like aaaaaa or ababab."], "Instantly (<1 second)", "Instantly (<1 second)"
    if categories < 2:
        return 1, "Weak", ["Use more character types (letters, numbers, symbols)."], "Instantly (<1 second)", "Instantly (<1 second)"

    # --- تعیین قدرت ---
    if score >= 7:
        strength = "Strong"
    elif 4 <= score < 7:
        strength = "Medium"
    else:
        strength = "Weak"

    crack_time = estimate_crack_time(password)
    brute_time = brute_force_time(password)

    return score, strength, feedback, crack_time, brute_time


# تست مستقیم
if __name__ == "__main__":
    user_password = input("Enter the password: ")
    score, strength, feedback, crack_time, brute_time = check_password(user_password)

    print(f"\nPassword score: {score}")
    print(f"Strength: {strength}")
    print(f"Estimated crack time (simple): {crack_time}")
    print(f"Brute-force attack time (@1B guesses/sec): {brute_time}")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print("-", tip)
