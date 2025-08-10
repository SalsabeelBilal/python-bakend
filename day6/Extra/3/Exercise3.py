
class InvalidLengthError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass


def register_user(output_file):
    try:
        username = input("Enter a username: ").strip()

    
        if len(username) < 5 or len(username) > 15:
            raise InvalidLengthError("Username must be between 5 and 15 characters.")

     
        if not username.isalnum():
            raise InvalidCharacterError("Username must contain only letters and numbers.")

        with open(output_file, "a", encoding="utf-8") as file:
            file.write(username + "\n")

        print("Registration successful!")

    except InvalidLengthError as e:
        print(f"Registration failed: {e}")
    except InvalidCharacterError as e:
        print(f"Registration failed: {e}")
    except PermissionError:
        print("Error: You don't have permission to write to the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Registration attempt completed.")



output_file = "users.txt"


register_user(output_file)
