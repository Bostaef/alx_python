# square.py

"""
This module defines a Square class.

A Square is defined by a private instance attribute 'size' with a getter and setter method.
"""

class Square:
    """
    This class represents a Square.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
          Raises:
          - TypeError: If size is not an integer.
          - ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Parameters:
        - value (int): The new size for the square.
          Raises:
          - TypeError: If value is not an integer.
          - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2