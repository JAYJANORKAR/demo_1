from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Step 1: Generate a random 8-byte DES key (56 bits are used for encryption)
key = get_random_bytes(8)

# Step 2: Get the message from the user
message = input("Enter your message to encrypt: ")

# Step 3: Pad the message to make it a multiple of 8 bytes (DES block size)
padded_message = pad(message.encode(), DES.block_size)

# Step 4: Create a cipher object using CBC mode (you need an IV for CBC)
cipher = DES.new(key, DES.MODE_CBC)

# Step 5: Encrypt the padded message
encrypted_message = cipher.encrypt(padded_message)

# Step 6: Decrypt the encrypted message using the same key and IV
decipher = DES.new(key, DES.MODE_CBC, iv=cipher.iv)
decrypted_message = unpad(decipher.decrypt(encrypted_message), DES.block_size)

# Output the results
print("\n--- Results ---")
print("Original Message: ", message)
print("Encrypted Message (Hex): ", encrypted_message.hex())
print("Decrypted Message: ", decrypted_message.decode())
