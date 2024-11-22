"""
This module provides helper functions for hashing and verifying passwords using the passlib library.
Classes:
  HashHelper: A class containing static methods for hashing and verifying passwords.
Methods:
  hash_password(password: str) -> str:
    Hashes a plain text password using bcrypt algorithm.
  verify_password(plain_password: str, hashed_password: str) -> bool:
    Verifies a plain text password against a hashed password.
"""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashHelper:
    """
    HashHelper is a utility class that provides methods for hashing and verifying passwords.
    Methods:
      hash_password(password: str) -> str:
        Hashes the given password and returns the hashed password as a string.
      verify_password(plain_password: str, hashed_password: str) -> bool:
        Verifies that the plain password matches the hashed password.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes the given password and returns the hashed password as a string."""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verifies that the plain password matches the hashed password."""
        return pwd_context.verify(plain_password, hashed_password)
