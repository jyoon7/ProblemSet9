from sys import argv

# Main function

def main(k):
    # Input plaintext
    plain = str(input("plaintext: "))
    # Encryption
    txt = encrypt(plain, k)
    print("ciphertext: ", end = "")
    for c in txt:
        print(c, end = "")
    print()
    # Decryption
    orig = decrypt(txt, k)
    print("decrypted: ", end = "")
    for c in orig:
        print(c, end = "")
    print()


# Encryption function 

def encrypt(plain, k):
    txt = [] # Create list to store encrypted text
    for c in plain:
        c = ord(c)
        # Force alphabetical characters to wrap around
        if ord("A") <= c <= ord("Z"): 
            k = k % 26
            c = (c + k) % (ord("Z") + 1)
            c = (c % ord("A")) + ord("A")
        elif ord("a") <= c <= ord("z"):
            k = k % 26
            c = (c + k) % (ord("z") + 1)
            c = (c % ord("a")) + ord("a")
        else:
            c = c + k
        c = chr(c)
        txt.append(c)
    return txt # Return list to main function


# Decryption function

def decrypt(txt, k):
    orig = [] # Create list to store decrypted text
    for c in txt:
        c = ord(c)
        # Force alphabetical characters to wrap around
        if ord("A") <= c <= ord("Z"): 
            k = k % 26
            c = c - k
            if c < ord("A"):
                c = c + 26
        elif ord("a") <= c <= ord("z"):
            k = k % 26
            c = c - k
            if c < ord("a"):
                c = c + 26
        else:
            c = c - k
        c = chr(c)
        orig.append(c)
    return orig # Return decrypted text to main function


# Run main function if there is only 1 argument, otherwise return error
if __name__ == "__main__":
    if len(argv) != 2:
        print ("Error")
        exit
    else:
        main(int(argv[1]))

