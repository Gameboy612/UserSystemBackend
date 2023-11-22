from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature
from typing import Tuple
from methods._utilities.str_to_bytes import str_to_bytes


def get_key_pairs(password: bytes | str) -> Tuple[bytes]:
    """Generates a public and private key.

    Args:
        password (bytes | str): User Password.

    Returns:
        Tuple[bytes]: Generates them in bytes.
    """
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    PUBLIC_KEY = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    PRIVATE_KEY = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption((password))
    )
    return (PUBLIC_KEY, PRIVATE_KEY)



def decrypt(private_key: bytes, ciphertext: bytes | str, password: bytes | str) -> bytes:
    """Decrypting the message.

    Args:
        private_key (bytes): Private key of user.
        ciphertext (bytes | str): Ciphertext.
        password (bytes | str): Password of user.

    Returns:
        bytes: Decrypted text.
    """
    private_key = serialization.load_pem_private_key(
        private_key,
        password=str_to_bytes(password),
    )
    
    plain_text = private_key.decrypt(
        str_to_bytes(ciphertext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plain_text

def encrypt(public_key: bytes, text: bytes | str) -> bytes:
    """Encrypting the message.

    Args:
        public_key (bytes): Public Key.
        text (bytes | str): Input Text.

    Returns:
        bytes: Cyphertext.
    """
    public_key = serialization.load_pem_public_key(
        public_key
    )
    ciphertext = public_key.encrypt(
        str_to_bytes(text),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def sign(private_key: bytes, message: bytes | str, password: bytes | str) -> bytes:
    """Provides a signature for the message.

    Args:
        private_key (bytes): Private Key.
        message (bytes | str): Message to sign.
        password (bytes | str): Password of user.

    Returns:
        bytes: Signature of the message.
    """
    private_key = serialization.load_pem_private_key(
        private_key,
        password=str_to_bytes(password),
    )
    signature = private_key.sign(
        str_to_bytes(message),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature

def verify(public_key: bytes, message: bytes | str, signature: bytes | str) -> bool:
    """Verifying the signature of the message.

    Args:
        public_key (bytes): Public Key of the user.
        message (bytes | str): Message to check.
        signature (bytes | str): Signature of the message.

    Returns:
        bool: Whether the signature is real.
    """
    public_key = serialization.load_pem_public_key(
        public_key
    )

    try:
        public_key.verify(
            str_to_bytes(signature),
            str_to_bytes(message),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

def main():
    keys = get_key_pairs(b"password123")
    print(keys)
    print(decrypt(keys[1], encrypt(keys[0], b"secret text"), b"password123"))
    print(verify(keys[0], b"secret text", sign(keys[1], b"secret text", b"password123")))

if __name__ == "__main__":
    main()