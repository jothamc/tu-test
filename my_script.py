import os

# Access the GitHub variable
github_variable = os.environ.get("MY_GITHUB_VARIABLE")

print(f"The value of MY_GITHUB_VARIABLE is: {github_variable}")

# Use the variable in your script
if github_variable:
    print(f"Received message: {github_variable}")
else:
    print("No message received")
