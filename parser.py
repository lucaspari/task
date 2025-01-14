from app.models.User import User
from app.models.UserPreferences import UserPreferences
from datetime import datetime

def parse_user_data_to_db(data: dict) -> User:
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    roles = []
    if data.get('is_user_admin') == True:
        roles.append("admin")
    if data.get('is_user_manager') == True:
        roles.append("manager")
    if data.get('is_user_tester') == True:
        roles.append("tester")
    user = User(
        username=data.get('user', ''),  
        password=data.get('password', ''),  
        roles=roles,
        preferences=UserPreferences(data.get('user_timezone')).timezone,  
        active=True if data.get('is_user_active') else False,  
        created_ts=data.get('created_at', ''),  
        update_ts=current_time
    )
    return user

def parse_user_data_to_server(data: dict) -> User:
    user = User(
        username=data.get('username', ''),  
        password=data.get('password', ''),  
                roles=data.get('roles'),
        preferences=data.get('preferences'),  
        active=True if data.get('active', False) else False,  
        created_ts=data.get('created_ts', ''),  
        update_ts=data.get('update_ts', '')
    )
    return user