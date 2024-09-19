import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)
    print("Signal ended")

user = User(username="test_user")
user.save()

print("Print after the signal completed")
