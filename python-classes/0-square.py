# square.py

"""
This module defines a Square class.

A Square is defined by a private instance attribute 'size'.
"""

class Square:
    """
    This class represents a Square.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes an instance of the Square class.

        Parameters:
        - size (int): The size of the square.
        """
        self.__size = size

    def get_size(self):
        """
        Get the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    def set_size(self, new_size):
        """
        Set the size of the square.

        Parameters:
        - new_size (int): The new size for the square.
        """
        self.__size = new_size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2