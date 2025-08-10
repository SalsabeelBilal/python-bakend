import re

def is_strong_password(password):
    """Check if the password meets all strength requirements."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*]", password):
        return False, "Password must contain at least one special character (!@#$%^&*)."
    return True, None


def check_passwords(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            passwords = [line.strip() for line in infile if line.strip()]

        strong_passwords = []

        for pwd in passwords:
            valid, error = is_strong_password(pwd)
            if valid:
                strong_passwords.append(pwd)
            else:
                print(f"'{pwd}' is invalid: {error}")

        with open(output_file, "w", encoding="utf-8") as outfile:
            for pwd in strong_passwords:
                outfile.write(pwd + "\n")

        print(f"✅ Strong passwords saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write the files.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# File paths
input_file = "passwords.txt"
output_file = "strong_passwords.txt"

# Run the checker
check_passwords(input_file, output_file)
