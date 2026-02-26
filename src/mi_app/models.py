from .exceptions import InvalidUserDataError, UserAlreadyExistsError, UserNotFoundError

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._validate_id(user_id)
        self._validate_email(email)
        self._validate_name(name)

        self._id = user_id
        self._name = name
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def _validate_id(self, user_id):
        if user_id <= 0:
            raise InvalidUserDataError("User id must be a positive integer")

    def _validate_email(self, email):
        if "@" not in email:
            raise InvalidUserDataError("Invalid email format")

    def _validate_name(self, name):
        if not name.strip():
            raise InvalidUserDataError("User name cannot be empty")
