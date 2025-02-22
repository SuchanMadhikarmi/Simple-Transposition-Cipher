def encrypt(message, key):
    ciphertext = [''] * key


    for x in range(key):
        pointer = x

        while pointer < len(message):
            ciphertext[x] += message[pointer]
            pointer += key 
    return ''.join(ciphertext)

def main():
    message = input("Enter your message")
    key = int(input("Enter your key"))
    print(encrypt(message, key))

if __name__ == "__main__":
    main()