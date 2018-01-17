from django.db import models
from django.contrib.auth.models import User

from common.models import Timestamped


class Connected(Timestamped):
    user1       = models.ForeignKey(User, on_delete=models.CASCADE)
    user2       = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Connection: {user1} {user2}".format(user1 = self.user1, user2 = self.user2)

