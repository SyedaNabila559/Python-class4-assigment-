######### Lesson 10: File Handling ########

# Opening a File
#In Python, files can be opened using the open() function. This function requires at least one argument, which is the file path. It can also take a second argument, which specifies the mode in which the file should be opened.

# 1: Reading a File
# To read the contents of a file, you can use several methods like read(), readline(), or readlines().
# Open file in read mode
file = open('example.txt', 'r')

# Read the entire content of the file
content = file.read()

# Print the content
print(content)

# Close the file after reading
file.close()

# 2: Writing to a File
# You can write content to a file using the write() method. If the file does not exist, it will be created.
# Open file in write mode (creates a new file if it doesn't exist)
file = open('output.txt', 'w')

# Write some text to the file
file.write("Hello, this is a test file!\n")
file.write("Writing some content to the file.")

# Close the file after writing
file.close()

# 3: Appending to a File
# If you want to add data to an existing file without overwriting its current contents, you can use 'a' mode (append mode).
file = open('output.txt', 'a')

# Append some text to the file
file.write("\nThis is a new line added to the file.")

# Close the file
file.close()

#  4: Using with Statement (Context Manager)
# The with statement is a better approach when working with files because it automatically closes the file when the block is finished. This prevents leaving files open by mistake.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

#  5: Reading CSV Files
# Python provides a csv module for handling CSV (Comma Separated Values) files. You can read CSV files in a structured way.
import csv

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# 6: Handling File Exceptions
# Sometimes, files might not exist, or there may be issues with file permissions. Python allows you to handle such exceptions using try and except blocks.
try:
    file = open('non_existent_file.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("Error: The file was not found!")
finally:
    print("Execution finished.")


########## ****************** #############