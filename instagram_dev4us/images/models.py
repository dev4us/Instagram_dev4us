from django.db import models
from instagram_dev4us.users import models as user_models
from taggit.managers import TaggableManager

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
    creator = models.ForeignKey(user_models.User, null=True, on_delete = models.CASCADE, related_name='images')
    tags = TaggableManager()

    @property
    def like_count(self):
        return self.likes.all().count()

    @property
    def comment_count(self):
        return self.comments.all().count()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']

class Comment(TimeStampModel):
    """ Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete = models.CASCADE, related_name='comments') 

    def __str__(self):
        return '{} - {}'.format(self.message, self.creator.username)

class Like(TimeStampModel):
    """ Like Model """

    creator = models.ForeignKey(user_models.User, null=True, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete = models.CASCADE, related_name='likes')

    def __str__(self):
        return '{} - {}'.format(self.image.caption, self.creator.username)

