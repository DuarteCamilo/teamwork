"""
This module defines the MessageResponse class, which is used to represent a message response.
"""


class MessageResponse:
    """
    A class used to represent a Message Response.

    Attributes:
        message (str): The message to be returned.
    """

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message
