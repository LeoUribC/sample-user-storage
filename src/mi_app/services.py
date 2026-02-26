from .models import User
from .storage import Storage
from .exceptions import UserNotFoundError, UserAlreadyExistsError, InvalidUserDataError


class UserService:
    def __init__(self, storage: Storage):
        self.storage = storage

    def create_user(self, user: User) -> None:
        self._validate_user(user)
        users = self.storage.load()
        self._ensure_user_is_unique(user, users)
        self._persist_new_user(user, users)

    def get_user(self, user_id: int) -> User:
        users = self.storage.load()
        for user in users:
            if user.id == user_id:
                return user
        raise UserNotFoundError(f"User {user_id} not found")

    def delete_user(self, user_id: int) -> None:
        users = self.storage.load()
        filtered = [u for u in users if u.id != user_id]

        if len(filtered) == len(users):
            raise UserNotFoundError(f"User {user_id} not found")

        self.storage.save(filtered)

    def _validate_user(self, user: User) -> None:
        self._validate_user_id(user.id)
        self._validate_user_name(user.name)
        self._validate_user_email(user.email)

    def _validate_user_id(self, user_id: int) -> None:
        if user_id <= 0:
            raise InvalidUserDataError("User id must be a positive integer")

    def _validate_user_name(self, name: str) -> None:
        if not name.strip():
            raise InvalidUserDataError("User name cannot be empty")

    def _validate_user_email(self, email: str) -> None:
        if "@" not in email:
            raise InvalidUserDataError("Invalid email format")

    def _ensure_user_is_unique(self, user: User, users: list[User]) -> None:
        if any(existing.id == user.id for existing in users):
            raise UserAlreadyExistsError(f"User with id {user.id} already exists")

    def _persist_new_user(self, user: User, users: list[User]) -> None:
        users.append(user)
        self.storage.save(users)
    
    def _normalize_user(self, user: User) -> User:
        user.name = user.name.strip().title()
        return user
    
    def _persist_user(self, user: User, users: list[User]) -> None:
        users.append(user)
        self.storage.save(users)

    def register_user(self, user: User) -> None:      # TESTEAR ESTA FUNCION
        self._validate_user(user)                     # hacerla fallar por el lado de validar usuario
        users = self.storage.load()
        self._ensure_user_is_unique(user, users)      # hacerla fallar por el lado de usuario duplicado
        normalized_user = self._normalize_user(user)
        self._persist_user(normalized_user, users)
