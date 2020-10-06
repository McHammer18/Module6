"""
Morgan Christensen

module 6 - functions with parameters

10/05/20
"""


def multiply_string(message, n):
    """Function that prints out a message a set amount of times"""
    return str(message)*n


if __name__ == '__main__':
    user_message = input("Enter a message")
    user_number = int(input("How many times would you like it to repeat"))
    print(multiply_string(user_message, user_number))
