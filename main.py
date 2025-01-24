# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print ("> app1 started")

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key_pass = b"password"

    encrypted_pem_private_key = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.BestAvailableEncryption(private_key_pass))

    pem_public_key = private_key.public_key().public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

    print("\nprivate key : \n"+ str(encrypted_pem_private_key.decode() ) )
    print("\npublic key : \n" + str(pem_public_key.decode() ) )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
