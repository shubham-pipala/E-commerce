from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings

def encry(password):
    """
    Encrypts the provided password using Fernet encryption.
    """
    try:
        password = str(password)
        cipher_password = Fernet(settings.ENCRYPT_KEY)
        encrypted_password = cipher_password.encrypt(password.encode('UTF-8'))
        # Use base64 to ensure it's safe for URLs
        encrypted_password = base64.urlsafe_b64encode(encrypted_password)
        return encrypted_password.decode('UTF-8')
    except Exception as e:
        logging.getLogger("error_login").error(traceback.format_exc())
        return None

def descry(encrypted_password):
    """
    Decrypts the provided encrypted password using Fernet decryption.
    """
    try:
        # Decode base64 encoding
        encrypted_password = base64.urlsafe_b64decode(encrypted_password)
        cipher_password = Fernet(settings.ENCRYPT_KEY)
        decoded_password = cipher_password.decrypt(encrypted_password).decode('UTF-8')
        return decoded_password
    except Exception as e:
        logging.getLogger("error_login").error(traceback.format_exc())
        return None
