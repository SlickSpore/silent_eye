from cryptography.fernet import Fernet
import common.config
import base64

def generate_key():
    print("->", Fernet.generate_key())

f = Fernet(common.config.SERVER_PROPERTIES["SECURE_KEY"])

def encrypt_message(msg: str) -> bytes:
    return f.encrypt(msg.encode())

def decrypt_message(token: bytes) -> str:
    return f.decrypt(token).decode()