import bcrypt
import base64
import hashlib

def calculateHash(password: bytes, salt: bytes = b"") -> str:
    """Returns the hash of the password.

    Args:
        password (bytes): Raw Password. *(in bytes)*
        salt (bytes, optional): Salt of the password. Defaults to b"".

    Returns:
        str: Hash of the password and salt.
    """
    if salt == b"":
        return hashlib.sha256(password).hexdigest()

    return bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(password).digest()),
        salt
    )