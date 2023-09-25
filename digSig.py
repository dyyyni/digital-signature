from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

import hashlib

def hashFile(filename):
    sha256Hash = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(4096):
            sha256Hash.update(chunk)

    return sha256Hash.digest()


def main():

    filename = input("Enter filename: ")
    fileHash = hashFile(filename)

# Load the private key
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
                key_file.read(),
                password="kukka".encode('utf-8'),
                backend=default_backend()
                )

    signature = private_key.sign(
            fileHash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
                ),
            hashes.SHA256()
            )


    with open("./public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
                )

    try:
        public_key.verify(
                signature,
                fileHash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                    ),
                hashes.SHA256()
                )
        print("The signature is valid.")
    except:
        print("The signature is invalid.")

    return


if __name__ == "__main__":
    main()
