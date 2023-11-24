import os
import django
from django.contrib.auth.models import User, Permission

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fundacion_apoyo_project.fundacion_apoyo_project.settings')
django.setup()

def get_user_permissions(username):
    try:
        user = User.objects.get(username=username)
        user_permissions = user.user_permissions.all()
        group_permissions = Permission.objects.filter(group__user=user)

        print(f"Permissions for User: {user.username}")
        print("User Permissions:")
        for permission in user_permissions:
            print(permission.codename)

        print("\nGroup Permissions:")
        for permission in group_permissions:
            print(permission.codename)
    except User.DoesNotExist:
        print(f"User '{username}' does not exist.")

# Usage example
get_user_permissions('your_username')