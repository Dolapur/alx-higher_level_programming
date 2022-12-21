#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """A class that represents a square"""
    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Return the current area of the square."""
        return (self.__size ** 2)
