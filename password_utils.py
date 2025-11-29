from cryptography.fernet import Fernet

class Fakestr(str):
    def __str__(self):
        return "*****"
    def __repr__(self):
        return "******"



def load_key():
    return open("secret.key", "rb").read()



def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypt_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypt_password).decode()
    return Fakestr(decrypted)

def get_decrypted_password():
    encrypt_password =b'gAAAAABoybKsWYUgMyITTtw3jf6DiystTR0_LFwJqKRDDfHQS4esnirWdlPeIEyEbYgxFNt0MVU1Zt_SHY_tZ5kh-1keIdHHFw=='   #its coming from randomgenerated key+ our 'root'password mixed dhan idhu

    return decrypt_password(encrypt_password)



