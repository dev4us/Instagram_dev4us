from django.db import models
from instagram_dev4us.users import models as user_models
from instagram_dev4us.images import models as image_models


class Notification(image_models.TimeStampModel):

    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow')
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name="creator")
    to = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name="to")
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'From: {} - To:{}'.format(self.creator, self.to)