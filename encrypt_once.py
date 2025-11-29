from password_utils import encrypt_password
from cryptography.fernet import Fernet   #cryptography library

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb")as f:
        f.write(key)
    print("key saved to secret.key")

if  __name__ == "__main__":
    #generate_key()

    encrypted = encrypt_password('root')
    print("encrypted password (copy this to password_utils.py)")
    print(encrypted)
