import bcrypt
import base64
import hashlib

def calculateHash(password: bytes, salt: bytes) -> str:
    '''
    Returns the hash of the password
    '''
    return bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(password).digest()),
        salt
    )
