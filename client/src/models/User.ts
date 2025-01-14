export interface UserPreferences {
  timezone: string;
}

export interface User {
  username: string;
  password: string;
  joinedRoles: string;
  roles: string[];
  preferences: UserPreferences;
  is_user_admin: boolean;
  is_user_tester: boolean;
  is_user_manager: boolean;
  created_ts: number;
  update_ts: number;
  active: boolean;
}
