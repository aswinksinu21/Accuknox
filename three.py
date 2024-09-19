from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print("Signal triggered.")

def user_transaction():
    with transaction.atomic():
        user = User(username="test_user")
        user.save()
        print("User saved, but transaction not yet committed.")

user_transaction()
print("Transaction completed.")
