from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Initialize Fernet cipher with the generated key
cipher = Fernet(key)

# Secret message to be encrypted
secret_message = b"This is a secret message."

# Encrypt the secret message
encrypted_message = cipher.encrypt(secret_message)

# Save the encrypted message to a file
with open("encrypted_file.txt", "wb") as file:
    file.write(encrypted_message)

# Send the encrypted file to the recipient

# Share the key with the recipient securely

# Recipient receives the encrypted file and the key

# Recipient decrypts the file using the key
with open("encrypted_file.txt", "rb") as file:
    encrypted_message = file.read()

decrypted_message = cipher.decrypt(encrypted_message)

# Print the decrypted message
print("Decrypted message:", decrypted_message.decode('utf-8'))
