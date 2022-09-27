alphabet = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
,'a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("type encode to encrypt, type decode to decrypt\n")
text = input("Type your message.\n").lower()
shift = int(input("Type your desired shift number\n"))

#step 1 
#todo 1 
#create function called encrypt > takes text and shift as inputs
def encrypt(plain_text, shift_amount): 
    #todo 2 inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrpyted text.
    #taking two inputs. Text and shift. 
    message = ""

    for letter in plain_text:

        alpha_index = alphabet.index(letter)

        new_letter = alphabet[alpha_index + shift_amount]
        message += new_letter

    print(f'The encoded message is: {message}')
    return message

#step 2
#Create the decrypt function to take a shift amount and a message to unravel the encryption and 

def decrypt(plain_text, shift_amount): 
    #todo 2 inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrpyted text.
    #taking two inputs. Text and shift.

    message = ""

    for letter in plain_text:

        alpha_index = alphabet.index(letter)

        new_letter = alphabet[alpha_index - shift_amount]
        message += new_letter

    print(f'The decoded message is: {message}')

#step 3 - combine the encrypt/decrypt functions into a single function.

def shift_message(direction, plain_text,shift_amount):
    message = ""
    is_encode = True
    is_decode = True

    if direction == 'encode':
        is_encode = True
        is_decode = False

        for letter in plain_text:

            alpha_index = alphabet.index(letter)

            new_letter = alphabet[alpha_index + shift_amount]
            message += new_letter

    elif direction == 'decode':
        is_encode = False
        is_decode = True

        for letter in plain_text:
            alpha_index = alphabet.index(letter)

            new_letter = alphabet[alpha_index - shift_amount]
            message += new_letter    
    else:
        print("Thanks for using this cipher service, come agian!")
        exit()

    if is_encode:
        print(f'The encoded message is: {message}')
    elif is_decode:
        print(f'The decoded message is: {message}')

shift_message(direction=direction, plain_text=text, shift_amount=shift)
