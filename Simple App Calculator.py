# use try catch
try:
    # input for math operation
    math_operation = input("Addition Subtraction Multiplication Division \nWhat math operation would you like to use?  ").strip().lower()
    # input for two numbers
    first_number, second_number = input("Enter your two numbers(add space between them): ").split()
    # if math operation is addtion, then add the two numbers
    if math_operation == "addition":
        print(f"{first_number} + {second_number} = ", float(first_number) + float(second_number))
    # if math operation is subtraction, then subtract the two numbers
    if math_operation == "subtraction":
        print(f"{first_number} - {second_number} = ", float(first_number) - float(second_number))
    # if math operation is multiplication, then multiply the two numbers
    # if math operation is division, then divide the two numners
except SyntaxError:
    print("Something is wrong with syntax")
except ZeroDivisionError:
    print("Something is wrong with division")
except ValueError:
    print("Something is wrong with printing value")

# output of the result
# input for try again
# while try again is not no, repeat Step 1
# else, display "Thank you"
# exit program
finally:
    print("End of program.")