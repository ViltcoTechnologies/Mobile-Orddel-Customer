import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ordel.settings')

import django
django.setup()

from django.contrib.auth.models import User



saved_user = User.objects.get(username="admin")
print(saved_user.password)
