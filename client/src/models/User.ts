
export interface User {
  username: string;
  password: string;
  joinedRoles: string;
  roles: string[];
  preferences: string;
  is_user_admin: boolean;
  is_user_tester: boolean;
  is_user_manager: boolean;
  created_ts: string;
  update_ts: number;
  active: boolean;
}
