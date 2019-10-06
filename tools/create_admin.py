from django.contrib.auth.models import User

users = User.objects.filter(username='admin')
if users:
    admin = users[0]
    admin.set_password('Pa55word')
    admin.save()
else:
    admin = User.objects.create_user(
        username='admin', is_staff=True, is_superuser=True)
    admin.set_password('Pa55word')
    admin.save()
