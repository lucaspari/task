from dataclasses import dataclass
from app.models import UserPreferences


@dataclass
class User:
	username: str
	password: str
	roles: list
	preferences: UserPreferences
	created_ts: float
	update_ts: float
	active: bool = True