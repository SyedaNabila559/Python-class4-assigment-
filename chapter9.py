########## Lesson 09: Exception Handling  ##########

# Exception Handling with try, except, else, and finally
# Exception handling is a crucial part of writing robust Python programs. It allows you to handle errors gracefully and ensure your program doesn't crash unexpectedly. In this tutorial, we'll cover the try, except, else, and finally blocks with examples.

# 1.The try Block in Python 
# (The try block is used to test a block of code for errors. If an error occurs within the try block, the program will immediately jump to the except block (if provided).)
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except:
    print("An error occurred!")


# 2. The except Block 
# (The except block is used to handle specific errors that occur in the try block. You can specify the type of error to catch, or use a generic except to catch all errors.)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# 3. The else Block 
# (The else block is executed if no errors occur in the try block. It is optional and is used for code that should only run when the try block is successful.)
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful. Result: {result}")


# 4. The finally Block
# The finally block is executed regardless of whether an error occurred or not. It is often used for cleanup operations, such as closing files or releasing resources.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")


# 5. Putting It All Together
# Here’s an example that combines all four blocks:
def divide_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.")

# Test cases
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "2")  # TypeError


# Practice Problem:
# Write a Python program that asks the user for two numbers and divides them. Use exception handling to catch any errors that might occur (e.g., division by zero or invalid input).
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")


######### **************************** ##########