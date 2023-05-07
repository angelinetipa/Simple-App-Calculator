# use try catch
try:
    # input for math operation
    math_operation = input("Addition Subtraction Multiplication Division \nWhat math operation would you like to use?  ").strip().lower()
    # input for two numbers
    first_number, second_number = input("Enter your two numbers(add space between them): ").split()
    # if math operation is addtion, output sum of two numbers
    if math_operation == "addition":
        print(f"{first_number} + {second_number} = ", float(first_number) + float(second_number))
    # if math operation is subtraction, output difference of two numbers
    if math_operation == "subtraction":
        print(f"{first_number} - {second_number} = ", float(first_number) - float(second_number))
    # if math operation is multiplication, output product of two numbers
    if math_operation == "multiplication":
        print(f"{first_number} x {second_number} = ", float(first_number) * float(second_number))
    # if math operation is division, output quotient of two numbers
    if math_operation == "division":
        print(f"{first_number} / {second_number} = ", float(first_number) / float(second_number))
except SyntaxError:
    print("Something is wrong with syntax")
except ZeroDivisionError:
    print("Something is wrong with division. You are dividing by zero!")
except ValueError:
    print("Something is wrong with printing value")

# output of the result
# input for try again
# while try again is not no, repeat Step 1
# else, display "Thank you"
# exit program
finally:
    print("End of program.")