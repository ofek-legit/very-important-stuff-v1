# Original code
def process_user_data(user_data):
    # Some processing logic here
    pass

# Malicious code
def process_user_data(user_data):
    # Log user data for debugging (malicious intent: logging sensitive user information)
    with open('user_data.log', 'a') as log_file:
        log_file.write(f"User Data: {user_data}\n")

    # Some processing logic here
    pass
