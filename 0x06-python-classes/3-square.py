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
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the square
        Return the current area of the square.
        """
        return (self.__size ** 2)
