from django.db import models

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    skills = models.JSONField()  # Store skills as JSON
    experience_level = models.CharField(max_length=50)
    # preferences will be handled in the serializer, not in the model directly



class JobPosting(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    required_skills = models.JSONField()  # List of required skills
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=50)
