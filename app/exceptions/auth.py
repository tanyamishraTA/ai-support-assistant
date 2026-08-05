class AuthException(Exception):
    """Base exception for authentication errors."""
    pass


class UserAlreadyExistsException(AuthException):
    """Raised when a user tries to register with an existing email."""

    def __init__(self):
        super().__init__("User with this email already exists.")


class InvalidCredentialsException(AuthException):
    """Raised when email or password is invalid."""

    def __init__(self):
        super().__init__("Invalid email or password.")


class UserNotFoundException(AuthException):
    """Raised when the user cannot be found."""

    def __init__(self):
        super().__init__("User not found.")


class InvalidTokenException(AuthException):
    """Raised when JWT is invalid."""

    def __init__(self):
        super().__init__("Invalid or expired token.")