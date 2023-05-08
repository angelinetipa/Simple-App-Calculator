# import time, os module
import time, os
from colorama import Fore, Back, Style, init
# to turn off color changes at the end of every print
init(autoreset=True)

# def to call calculator
def calculator():
    # while try again is not no, repeat Step 1 
    try_again = ""
    while try_again != "no":
        print(f"\n{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}")    
        # while math operation is not 1,2,3,4, repeat in choosing
        math_operation = ""
        while math_operation != "1" and math_operation != "2" and math_operation != "3" and math_operation != "4":   
            # input for math operation
            math_operation = input(f" \n{Fore.MAGENTA}{Style.BRIGHT}> > >  1. Addition {Fore.GREEN}2. Subtraction {Fore.YELLOW}3. Multiplication {Fore.CYAN}4. Division   < < <\n{Style.RESET_ALL}{Style.BRIGHT}Choose the number of math operation you would like to use:  {Style.RESET_ALL}").strip()
            # if math operation is not 1,2,3,4, print invalid input
            if math_operation != "1" and math_operation != "2" and math_operation != "3" and math_operation != "4":
                print(f"{Fore.RED}Invalid Input. Choose only the number from the given math operation ‼")
        # input for two numbers
        first_number, second_number = input(f"{Style.BRIGHT}Enter your two numbers(add space between them):  {Style.RESET_ALL}").split()
        # if math operation is addtion, output sum of two numbers
        if math_operation == "1":
            print (f"{Fore.MAGENTA}{first_number} + {second_number} = ", float(first_number) + float(second_number))
        # if math operation is subtraction, output difference of two numbers
        elif math_operation == "2":
            print(f"{Fore.GREEN}{first_number} - {second_number} = ", float(first_number) - float(second_number))
        # if math operation is multiplication, output product of two numbers
        elif math_operation == "3":
            print(f"{Fore.YELLOW}{first_number} x {second_number} = ", float(first_number) * float(second_number))
        # if math operation is division, output quotient of two numbers
        elif math_operation == "4":
            print(f"{Fore.CYAN}{first_number} / {second_number} = ", float(first_number) / float(second_number)) 
        # input for try again
        try_again = input(f"{Style.RESET_ALL}{Style.BRIGHT}Do you want to try again (yes/no)?😁  {Style.RESET_ALL}").strip().lower()
        # clear terminal
        time.sleep(0.5)
        os.system("cls")
        # else, display "Thank you"
        print(f"{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}\n{Style.BRIGHT}Thank you for using my Simple App Calculator! ♥")
    
# use try catch
try:
    #call calculator
    calculator()
# exception for syntax error
except SyntaxError:
    print(f"{Fore.RED}Something is wrong with syntax.")
    time.sleep(2.5)
    try_again = input(f"{Style.RESET_ALL}{Style.BRIGHT}Do you want to try again (yes/no)?😁  {Style.RESET_ALL}").strip().lower()
    if try_again == "yes":
        #call calculator to repeat the process
        calculator()
    # last message
    os.system("cls")
    print(f"{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}\n{Style.BRIGHT}Thank you for using my Simple App Calculator! ♥")
# exception for zero division error
except ZeroDivisionError:
    print(f"{Fore.RED}Something is wrong with division. You are dividing by zero!")
    time.sleep(2.5)
    try_again = input(f"{Style.RESET_ALL}{Style.BRIGHT}Do you want to try again (yes/no)?😁  {Style.RESET_ALL}").strip().lower()
    if try_again == "yes":
        #call calculator to repeat the process
        calculator()
    # last message
    os.system("cls")
    print(f"{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}\n{Style.BRIGHT}Thank you for using my Simple App Calculator! ♥")
# exception for value error
except ValueError:
    print(f"{Fore.RED}Some value is invalid for a given operation.")
    time.sleep(2.5)
    try_again = input(f"{Style.RESET_ALL}{Style.BRIGHT}Do you want to try again (yes/no)?😁  {Style.RESET_ALL}").strip().lower()
    if try_again == "yes":
        #call calculator to repeat the process
        calculator()
    # last message
    os.system("cls")
    print(f"{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}\n{Style.BRIGHT}Thank you for using my Simple App Calculator! ♥")
# exception for value error
except:
    print(f"{Fore.RED}Unkown Exception. ")
    time.sleep(2.5)
    try_again = input(f"{Style.RESET_ALL}{Style.BRIGHT}Do you want to try again (yes/no)?😁  {Style.RESET_ALL}").strip().lower()
    if try_again == "yes":
        #call calculator to repeat the process
        calculator()
    # last message
    os.system("cls")
    print(f"{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}\n{Style.BRIGHT}Thank you for using my Simple App Calculator! ♥")
# exit program
finally:
    print(f"{Style.BRIGHT}Bye Bye!")