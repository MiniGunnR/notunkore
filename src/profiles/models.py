from django.db import models
from django.contrib.auth.models import User

from common.models import Timestamped


class Profile(Timestamped):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    dob                 = models.DateField()
    divorced            = models.BooleanField(default=False)
    divorced_number     = models.SmallIntegerField(default=1)
    children            = models.BooleanField(default=False)
    children_number     = models.SmallIntegerField(default=1)
    description         = models.TextField()

    def get_full_name(self):
        return self.user.get_full_name()

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def username(self):
        return self.user.username

    def __str__(self):
        return self.get_full_name()


class Photos(Timestamped):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    photo               = models.ImageField(upload_to='photos/')
