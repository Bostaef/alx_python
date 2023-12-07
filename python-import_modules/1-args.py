def print_arguments(arguments):
    num_args = len(arguments) - 1

    if num_args == 0:
        result = "0 arguments."
    else:
        result = "{} argument{}:\n".format(num_args, "s" if num_args != 1 else "")
        for i in range(1, num_args + 1):
            result += "{}: {}\n".format(i, arguments[i])

    return result

if __name__ == "__main__":
    # Example usage:
    command_line_arguments = ["", "Hello", "Holberton", "School", "98", "Battery", "street"]
    
    # Call the function to get the formatted output
    output = print_arguments(command_line_arguments)
    
    # Print the result
    print(output, end="")