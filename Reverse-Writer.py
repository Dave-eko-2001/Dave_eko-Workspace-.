def reverse_string():
    # Prompt the user for input
    user_input = input("Enter a string to reverse: ")

    # Reverse the string using slicing
    reversed_string = user_input[::-1]

    # Output the reversed string
    print("Reversed string:", reversed_string)


# Call the function
reverse_string()
