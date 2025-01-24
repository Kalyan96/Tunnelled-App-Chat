import socket
import sys
import os
from Crypto.PublicKey import RSA

HOST = '192.168.71.172'
PORT = 65435

s = socket.socket (socket. AF_INET, socket. SOCK_STREAM)
s.connect((HOST, PORT))
print("connection to the host is successful..")

flag = False #check and create RSA key pairs here.

try:
    if os.stat("B_publickey.pen").st_size > 0:
        print("RSA key pairs already exist")
        pass
# Generates key if it doesn't exist
    else:
        key = RSA.generate(1024)
        f = open("B_privatekey. pen", "wb")
        f.write(key.exportKey('PEM'))
        f.close()

        pubkey = key.publickey
        f.open("_publickey.pen", "Wb")
        f.write(pubkey.exportKey( 'OpenSSH'))
        f.close()

except OSError:
    print("No file found, creating a new one....")
    flag = True
    key = RSA.generate(1024)
    f = open("B_privatekey. pen", "wb")
    f.write(key.exportKey( 'PEM'))
    f.close()
    pubkey = key.publickey
    f = open("B publickey.pen", "wb")
    f.write(pubkey.exportKey( 'OpenSSH'))


# sendong and reciving public keys
data = s.recv(1024)
file = open("A_publickey.pem", "wb"),
file.write(data)
file.close()

file = open("B_publickey.pem", "rb")
data = file.read()
s.send(data)
file.close()

# Function for encryption
def encrypt(msg):
    f = open("A publickey. pem", "rb")
    key = RSA. importKey(f.read())
    x = key.encrypt(bytes (msg, "utf-8"), 32)
    return x[0]

# Function for decryption
def decryptt(msg):
    f1 = open("B_privatekey.pem", "rb")
    key1 = RSA. importKey(f1.read() )
    z = key1.decrypt(msg) # try direct string
    return z.decode()# Decode the bytes data into string format, can use str(z. "utf-8")

#Function used to send messages
def sendmsg():
    data = input("msg to A: ")
    if data:
        s.send(encrypt(data))
        if data == "exit":
            if flag == True:
                os.remove("A_publickey. pem")
            sys.exit()
        else:
            doagain()
#Function used to receive messages
def recvmsg():
    recived = s.recv(2048)
    string = recived
    output = str(string)[1:]

    if decryptt(string) == "exit":
        print("A left the chatroom...")
        sys.exit()
    elif len(string) > 0:
        print("msg from A: ", "Orignal Message:", decryptt(string))
        print("Cipher text:", output)
    else:
        doagain()
# Recives and Decrypts the message using decrypt function, # prints cypher text i.e. message w/o decryption
while True:
    sendmsg()
    recvmsg()