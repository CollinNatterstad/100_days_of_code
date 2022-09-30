from OHDC_10_art import logo

def add(n1,n2):
    return n1+n2

def subt(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    
    if n2 > 0:
        return n1/n2

    elif n2 == 0:
        return "You cannot divide by zero."


def calculator():
    
    n1 = float(input("What is your first number?\n"))
    carry_on = True
    while carry_on:
        n2 = float(input("What is your next number?\n"))
        
        operations = {
            '+':add(n1,n2)
            ,'-':subt(n1,n2)
            ,'*':mult(n1,n2)
            ,'/':div(n1,n2)
            }
        
        for symbol in operations:
            print(symbol)

        operation = input("Choose the symbol of the calculation you'd like to perform.\n")
        
        answer = operations[operation]
        print(f'{n1} {operation} {n2} = {answer}')
        n1 = answer 
        cont = input("Would you like to continue with this calculation? y/n \n").lower()
        
        if cont == 'n':
            carry_on = False
            calculator()
print(logo)    
calculator()

