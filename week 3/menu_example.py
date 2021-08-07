"""
Menu examples

"""

def show_menu(menu_list):
    skip_first_flag = True
    header_line = menu_list[0] # 0 tuple is the header
    print(header_line)
    for item in menu_list:
        if skip_first_flag:
            skip_first_flag = False
        else:
            print(f'{item[0]} {item[1]}')

def make_valid_numbers(menu_list):
    """
    Make a set of valid numbers from a menu_list
    """
    result = set()
    print("in make valid numbers:")
    first = True
    for a_tuple in menu_list:
        if first: 
            first = False
        else:
            result = result | {a_tuple[0]}
    return result

def run_menu(menu_list):
    """
    Display a menu
    """
    valid_numbers = make_valid_numbers(menu_list) # set of valid numbers1
    not_done = True
    while not_done:
        show_menu(menu_list)
        the_value = get_integer_input()
        if the_value in valid_numbers:
           the_cmd = menu_list[the_value][2]
           not_done = the_cmd(the_value)
        else:
          print(f"Oops! {the_value} is not a valid number")

def get_integer_input():
    """
    Input a number
    """
    result = None
    test = None
    while True:
        try:
            test = input("Enter a number:")
            result = int(test)
            break  
        except Exception:
            print(f'Oops! {test} was not a number')
            
    return result
    
def run_menu_one(a_value):
    menu_one =  (\
                   "Select a number.",\
                   (1,"Menu Burger",burg_cmd),  \
                   (2,"Menu Chips",fries_cmd),   \
                   (3,"Quit",quit_cmd)\
                 )
    run_menu(menu_one)
    return True

def run_menu_two(a_value):
    menu_two =  (\
                   "Select a number.",\
                   (1,"Menu Pizza",pizza_cmd),  \
                   (2,"Menu Moonshine",alchy_cmd),   \
                   (3,"Quit",quit_cmd)\
                 )
    run_menu(menu_two)
    return True

def burg_cmd(a_value):
    print('Enjoy your meal!\n  .-""""-.\n /\' .  \'. \\\n(`-..:...-\')\n ;-......-;\n  \'------\'')
    return True # continue

def fries_cmd(a_value):
    print('Enjoy your meal!\n\|/\//\n|`""`|\n|    |\n\____/')
    return True # continue

def pizza_cmd(a_value):
    print('Enjoy your meal!\n   __\n // ""--.._\n||  (_)  _ "-._\n||    _ (_)    \'-.\n||   (_)   __..-\'\n \\__..--""')
    return True # continue

def alchy_cmd(a_value):
    print('Enjoy your drink!\n    ...\n    :::  _\n .-\'   \':o)\n;        `;\n| .-----. |\n| : XXX : |\n| \'-----\' |\n\'=========\'\n')
    return True # continue

def test_cmd(a_value):
    print('This item is not here yet')
    return True # continue

def quit_cmd(a_value):
    print( 'Thank you, good-bye!')
    return False # stop

if __name__ == "__main__":
    # testing code for now
    menu_list = (\
                   "Select a number.",\
                   (1,"Menu One",run_menu_one),  \
                   (2,"Menu Two",run_menu_two),   \
                   (3,"Menu Three",test_cmd), \
                   (4,"Quit",quit_cmd)\
                 )
    run_menu(menu_list)