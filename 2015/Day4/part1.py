import hashlib


secret_key = "iwrupvqb"

number = 1
while True:
    # Create the string to hash
    input_string = secret_key + str(number)

    # Compute the MD5 hash
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()

    # Check if the hash starts with five zeroes
    if md5_hash.startswith("00000"):
        break

    # Increment the number and try again
    number += 1

print(f"The lowest positive number for the secret key '{secret_key}' is: {number}")
