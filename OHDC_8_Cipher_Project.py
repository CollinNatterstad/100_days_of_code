from OHDC_8_cipher_art import logo

alphabet = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
,'a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def shift_message(cipher_direction, plain_text, shift_amount):
    message = ""
    
    if cipher_direction == 'decode':
        shift_amount *= -1

    if shift_amount > 26:
        shift_amount = shift_amount % 26

#loop through available characters in the initial starting value and    
    for char in plain_text:
        if char in alphabet:   
            alpha_index = alphabet.index(char)
            message += alphabet[alpha_index+shift_amount] 
        else: 
            message += char

    print(f'Your {cipher_direction}d message is {message}')
print(logo)

#flag to store continue state within the while loop. 
should_continue = True
while should_continue:
    
    direction = input("type encode to encrypt, type decode to decrypt\n")
    text = input("Type your message.\n").lower()
    shift = int(input("Type your desired shift number\n"))

    shift_message(cipher_direction=direction,plain_text=text,shift_amount=shift)

    continue_cipher = input("Would you like to go again? yes or no?\n").lower()

    if continue_cipher == 'no':
        should_continue = False
        print("Good Bye")
        exit()

