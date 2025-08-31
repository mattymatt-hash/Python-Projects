# Assign the string to a variable
favorite = "Ryan Reynolds in Dead pool"

# 1. capitalize() – Capitalizes the first character, rest lowercase
print(favorite.capitalize())  # Output: "Ryan reynolds in dead pool"

# 2. find() – Finds the position of a substring
print(favorite.find("Dead"))  # Output: 19

# 3. index() – Same as find, but raises error if not found
print(favorite.index("Reynolds"))  # Output: 5

# 4. isalnum() – Checks if all characters are alphanumeric (no spaces/punctuation)
print(favorite.isalnum())  # Output: False (contains spaces)

# 5. isalpha() – Checks if all characters are alphabetic (no spaces/numbers)
print(favorite.isalpha())  # Output: False (contains spaces)

# 6. isdigit() – Checks if all characters are digits
print(favorite.isdigit())  # Output: False

# 7. islower() – Checks if all alphabetic characters are lowercase
print(favorite.islower())  # Output: False

# 8. isupper() – Checks if all alphabetic characters are uppercase
print(favorite.isupper())  # Output: False

# 9. isspace() – Checks if the string contains only whitespace
print(favorite.isspace())  # Output: False

# 10. startswith() – Checks if string starts with a specific substring
print(favorite.startswith("Ryan"))  # Output: True

