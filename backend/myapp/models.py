from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg  



class Login(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

    def str(self):
        return self.username


class Profile(models.Model):
    WORKER_TYPE_WAGE_MAP = {
        'Electrician': 3500,
        'Plumber': 3000,
        'Carpenter': 5000,
        'Painter': 3800,
        'Mechanics': 4000,
    }

    user = models.OneToOneField('Login', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], 
        blank=False
    )
    worker_type = models.CharField(
        max_length=40, 
        choices=[(key, key) for key in WORKER_TYPE_WAGE_MAP.keys()],
        default='NULL'
    )
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=False)
    jobs_done = models.IntegerField()
    rating = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    minimum_wage = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # Automatically set minimum wage based on worker type
        self.minimum_wage = self.WORKER_TYPE_WAGE_MAP.get(self.worker_type, 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.worker_type})"


    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    def str(self):
        return self.user.username
    


class Rating(models.Model):
    customer_username = models.CharField(max_length=20)
    worker_username = models.CharField(max_length=20)
    ratings = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the rating

        # Automatically update the worker's rating in the Profile table
        self.update_worker_rating()

    def update_worker_rating(self):
        # Calculate the average rating for the worker
        average_rating = Rating.objects.filter(worker_username=self.worker_username).aggregate(Avg('ratings'))['ratings__avg']
        if average_rating:
            try:
                profile = Profile.objects.get(user__username=self.worker_username)
                profile.rating = average_rating
                profile.save()  # Save the updated profile rating
            except Profile.DoesNotExist:
                pass

    
class JobDetails(models.Model):
    worker_username = models.CharField(max_length=20)
    job_type = models.CharField(max_length=25)
    job_description = models.CharField(max_length=255)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.job_type} by {self.worker_username} at {self.location}"

    @classmethod
    def get_jobs_by_worker(cls, worker_username):
        return cls.objects.filter(worker_username=worker_username)

    def save(self, *args, **kwargs):
        if len(self.job_description) < 10:
            raise ValueError("Job description must be at least 10 characters long.")
        super().save(*args, **kwargs)

    def formatted_job_details(self):
        return {
            "worker": self.worker_username,
            "type": self.job_type,
            "description": self.job_description,
            "location": self.location,
        }



    