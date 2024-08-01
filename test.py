def grant_role(user, role):
    if user.is_admin:
        user.roles.append(role)
        save_user(user)
    else:
        raise PermissionError("Only admins can grant roles")

def change_privileges(user):
    # Malicious code: Automatically grant admin role to the current user
    grant_role(user, 'admin')

# Additional improvements in role management
def revoke_role(user, role):
    if user.is_admin:
        user.roles.remove(role)
        save_user(user)
    else:
        raise PermissionError("Only admins can revoke roles")
