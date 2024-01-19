# 8BW_TASK_AUTOMATION
🌟Automate File Renaming Script in Python🌟
This Python script automates file renaming in a specified directory by adding a user-defined prefix. Using the os module, it navigates and renames each file by appending the chosen prefix. With error handling, the script offers a concise solution for efficient batch file renaming. This script is a handy tool for anyone dealing with large sets of files and wants to add a consistent prefix to their filenames.

WORKING:
1. User Input: The script takes user input for the destination path and the desired prefix for file renaming.
2. File Renaming Loop: It then iterates through all files in the specified directory, checking if each item is a file.
3. Renaming Process: For each file, it constructs a new filename by appending the provided prefix and then renames the file accordingly using the os.rename function.
4. Feedback: Throughout the process, the script provides feedback by printing the old and new filenames for each file.
5. Error Handling: The script includes error handling to catch any exceptions that may occur during the execution and prints an informative message.
