# importing sys allows for access to command line args...
import sys

# calling main() allows for the potential "Usage: error" return at lines 9 and 16... 
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python caesar.py k")
        return 1
        
    try:
        # type cast command line input
        key = int(sys.argv[1])
    except ValueError:
        print("Your input {} is not an integer value".format(sys.argv[1]))
        return 2
    
    # gather user input...as string
    plain = input("plaintext: ")
    cipher = []
    
    # convert user string input to a list of individual letters
    plain_list = list(plain)
    
    # convert alphabetic 'letters' to ints ... caesar-ize...and revert to letters....
    for letter in plain_list:
        if ord(letter) > 96 and ord(letter) < 123:
            cipher_letter = chr(((ord(letter) - 97) + key) % 26 + 97)
    
        elif ord(letter) > 64 and ord(letter) < 91:
            cipher_letter = chr(((ord(letter) - 65) + key) % 26 + 65)
    
        # non-alphabetic 'letters' need not change...
        else:
            cipher_letter = letter
    
        cipher.append(cipher_letter)
        
    # output "caesar-ized" list as a string....
    print("ciphertext: ", end = '')
    
    for letter in cipher:
        print(letter, end = '')
    
    print('')
    

if __name__ == "__main__":
    main()
