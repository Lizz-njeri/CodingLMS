from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher')
    )

    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=1)
    phone = models.CharField(max_length=15, null=True)  

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Assuming you store the phone number as a string

    # Add other fields as needed

    def __str__(self):
        return self.user.username + '' 