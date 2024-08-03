def string_operations():
    # Get user input
    user_string = input("Enter a string: ")

    # Reverse the string
    reversed_string = user_string[::-1]
    
    # Convert the string to uppercase
    uppercase_string = user_string.upper()
    
    # Check if the string is a palindrome
    is_palindrome = user_string == reversed_string

    # Print the results
    print(f"Original string: {user_string}")
    print(f"Reversed string: {reversed_string}")
    print(f"Uppercase string: {uppercase_string}")
    print(f"Is the string a palindrome? {'Yes' if is_palindrome else 'No'}")

# Run the function
string_operations()