from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator


class Login(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

<<<<<<< HEAD
    def str(self):
=======
    def __str__(self):
>>>>>>> 2b4044a03d2cd5e7ef1ac029d7922d533084a71f
        return self.username





class Profile(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], 
        blank=False
    )
    worker_type = models.CharField(max_length=40, default='NULL')
    name = models.CharField(max_length=50, blank=False)
    address=models.CharField(max_length=50,blank=False)
    jobs_done=models.IntegerField()
    rating  = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )

    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
<<<<<<< HEAD
    def str(self):
        return self.user.username
=======
    def __str__(self):
        return self.user.username
>>>>>>> 2b4044a03d2cd5e7ef1ac029d7922d533084a71f
