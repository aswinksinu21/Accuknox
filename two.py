import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

print(f"Main code running in thread: {threading.current_thread().name}")
user = User(username="test_user")
user.save()
