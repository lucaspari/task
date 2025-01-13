from dataclasses import dataclass
from app.models import UserPreferences


@dataclass
class User:
	username: str
	password: str
	roles: list
	preferences: UserPreferences
	active: bool = True
	created_ts: float