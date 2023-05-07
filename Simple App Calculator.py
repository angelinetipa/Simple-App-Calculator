# import time, os, colorama module
import time, os
from colorama import Fore, Back, Style, init
init(autoreset=True)


# use try catch
try:
    # while try again is not no, repeat Step 1 
    try_again = ""
    while try_again != "no":
        print(f"{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}   🌟  S I M P L E     A P P     C A L C U L A T O R  🌟   {Style.RESET_ALL}")
        # input for math operation
        math_operation = input(f" \n{Fore.MAGENTA}{Style.BRIGHT}>>>  Addition {Fore.GREEN}Subtraction {Fore.YELLOW}Multiplication {Fore.CYAN}Division  <<<\n{Style.RESET_ALL}{Style.BRIGHT}What math operation would you like to use?  {Style.RESET_ALL}").strip().lower()
        # input for two numbers
        first_number, second_number = input(f"{Style.BRIGHT}Enter your two numbers(add space between them): {Style.RESET_ALL}").split()
        # if math operation is addtion, output sum of two numbers
        if math_operation == "addition":
            print (f"{Fore.MAGENTA}{first_number} + {second_number} = ", float(first_number) + float(second_number))
        # if math operation is subtraction, output difference of two numbers
        elif math_operation == "subtraction":
            print(f"{Fore.GREEN}{first_number} - {second_number} = ", float(first_number) - float(second_number))
        # if math operation is multiplication, output product of two numbers
        elif math_operation == "multiplication":
            print(f"{Fore.YELLOW}{first_number} x {second_number} = ", float(first_number) * float(second_number))
        # if math operation is division, output quotient of two numbers
        elif math_operation == "division":
            print(f"{Fore.CYAN}{first_number} / {second_number} = ", float(first_number) / float(second_number))
        # if math operation not one of math operation
        else:
            print(f"{Fore.RED}Sorry, its not one of the math operations. 😔")
        # input for try again
        try_again = input(f"{Style.RESET_ALL}{Style.BRIGHT}Do you want to try again?😁  {Style.RESET_ALL}").strip().lower()
        # clear terminal
        time.sleep(0.5)
        os.system("cls")
    # else, display "Thank you"
    print(f"{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}   🌟  S I M P L E     A P P     C A L C U L A T O R  🌟   {Style.RESET_ALL}\n{Style.BRIGHT}Thank you for using my Simple App Calculator! ♥")
    
except SyntaxError:
    print(f"{Fore.RED}Something is wrong with syntax")
except ZeroDivisionError:
    print(f"{Fore.RED}Something is wrong with division. You are dividing by zero!")
except ValueError:
    print(f"{Fore.RED}Something is wrong with printing value")
except:
    print(f"{Fore.RED}Unkown Exception")
# exit program
finally:
    print(f"{Style.BRIGHT}Bye Bye!")