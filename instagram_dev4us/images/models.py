from django.db import models
from instagram_dev4us.users import models as user_models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Image(TimeStampModel):
    """ Image Model """
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete = models.DO_NOTHING)

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

class Comment(TimeStampModel):
    """ Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete = models.DO_NOTHING)
    image = models.ForeignKey(Image, null=True, on_delete = models.DO_NOTHING) 

    def __str__(self):
        return '{} - {}'.format(self.message, self.creator.username)

class Like(TimeStampModel):
    """ Like Model """

    creator = models.ForeignKey(user_models.User, null=True, on_delete = models.DO_NOTHING)
    image = models.ForeignKey(Image, null=True, on_delete = models.DO_NOTHING)

    def __str__(self):
        return '{} - {}'.format(self.image.caption, self.creator.username)

