# A simple guess the number game

def get_guess():
    
    # Input a prompted guess that is a number
    
    result = None
    while True:
        try:
            test = input("Guess a number> ")
            if type(test) == int:
                result = float(test)
            elif type(test) == str:
                result = str(test)
            break
        except:
            print(f'error')

    return result

if __name__ == "__main__":
    print('Your input is {}'.format(get_guess()))

    # dont understand what is wanted from the "formatting your output but this takes a str and int"