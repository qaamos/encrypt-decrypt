from cryptography.fernet import Fernet

def encryptFile():

    filename = input("Enter filename: ")

    key = Fernet.generate_key()
    with open(filename+".key", "wb") as filekey:
        filekey.write(key)

    with open(filename, "rb") as file:
        original = file.read()
    
    fernet = Fernet(key)
    encrypted = fernet.encrypt(original)

    with open(filename, "wb") as encryptedFile:
        encryptedFile.write(encrypted)

    return 0

def decryptFile():

    filename = input("Enter filename: ")

    with open(filename+".key", "rb") as filekey:
        key = filekey.read()
    
    fernet = Fernet(key)

    with open(filename, "rb") as encryptedFile:
        encrypted = encryptedFile.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as decryptedFile:
        decryptedFile.write(decrypted)

    return 0

def main():

    mode = input("[e]ncrypt or [d]ecrypt: ")
    if mode == "e":
        encryptFile()
    elif mode == "d":
        decryptFile()

    return 0

if __name__ == "__main__":
    main()
