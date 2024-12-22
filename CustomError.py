# Define a custom exception class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Function that raises the custom error
def risky_function(value):
    if value < 0:
        raise CustomError("Value cannot be negative!")
    else:
        return f"Value is acceptable: {value}"

# Example usage
try:
    result = risky_function(-1)  # This will raise the error
    print(result)
except CustomError as e:
    print(f"An error occurred: {e.message}")
