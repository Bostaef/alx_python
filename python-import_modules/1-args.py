#!/usr/bin/python3

def print_arguments(arguments):
    num_args = len(arguments) - 1

    result = "{} argument{}:".format(num_args, "s" if num_args != 1 else "")

    if num_args == 0:
        result += "."
    else:
        result += "\n"
        for i in range(1, num_args + 1):
            result += "{}: {}\n".format(i, arguments[i])

    return result

if __name__ == "__main__":
    # Example usage:
    command_line_arguments = ["", "Hello", "Holberton", "School", "98", "Battery", "street"]
    
    # Call the function to print arguments
    output = print_arguments(command_line_arguments)
    
    # Print the result
    print(output)