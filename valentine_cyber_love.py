"""
valentine_cyber_love.py

This script allows you to encrypt and decrypt love messages using the Caesar Cipher.
It's a fun and romantic way to keep your love notes secure and special. ❤️🔒

Things to Try:
1. **Encryption and Decryption**: Encrypt a special love message and decrypt it to see the original.
2. **Experiment with Shifts**: Try different shift values and see how the encrypted message changes.
3. **Customize the Algorithm**: Modify the script to use a different cipher algorithm like the Vigenère cipher.

Contributions:
1. **Add New Cipher Algorithms**: Introduce additional encryption methods for more variety.
2. **Create a GUI**: Develop a user-friendly interface for the script using a library like Tkinter.
3. **Additional Features**: Implement key management, secure password storage, or even email encryption.
4. **Improve Documentation**: Add detailed explanations, comments, and examples to make the code more understandable.
5. **Code Optimization**: Refactor the code to make it more efficient and readable.

Example usage:
    message = "Happy Valentine's Day, my love!"
    shift = 3

    encrypted_message = encrypt(message, shift)
    print(f"Encrypted: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted: {decrypted_message}")

To run the script:
    Enter your love message and the shift value when prompted.

Happy Valentine's Day! 💖
"""

def encrypt(text, shift):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage
message = "Happy Valentine's Day, my love!"
shift = 3

encrypted_message = encrypt(message, shift)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted: {decrypted_message}")

if __name__ == "__main__":
    message = input("Enter your love message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = encrypt(message, shift)
    print(f"Encrypted: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted: {decrypted_message}")
