from app.models.User import User
from app.models.UserPreferences import UserPreferences
from datetime import datetime

def parse_user_data_to_db(data: dict) -> User:
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = User(
        username=data.get('user', ''),  
        password=data.get('password', ''),  
        roles={
            "is_user_admin": True if data.get('is_user_admin') else False,
            "is_user_manager": True if data.get('is_user_manager') else False, 
            "is_user_tester": True if data.get('is_user_tester') else False 
        },
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
                roles={
            "is_user_admin": "is_user_admin -> admin" if data["roles"]["is_user_admin"] else "",
            "is_user_manager": "is_user_manager -> manager" if data["roles"]["is_user_manager"] else "",
            "is_user_tester": "is_user_tester -> tester" if data["roles"]["is_user_tester"] else ""
        },
        preferences=data.get('preferences'),  
        active=True if data.get('active', False) else False,  
        created_ts=data.get('created_ts', ''),  
        update_ts=data.get('update_ts', '')
    )
    return user