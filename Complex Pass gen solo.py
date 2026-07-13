import random
import string
import tkinter as tk

#this allows us to copy the text to the system clipboard
root = tk.Tk()
root.withdraw()

def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()  # now it stays on the clipboard after the window is closed
    
def generate_password(length, use_lower, use_upper, use_numbers, use_special):
    character_pool = ""
    password = []
    
    #ensure that at least one character from each selected catagory is selected
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
        character_pool += string.ascii_lowercase
        
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
        character_pool += string.ascii_uppercase
        
    if use_numbers:
        password.append(random.choice(string.digits))
        character_pool += string.digits
        
    if use_special:
        special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
        password.append(random.choice(special_chars))
        character_pool += special_chars
        
    while len(password) < length:
     password.append(random.choice(character_pool))
        
    for _ in range (random.randint(3 , 5)):
        random.shuffle(password)
    return "".join(password)


while True:
    # Password length
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("\nERROR: Password won't be strong enough. Minimum length is 8 characters.\n")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    print("\nInclude the following character types? (y/n)")

    lower = input("Lowercase letters: ").strip().lower() in ("y", "yes")
    upper = input("Uppercase letters: ").strip().lower() in ("y", "yes")
    numbers = input("Numbers: ").strip().lower() in ("y", "yes")
    special = input("Special characters: ").strip().lower() in ("y", "yes")

    # Require at least one option
    if not (lower or upper or numbers or special):
        print("\nERROR: Password won't be strong enough. Select at least one character type.\n")
        continue

    while True:
        password = generate_password(length, lower, upper, numbers, special)

        print("\nGenerated Password:")
        print(password)

        regenerate = input("\nWould you like a new password generated? (y/n): ").strip().lower()

        if regenerate in ("y", "yes"):
            continue

        accept = input("Is this password okay? (y/n): ").strip().lower()

        if accept in ("y", "yes"):
            copy_to_clipboard(password)
            print("\nPassword copied to clipboard.")
            input("Clipboard updated. Press Enter to exit...")
        break
    break